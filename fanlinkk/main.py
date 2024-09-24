import sys
import os
import logging
import json
import time
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QDialog, QCheckBox, QSizePolicy, QSpacerItem
from PySide6.QtCore import QThread, QTimer, QDateTime, Signal, QObject, Slot, QSize, Qt, QDate, QTime, QUrl
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QFont, QIcon

import pyqtgraph as pg
from collections import defaultdict

import db_utils, grab2
from sqlalchemy import select
from datetime import datetime, timedelta
import requests


import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.dates import DateFormatter
from matplotlib.ticker import MaxNLocator , MultipleLocator
from datetime import datetime, timedelta




from grab2 import DataFetcher

from MainView import MainViewer

import getnotifs
from DashboardPage import DashboardWidget

from EmployeeReportsPage import EmployeeReports
from ChatterAnalytics import ChatterAnalyticia
from FSHome import FSHomePage
from FLSettings import FLSettingsPage
from RotaPage import Rota
from TeamLayoutPage import TeamLayout
from ManageCreatorsPage import ManageCreators
from creator_loader import load_creators
from db_utils import set_active_user, get_active_user, dbinitialize , DBWorker, Session, models, users, user_models
import db_utils
from token_utils import TokenUtils
from Login import LoginPage
from Menu import MenuWidget
from login_test import run_browser_app, BrowserApp
from django_utils import DjangoUtils
from token_utils import TokenUtils



dbinitialize()





def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)






class ModelDataWorker(QObject):
    
    model_data_refreshed = Signal(list)

    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id

    @Slot()
    def refresh_model_data(self):
        models = db_utils.get_models_for_user(self.user_id)
        model_names = []

        for model in models:
            logging.info(f"\n\nModel data: {model}\n\n")
            model_email = model.get('email')
            csrf_cookies = model.get('csrf_cookies')
            auth_token = model.get('auth_token')

            model_name = model.get('name')
            if model_name:
                model_names.append(model_name)

            if csrf_cookies and auth_token:
                cookies = {
                    'email': model_email,
                    'csrf_cookies': csrf_cookies,
                    'auth_token': auth_token
                }

                model_data = {}
                for i, url in enumerate(grab2.links):
                    logging.info(f"\nFetching data for {model_email}\n")
                    print('Fetching data...')
                    data = grab2.filegrab(i, url, cookies, model_email)
                    print(model_email)
                    model_data[f'response_{i}'] = data
                    logging.info(f"\n{model_email} DATA: {model_data}\n")
            else:
                logging.warning(f"No valid cookies or auth token for {model_name} ({model_email}). Skipping.")

        self.model_data_refreshed.emit(model_names)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Fanlinkk")
        self.setWindowIcon(QIcon("Icon.ico"))
        self.setGeometry(50, 50, 1200, 900)
        self.django_utils = DjangoUtils()
        self.token_utils = TokenUtils()
        self.selected_models = []  # List of selected models
        self.selected_time_range = 7  # Default time range (last 7 days)

        self.model_data = {}  # Dictionary to store the last fetched data for each model # NEW ADDITION
        self.total_subs = 00  # Total subscriptions
        self.total_purchases = 00  # Total purchases
        self.total_tips = 00  # Total tips
        self.total_all = 00

        self.session = requests.Session() 



        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()

        self.Menu = MenuWidget()

        left_layout.addWidget(self.Menu)
        # self.icon_menu = IconMenu()
        # self.full_menu = FullMenu()
        # left_layout.addWidget(self.icon_menu)
        # left_layout.addWidget(self.full_menu)

        right_layout = QVBoxLayout()
        # self.top_bar = TopBar()
        # right_layout.addWidget(self.top_bar)

        self.stacked_widget = QStackedWidget()
        self.dashboard = DashboardWidget()





        self.stacked_widget.addWidget(self.dashboard)
        self.hide_fanservice_buttons()

        # Heartbeat timer
        self.heartbeat_timer = QTimer(self)
        self.heartbeat_timer.timeout.connect(self.send_heartbeat)
        self.heartbeat_timer.start(60000)  # 5 minutes interval

        # Matplotlib integration with PyQt
        self.dashboard_graph = self.dashboard.ui.SalesGraphDashboard  # Assuming it's already defined in your UI
        self.dashboard_graph_layout = QVBoxLayout(self.dashboard_graph)  # Assuming it's a QWidget placeholder
        self.dashboard_graph_layout.setContentsMargins(0,0,0,0)
        self.dashboard_graph.setStyleSheet(u"background-color:#373737;\n"
"    border-radius: 48px; \n"
"    padding: 12px; ")


        # Create a matplotlib Figure and FigureCanvas

        plt.rcParams['font.family'] = 'Arial'
        self.fig, self.ax = plt.subplots()
        plt.tight_layout()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.last_xlim = None  # Store the last xlim
        self.last_ylim = None  # Store the last ylim



        # Add the canvas to the layout
        self.dashboard_graph_layout.addWidget(self.canvas)
        self.clear_graph()

        self.FSHome = FSHomePage()
        self.stacked_widget.addWidget(self.FSHome)



        # self.ChatterAnalytics = ChatterAnalyticia()
        # self.stacked_widget.addWidget(self.ChatterAnalytics)

        self.TeamLayoutPage = TeamLayout()
        self.stacked_widget.addWidget(self.TeamLayoutPage)



        self.FLSettings = FLSettingsPage()
        self.stacked_widget.addWidget(self.FLSettings)

        self.ManageCreator = ManageCreators()
        self.stacked_widget.addWidget(self.ManageCreator)

        self.main_view = MainViewer()
        self.main_view.setCentralWidget(self.stacked_widget)
        right_layout.addWidget(self.main_view)

        main_layout.addLayout(left_layout, 0)
        main_layout.addLayout(right_layout, 9)


        right_layout.setContentsMargins(0,0,0,0)
        right_layout.setStretch(2,9)
        left_layout.setContentsMargins(0,0,0,0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        central_widget = QWidget()
        central_widget.setStyleSheet(u"background-color:#141414;\n")
        central_widget.setLayout(main_layout)
        


        self.setCentralWidget(central_widget)
        

        self.setup_connections()
        self.setup_db_worker()
        self.load_creators_into_table()
        self.load_model_checkboxes()

    def send_heartbeat(self):
            session_data = read_session_file('session.json')
            if session_data:
                access_token = session_data.get('access_token')
                refresh_token = session_data.get('refresh_token')

                headers = {
                    'Authorization': f'Bearer {access_token}'
                }

                try:
                    response = self.session.get('http://127.0.0.1:8000/api/heartbeat/', headers=headers)

                    if response.status_code == 401:
                        logging.info("Access token expired, refreshing token...")
                        # Use the utility function to refresh the access token
                        new_access_token = self.django_utils.refresh_access_token(refresh_token)
                        if new_access_token:
                            self.new_access_token = new_access_token
                            headers['Authorization'] = f'Bearer {self.new_access_token}'
                            response = self.session.get('http://127.0.0.1:8000/api/heartbeat/', headers=headers)
                        else:
                            logging.error("Failed to refresh access token.")
                            return

                    if response.status_code == 200:
                        logging.info('Heartbeat sent successfully.')
                    else:
                        logging.warning(f'Failed to send heartbeat: {response.status_code}')

                except requests.RequestException as e:
                    logging.error(f'Error sending heartbeat: {e}')
            else:
                logging.warning('No session data found. Cannot send heartbeat.')

    def update_fs_home_url(self, new_url):
        # This will load the new URL in the FSHomePage's browser
        self.FSHome.browser_window.setUrl(QUrl(new_url))





    QApplication.processEvents()





    def load_model_checkboxes(self):
        session = Session()
        try:
            # Get the currently active user's email
            active_user_email = self.token_utils.get_email
            if not active_user_email:
                logging.error("No active user found.")
                return

    


            # Fetch models assigned to the active user
            result = self.django_utils.get_models_for_user()
            # Update the checkboxes with the models assigned to the active user
            self.update_dashboard_checkboxes(result)
            self.enable_checkboxes(None)

            logging.info(f"Model checkboxes updated and enabled successfully for user {active_user_email}.")
        except Exception as e:
            logging.error(f"An error occurred while updating model checkboxes: {e}")
        finally:
            session.close()

    def disable_checkboxes(self):
        for checkbox, _ in self.get_checkboxes():
            checkbox.setEnabled(False)

    def enable_checkboxes(self, _):
        for checkbox, _ in self.get_checkboxes():
            checkbox.setEnabled(True)

    def get_checkboxes(self):
        return [
            (self.dashboard.ui.MBoxone, self.dashboard.ui.Model_1Pic),
            (self.dashboard.ui.MBoxtwo, self.dashboard.ui.Modle_2Pic),
            (self.dashboard.ui.MBoxthree, self.dashboard.ui.Model_3Pic),
            (self.dashboard.ui.MBoxfour, self.dashboard.ui.Model_4Pic),
        ]

    def update_dashboard_checkboxes(self, result):
        placeholder_image_path = resource_path("images/user.svg")
        checkboxes = self.get_checkboxes()

        for i, (model_name, image_path, model_email) in enumerate(result):
            if i < len(checkboxes):
                checkbox, image_label = checkboxes[i]
                normalized_model_name = model_name.lower().replace(" ", "_").replace('_response', '')
                checkbox.setText(normalized_model_name.capitalize())
                checkbox.setProperty('model_email', model_email)
                checkbox.setVisible(True)
                checkbox.setEnabled(True)  # Enable checkbox

                checkbox.toggled.connect(lambda checked, name=model_email: self.print_checkbox_state(name, checked))

                if image_path and os.path.exists(image_path):
                    self.set_rounded_image(image_label, image_path)
                else:
                    self.set_rounded_image(image_label, placeholder_image_path)

                image_label.setVisible(True)
            else:
                checkbox.setVisible(False)
                image_label.setVisible(False)

        for i in range(len(result), len(checkboxes)):
            checkbox, image_label = checkboxes[i]
            checkbox.setVisible(False)
            image_label.setVisible(False)

        # Check if there is an odd number of models and add a horizontal spacer if so
 

        QApplication.processEvents()

    def set_rounded_image(self, image_label, image_path):
        # Set the size of the QLabel (e.g., 64x64)
        image_label.setFixedSize(48, 48)

        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(image_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        # Scale the pixmap to fit exactly the size of the label
        scaled_pixmap = pixmap.scaled(image_label.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        # Create a mask with a transparent background
        mask = QPixmap(image_label.size())
        mask.fill(Qt.transparent)

        # Start painting on the mask
        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        path = QPainterPath()
        path.addEllipse(0, 0, image_label.width(), image_label.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, scaled_pixmap)
        painter.end()

        image_label.setPixmap(mask)

        image_label.setStyleSheet(f"""
            QLabel {{
                border-radius: {image_label.width() // 2}px;
                border: 2px solid #0A0A0A;
                padding: 0px;
                background-color: transparent;
            }}
        """)

        image_label.repaint()
        QApplication.processEvents()

    def print_checkbox_state(self, model_name, is_checked):
        logging.info(f"Checkbox for {model_name} toggled. Checked: {is_checked}")

        if is_checked:
            if model_name not in self.selected_models:
                self.selected_models.append(model_name)
                logging.info(f"Model {model_name} added to selected models: {self.selected_models}")
        else:
            if model_name in self.selected_models:
                self.selected_models.remove(model_name)
                # Subtract the model's data from the totals if it was fetched
                if model_name in self.model_data:
                    subs, purchases, tips = self.model_data.pop(model_name)
                    self.total_subs -= subs
                    self.total_purchases -= purchases
                    self.total_tips -= tips
                    logging.info(f"Model {model_name} removed from selected models: {self.selected_models}")

        # Fetch and update notifications for the selected models
        self.fetch_notifications()

    def load_creators_into_table(self):
        table_widget = self.ManageCreator.ui.tableWidget
        load_creators(table_widget, self)

    def setup_connections(self):
        self.Menu.ui.DAMain.clicked.connect(self.show_dashboard)
        # self.full_menu.ui.ANMain.clicked.connect(self.show_AnalyticsSide)
        self.Menu.ui.CEMain.clicked.connect(self.ManageCreatorsPage)
        self.Menu.ui.TEMain.clicked.connect(self.TeamLayPage)
        self.Menu.ui.FSMain.clicked.connect(self.show_FanSide)
        self.Menu.ui.SEMain.clicked.connect(self.FanlinkkSettingsPage)
        # self.top_bar.ui.SidebarExpand.clicked.connect(self.toggle_sidebar)
        # self.full_menu.ui.HomeButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/home"))
        
        self.Menu.ui.InsightsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/insights"))
        self.Menu.ui.NotificationsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/notifications/all"))
        # self.top_bar.ui.NOTopBar.clicked.connect(self.show_FanSide)
        # self.top_bar.ui.NOTopBar.clicked.connect(lambda:self.update_fs_home_url("https://fanvue.com/notifications/all"))
        self.Menu.ui.NewPostsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/create"))

        # #self.full_menu.ui.NewPostsButton.clicked.connect(self.FSNewPostsPage)
       
        self.Menu.ui.QueueButton.clicked.connect(lambda: self.update_fs_home_url("https://www.fanvue.com/queue"))
        self.Menu.ui.VaultButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/vault"))
         # self.full_menu.ui.ProfileButton.clicked.connect(lambda: self.update_fs_home_url("https://www.fanvue.com/profile"))
        
        # self.full_menu.ui.ManageCreatorsButton.clicked.connect(self.ManageCreatorsPage)
        # self.full_menu.ui.SEMain.clicked.connect(self.FanlinkkSettingsPage)
        # self.full_menu.ui.TeamLayoutButton.clicked.connect(self.TeamLayPage)
        self.ManageCreator.ui.LinkAccountButton.clicked.connect(self.link_account)
        self.ManageCreator.ui.LinkAccountButton.clicked.connect(self.fetch_model_data)

        self.dashboard.ui.DateTodayButton.clicked.connect(lambda: self.handle_time_button_clicked(1))
        self.dashboard.ui.DateYesterdayButton.clicked.connect(lambda: self.handle_time_button_clicked(2))
        self.dashboard.ui.DateWeekButton.clicked.connect(lambda: self.handle_time_button_clicked(7))
        self.dashboard.ui.DateMonthButton.clicked.connect(lambda: self.handle_time_button_clicked(230))

        for checkbox, _ in self.get_checkboxes():
            checkbox.toggled.connect(self.on_checkbox_toggled)


        self.Menu.ui.FSMain.clicked.connect(self.show_fanservice_buttons)
        self.Menu.ui.DAMain.clicked.connect(self.hide_fanservice_buttons)
        self.Menu.ui.ANMain.clicked.connect(self.hide_fanservice_buttons)
        self.Menu.ui.TEMain.clicked.connect(self.hide_fanservice_buttons)
        self.Menu.ui.CEMain.clicked.connect(self.hide_fanservice_buttons)
        self.Menu.ui.SEMain.clicked.connect(self.hide_fanservice_buttons)

    def show_fanservice_buttons(self):
        # Show the Fanservice buttons
        self.Menu.ui.HomeButton.show()
        self.Menu.ui.NotificationsButton.show()
        self.Menu.ui.VaultButton.show()
        self.Menu.ui.QueueButton.show()
        self.Menu.ui.InsightsButton.show()
        self.Menu.ui.NewPostsButton.show()

    def hide_fanservice_buttons(self):
        # Hide the Fanservice buttons
        self.Menu.ui.HomeButton.hide()
        self.Menu.ui.NotificationsButton.hide()
        self.Menu.ui.VaultButton.hide()
        self.Menu.ui.QueueButton.hide()
        self.Menu.ui.InsightsButton.hide()
        self.Menu.ui.NewPostsButton.hide()







    def setup_db_worker(self):
        self.db_worker = DBWorker()
        self.db_thread = QThread()
        self.db_worker.moveToThread(self.db_thread)
        self.db_thread.started.connect(self.db_worker.initialize)
        self.db_worker.initialize_finished.connect(self.on_initialize_finished)
        self.db_worker.models_for_user_retrieved.connect(self.on_models_for_user_retrieved)
        self.db_worker.cookies_for_model_retrieved.connect(self.on_cookies_for_model_retrieved)
        self.db_worker.data_inserted_or_updated.connect(self.on_data_inserted_or_updated)
        self.db_thread.start()

    def on_checkbox_toggled(self, checked):
        checkbox = self.sender()
        model_email = checkbox.property('model_email')

        if checked:
            if model_email not in self.selected_models:
                self.selected_models.append(model_email)
                logging.info(f"Model {model_email} added to selected models.")
        else:
            if model_email in self.selected_models:
                self.selected_models.remove(model_email)
                logging.info(f"Model {model_email} removed from selected models.")

        self.fetch_notifications()

    def handle_time_button_clicked(self, days):
        self.selected_time_range = days
        self.fetch_notifications()

    def fetch_notifications(self):
        logging.info("Fetching notifications for selected models...")

        if not self.selected_models:
            logging.info("No models selected. Resetting totals to zero.")
            self.total_subs = 0
            self.total_purchases = 0
            self.total_tips = 0
            self.total_all = 0
            self.update_dashboard_with_notifications()
            self.clear_graph()
            return

        self.total_subs = 0
        self.total_purchases = 0
        self.total_tips = 0
        self.model_data = {}

        for model in self.selected_models:
            subs = getnotifs.get_notifications_for_models_and_time(model, self.selected_time_range, event_type=10)
            purchases = getnotifs.get_notifications_for_models_and_time(model, self.selected_time_range, event_type=9)
            tips = getnotifs.get_notifications_for_models_and_time(model, self.selected_time_range, event_type=11)

            total_subs_for_model = sum(subs.values())
            total_purchases_for_model = sum(purchases.values())
            total_tips_for_model = sum(tips.values())

            self.model_data[model] = {
                "subs": total_subs_for_model,
                "purchases": total_purchases_for_model,
                "tips": total_tips_for_model
            }

            self.total_subs += total_subs_for_model
            self.total_purchases += total_purchases_for_model
            self.total_tips += total_tips_for_model

        logging.info(f"Model data: {self.model_data}")

        self.total_all = self.total_subs + self.total_purchases + self.total_tips

        logging.info(f"Total Subs = {self.total_subs}, Purchases = {self.total_purchases}, Tips = {self.total_tips}, All = {self.total_all}")

        self.update_dashboard_with_notifications()
        self.plot_cumulative_notifications(self.selected_time_range)

    def update_dashboard_with_notifications(self):
        logging.info(f"Total Subs = {self.total_subs:.2f}, Purchases = {self.total_purchases:.2f}, Tips = {self.total_tips:.2f}")
        logging.info(f"Total All = {self.total_all:.2f}")

        self.dashboard.ui.TipsDollarDash.setText(f'${self.total_tips:.2f}')
        self.dashboard.ui.SubscribersDollarDash.setText(f'${self.total_subs:.2f}')
        self.dashboard.ui.PurchasesDollarDash.setText(f'${self.total_purchases:.2f}')
        self.dashboard.ui.TotalDollarDash.setText(f'${self.total_all:.2f}')

        self.dashboard.ui.TipsDollarDash.repaint()
        self.dashboard.ui.SubscribersDollarDash.repaint()
        self.dashboard.ui.PurchasesDollarDash.repaint()
        self.dashboard.ui.TotalDollarDash.repaint()
        QApplication.processEvents()

    def ClearLogin(self):
        self.ManageCreator.ui.DisplayNameLineEdit.clear()
        self.ManageCreator.ui.LoginEmailLineEdit.clear()
        self.ManageCreator.ui.PasswordLineEdit.clear()

    def setup_data_fetcher(self):
        self.data_fetcher = DataFetcher(user_id=1)
        self.data_fetcher.data_fetched.connect(self.on_data_fetched)
        self.fetch_timer = QTimer(self)
        self.fetch_timer.timeout.connect(self.start_data_fetching)

    def start_data_fetching(self):
        if not self.data_fetcher.isRunning():
            self.data_fetcher.start()
            logging.info("Fetching... THE DATA")

    # # def update_dashboard(self):
    #     logging.info("Starting grapher to update dashboard...")
    #     self.start_grapher()

    def on_data_fetched(self, models_data):
        #logging.info(f"Data fetched: {models_data}")
        pass

    def get_dates_in_range(self, time_range):
        today = QDateTime.currentDateTime()
        date_list = [today.addDays(-i).toString("yyyy-MM-dd") for i in range(time_range)]
        return date_list

    def set_last_time_range(self, selected_time_range):
        self.last_selected_time_range = selected_time_range

    def clear_graph(self):
        """
        Clears the graph and applies a professional, static style.
        The graph displays a default layout with gridlines but no tick labels.
        """
        logging.info("Clearing graph and applying professional static styling.")

        # Clear the entire axes
        self.ax.clear()

        # Set the background and other graph properties for a clean, professional look
        self.fig.patch.set_facecolor('none')
        self.ax.set_facecolor('#474747')         # Very light gray for the plot area background

        # Set axis labels (you can customize these or leave them empty)
        self.ax.set_title("Cumulative Profits", fontsize=16, color='#ffffff', pad=2)
        self.ax.set_xlabel("Date", fontsize=12, color='#ffffff', labelpad=2)
        self.ax.set_ylabel("Profits $", fontsize=12, color='#ffffff', labelpad=2, rotation=90)

        # Remove both tick labels but keep the gridlines
        self.ax.set_xticklabels([])  # Hide tick labels on the x-axis
        self.ax.set_yticklabels([])  # Hide tick labels on the y-axis

        # Enable grid lines for both x and y axes
        self.ax.grid(True, which='both', color='#CCCCCC', linestyle='--', linewidth=1)

        # Set x and y axis limits for a static layout
        self.ax.set_xlim([0, 30])  # Assuming a 30-day static range
        self.ax.set_ylim([-1, 100])  # Adjust the profit range based on your data

        # Set 10x10 gridlines with consistent spacing
        self.ax.xaxis.set_major_locator(MaxNLocator(nbins=10))
        self.ax.yaxis.set_major_locator(MaxNLocator(nbins=10))

        # Remove the legend if it's present
        self.ax.legend_ = None

        # Adjust layout for reduced left padding
        self.fig.subplots_adjust(left=0.065, right=0.95, top=0.90, bottom=0.12)

        # Force the canvas to update and reflect the changes
        self.canvas.draw()

        # Log new limits for verification
        logging.info(f"Graph cleared with xlim: {self.ax.get_xlim()}, ylim: {self.ax.get_ylim()}")

    def plot_cumulative_notifications(self, selected_time_range):
        logging.info(f"Plotting cumulative notifications for {self.selected_models} over {selected_time_range} days.")

        # Clear the graph if no models are selected
        if not self.selected_models:
            self.clear_graph()
            return

        today = datetime.now().date()

        # Clear the previous plot
        self.ax.clear()

        # Set the background and axis properties for a clean, professional look
        self.fig.patch.set_facecolor('none')  # Dark background for the figure
        self.ax.set_facecolor('#474747')         # Light gray for the plot area background

        # Initialize cumulative totals for all selected models
        total_cumulative_subs = [0] * selected_time_range
        total_cumulative_purchases = [0] * selected_time_range
        total_cumulative_tips = [0] * selected_time_range
        total_cumulative_total = [0] * selected_time_range

        timestamps = []
        for day_offset in range(selected_time_range - 1, -1, -1):
            day_date = today - timedelta(days=day_offset)
            timestamps.append(day_date)

        if len(timestamps) > 1 or selected_time_range == 1:
            for model_email in self.selected_models:
                model_data = db_utils.fetch_event_data(model_email=model_email)

                logging.debug(f"Fetched model data for {model_email}: {model_data}")

                cumulative_subs = 0
                cumulative_purchases = 0
                cumulative_tips = 0
                cumulative_total = 0

                for i, day_offset in enumerate(range(selected_time_range - 1, -1, -1)):
                    day_date = today - timedelta(days=day_offset)
                    filtered_data = {k: v for k, v in model_data.items() if k == day_date}
                    day_data = filtered_data.get(day_date, {'subs': [0], 'purchases': [0], 'tips': [0]})

                    daily_subs = sum([val for val in day_data.get('subs', [0]) if val > 0]) / 100
                    daily_purchases = sum([val for val in day_data.get('purchases', [0]) if val > 0]) / 100
                    daily_tips = sum([val for val in day_data.get('tips', [0]) if val > 0]) / 100

                    cumulative_subs += daily_subs
                    cumulative_purchases += daily_purchases
                    cumulative_tips += daily_tips
                    cumulative_total += daily_subs + daily_purchases + daily_tips

                    total_cumulative_subs[i] += cumulative_subs
                    total_cumulative_purchases[i] += cumulative_purchases
                    total_cumulative_tips[i] += cumulative_tips
                    total_cumulative_total[i] += cumulative_total

            # Plot cumulative data with professional color scheme
            self.ax.plot(timestamps, total_cumulative_subs, color='#1f77b4', linewidth=2, label="Total Subscriptions")
            self.ax.plot(timestamps, total_cumulative_purchases, color='#2ca02c', linewidth=2, label="Total Purchases")
            self.ax.plot(timestamps, total_cumulative_tips, color='#ff7f0e', linewidth=2, label="Total Tips")
            self.ax.plot(timestamps, total_cumulative_total, color='#d62728', linewidth=2, label="Total")

            # Set the title, x-axis, and y-axis labels
            self.ax.set_title("Cumulative Profits", fontsize=16, color='#ffffff', pad=20)
            self.ax.set_xlabel("Date", fontsize=12, color='#ffffff', labelpad=10)
            self.ax.set_ylabel("Profits $", fontsize=12, color='#ffffff', labelpad=15, rotation=90)

            # Enable grid lines for a professional look
            self.ax.grid(True, which='both', color='#CCCCCC', linestyle='--', linewidth=1)
            # Set the color of the X and Y ticks and labels
            self.ax.tick_params(axis='x', colors='#ffffff')  # Set X-axis tick color to white
            self.ax.tick_params(axis='y', colors='#ffffff') 
            # Adjust limits and gridlines based on time range
            self.ax.set_ylim(bottom=-1)
            self.ax.xaxis.set_major_formatter(DateFormatter("%b %d"))

            if selected_time_range == 1:
                self.ax.set_xticks([timestamps[0]])
                self.ax.set_xticklabels([timestamps[0].strftime("%b %d")])
            elif selected_time_range <= 7:
                self.ax.xaxis.set_major_locator(MaxNLocator(nbins=selected_time_range, prune=None))
            elif selected_time_range >= 30:
                self.ax.xaxis.set_major_locator(MaxNLocator(nbins=15, prune='both'))

            # Fix x-axis limits to prevent resizing when switching date ranges
            self.ax.set_xlim([timestamps[0], timestamps[-1]])

            # Adjust layout to reduce left padding and align the graph more professionally
            self.fig.subplots_adjust(left=0.065, right=0.95, top=0.90, bottom=0.12)

            # Add legend dynamically using 'best' location to avoid overlapping data
            self.ax.legend(loc="best", fontsize=8, frameon=False)

            plt.tight_layout()
            # Save the last used x and y limits
            self.last_xlim = self.ax.get_xlim()
            self.last_ylim = self.ax.get_ylim()

            # Force the canvas to update and reflect the changes
            self.canvas.draw()


    def start_model_data_refresh(self):
        self.model_data_thread = QThread()
        self.model_data_worker = ModelDataWorker(self.user_id)
        self.model_data_worker.moveToThread(self.model_data_thread)
        self.model_data_thread.started.connect(self.model_data_worker.refresh_model_data)
        self.model_data_worker.model_data_refreshed.connect(self.on_model_data_refreshed)
        self.model_data_thread.start()

    def on_model_data_refreshed(self, model_names):
        logging.info(f"Model names refreshed: {model_names}")
        self.model_data_thread.quit()
        self.model_data_thread.wait()
        self.model_data_worker.deleteLater()

    def link_account(self):
        displayname = self.ManageCreator.ui.DisplayNameLineEdit.text()
        email = self.ManageCreator.ui.LoginEmailLineEdit.text()
        passwd = self.ManageCreator.ui.PasswordLineEdit.text()
        self.browser_app = run_browser_app(displayname, email, passwd)
        self.browser_app.login_successful.connect(self.on_successful_login)

    def fetch_model_data(self):
        if not hasattr(self, 'data_fetcher') or not self.data_fetcher.isRunning():
            logging.warning("Cannot fetch data, either not logged in or fetcher not ready.")
            return
        self.data_fetcher = DataFetcher(user_id=1)
        self.data_fetcher.data_fetched.connect(self.on_data_fetched)
        self.data_fetcher.start()

    def on_initialize_finished(self):
        print("Database initialization finished.")

    def on_models_for_user_retrieved(self, models):
        print(f"Models retrieved: {models}")

    def on_cookies_for_model_retrieved(self, cookies):
        print(f"Cookies retrieved: {cookies}")

    def on_data_inserted_or_updated(self, success):
        print(f"Data inserted/updated: {success}")

    def closeEvent(self, event):
        logging.info("Closing the application, releasing resources...")

        # Stop and clean up any running threads
        if self.browser_thread and self.browser_thread.isRunning():
            self.browser_thread.quit()
            self.browser_thread.wait()

        # Clean up QWebEnginePage and QWebEngineProfile
        if self.browser_page:
            self.browser_page.deleteLater()
        if self.browser_profile:
            self.browser_profile.deleteLater()

        logging.info("QWebEnginePage and Profile cleaned up.")

        super().closeEvent(event)

    def on_successful_login(self):
            logging.info("Login successful. Starting data fetcher...")
            self.setup_data_fetcher()
            self.start_data_fetching()
            self.fetch_timer.start(15000)
            self.ClearLogin()

            self.load_creators_into_table()
            self.load_model_checkboxes()
            #close login browser here

            
    def show_dashboard(self):
        # If the FSHome page is active, close and clean up the profile
        if self.stacked_widget.currentWidget() == self.FSHome:
            logging.info("Navigating away from Fanservice. Releasing profile.")
            self.FSHome.close()  # Trigger the closeEvent in FSHomePage

        self.stacked_widget.setCurrentWidget(self.dashboard)

    def ManageCreatorsPage(self):
        self.stacked_widget.setCurrentWidget(self.ManageCreator)

    def TeamLayPage(self):
        self.stacked_widget.setCurrentWidget(self.TeamLayoutPage)

    def FanlinkkSettingsPage(self):
        self.stacked_widget.setCurrentWidget(self.FLSettings)

    def show_AnalyticsSide(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.AnalyticsSidebarPage)

    def show_CreatorSide(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.CreatorSidebarPage)

    def show_TeamSide(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.TeamSidebarPage)

    def show_FanSide(self):
        if hasattr(self, 'FSHome'):
            self.FSHome.close()
            self.stacked_widget.removeWidget(self.FSHome)
            self.FSHome.deleteLater()
            self.FSHome = None

        self.FSHome = FSHomePage()  
        self.stacked_widget.addWidget(self.FSHome)
        self.stacked_widget.setCurrentWidget(self.FSHome)


    # def show_EmptySidebar(self):
    #     self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.EmptySidebarPage)

    # def toggle_sidebar(self):
    #     if self.full_menu.isHidden():
    #         self.icon_menu.hide()
    #         self.full_menu.show()
    #     elif self.icon_menu.isHidden():
    #         self.full_menu.hide()
    #         self.icon_menu.show()

# Function to read the session file with retry logic
def verify_login_with_server(email, password):
    url = "http://127.0.0.1:8000/login/"  # Replace with your Django server URL
    payload = {'email': email, 'password': password}
    
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            return response.json()  # This will contain the token
        else:
            logging.error(f"Failed to log in: {response.text}")
            return None
    except requests.RequestException as e:
        logging.error(f"Error during login request: {e}")
        return None


def read_session_file(file_path, retries=3, delay=1):
    for i in range(retries):
        try:
            with open(file_path, 'r') as session_file:
                return json.load(session_file)
        except (PermissionError, IOError) as e:
            logging.warning(f"Error accessing session.json: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    return None  # Return None if the file can't be accessed after retries

db_utils.dbinitialize()

def main():
    logging.info("Starting application...")

    app = QApplication(sys.argv)
    logging.info("QApplication initialized.")

    # Load the styles
    styles_path = "resources/styles.qss"
    try:
        with open(styles_path, "r") as style_file:
            style_str = style_file.read()
        app.setStyleSheet(style_str)
        logging.info("Styles loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load styles: {e}")

    # Check if session file exists
    if os.path.exists('session.json'):
        logging.info("Session file found. Attempting auto-login.")
        session_data = read_session_file('session.json')  # Custom function to read session.json
        if session_data:
            active_user_email = session_data.get('email')
            access_token = session_data.get('access_token')
            refresh_token = session_data.get('refresh_token')
            logging.info(f"Attempting auto-login for user: {active_user_email}")

            # Validate access token
            if access_token and TokenUtils.validate_token(access_token):  # Token validation logic
                logging.info(f"Auto-login successful for user: {active_user_email}")
                main_window = MainWindow()  # No token passed here
                main_window.show()
                sys.exit(app.exec())  # Start the application event loop
            else:
                # Try refreshing the token if access token is invalid
                logging.warning("Access token expired or invalid. Attempting token refresh.")
                new_token = TokenUtils.refresh_access_token(refresh_token)  # Token refresh logic
                if new_token:
                    session_data['access_token'] = new_token
                    with open('session.json', 'w') as session_file:
                        json.dump(session_data, session_file)
                    logging.info("Token refreshed successfully. Logging in.")
                    main_window = MainWindow()  # No token passed here
                    main_window.show()
                    sys.exit(app.exec())
                else:
                    logging.error("Token refresh failed. Showing login dialog.")
        else:
            logging.error("Failed to read session.json. Showing login dialog.")
    else:
        logging.info("No session found. Showing login dialog.")

    # Show login dialog if no valid session or token
    login_dialog = LoginPage()
    if login_dialog.exec() == QDialog.Accepted:
        logging.info("Login successful. Showing main window.")
        access_token = login_dialog.get_token()  # Get the JWT token from LoginPage
        main_window = MainWindow()  # No token passed here
        main_window.show()

    logging.info("Starting application event loop.")
    sys.exit(app.exec())  # Start the application event loop
if __name__ == "__main__":
    main()