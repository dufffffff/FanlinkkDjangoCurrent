import sys
import os
import logging
import json
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QDialog, QCheckBox, QSizePolicy, QSpacerItem
from PySide6.QtCore import QThread, QTimer, QDateTime, Signal, QObject, Slot, QSize, Qt, QUrl
from PySide6.QtGui import QPixmap, QPainter, QPainterPath

import pyqtgraph as pg
from collections import defaultdict

import db_utils, grab2
from sqlalchemy import select


from db_utils import DBWorker, Session, models
from login_test import run_browser_app
#from test_grab import DataFetcher
#from json_reader import JSONProcessor
from grab2 import DataFetcher

from MainView import MainViewer
from full_menu import FullMenu
from icon_menu import IconMenu
from top_bar import TopBar
import getnotifs
from DashboardPage import Dashboard

from EmployeeReportsPage import EmployeeReports
from ChatterAnalytics import ChatterAnalyticia
from FSHome import FSHomePage
from FSDiscover import FSDiscoverPage
from FSNotifications import FSNotificationsPage
from FSMessages import FSMessagesPage
from FSInsights import FSInsightsPage
from FSLists import FSListsPage
from FSVault import FSVaultPage
from FSSettings import FSSettingsPage
from FSNewPosts import FSNewPostsPage
from FSQueue import FSQueuePage
from FSProfile import FSProfilePagel
from FLSettings import FLSettingsPage
from RotaPage import Rota
from TeamLayoutPage import TeamLayout
from ManageCreatorsPage import ManageCreators
from creator_loader import load_creators
from db_utils import set_active_user, get_active_user, dbinitialize
import db_utils

from Login import LoginPage


dbinitialize()
# class GrapherWorker(QObject):
#     graph_updated = Signal(dict)
#     finished = Signal()

#     def __init__(self, directory):
#         super().__init__()
#         self.directory = directory

#     def run(self):
#         aggregated_data = self.load_and_aggregate_json_files(self.directory)
#         self.graph_updated.emit(aggregated_data)
#         self.finished.emit()

#     # def load_and_aggregate_json_files(self, directory):
#     #     aggregated_data = defaultdict(float)
#     #     for filename in os.listdir(directory):
#     #         if filename.endswith('response_1.json'):
#     #             filepath = os.path.join(directory, filename)
#     #             with open(filepath, 'r') as file:
#     #                 data = json.load(file)
#     #                 if 'result' in data and 'data' in data['result'] and 'json' in data['result']['data']:
#     #                     for period in data['result']['data']['json']['currentPeriod']:
#     #                         date = period['date'].split('T')[0]
#     #                         gross = period['gross']
#     #                         aggregated_data[date] += gross
#     #     return aggregated_data


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
                    print('cuntbuster')
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
        
        self.setWindowTitle("Dashboard Application")
        self.setGeometry(100, 100, 1200, 800)
        self.selected_models = []  # List of selected models
        self.selected_time_range = 7  # Default time range (last 7 days)

        self.model_data = {}  # Dictionary to store the last fetched data for each model # NEW ADDITION
        self.total_subs = 0  # Total subscriptions
        self.total_purchases = 0  # Total purchases
        self.total_tips = 0  # Total tips
        self.total_all = 0
        # self.total_metrics = {
        #     'tips': 0,
        #     'subs': 0,
        #     'ptv': 0,
        #     'renewals': 0,
        #     'messages': 0
        # }

        main_layout = QHBoxLayout()

        left_layout = QVBoxLayout()
        self.icon_menu = IconMenu()
        self.full_menu = FullMenu()
        left_layout.addWidget(self.icon_menu)
        left_layout.addWidget(self.full_menu)

        right_layout = QVBoxLayout()
        self.top_bar = TopBar()
        right_layout.addWidget(self.top_bar)

        self.stacked_widget = QStackedWidget()
        self.dashboard = Dashboard()
        self.stacked_widget.addWidget(self.dashboard)

        self.EmployeeReports = EmployeeReports()
        self.stacked_widget.addWidget(self.EmployeeReports)

        self.ChatterAnalytics = ChatterAnalyticia()
        self.stacked_widget.addWidget(self.ChatterAnalytics)



        self.FSDiscover = FSDiscoverPage()
        self.stacked_widget.addWidget(self.FSDiscover)

        self.FSNotifications = FSNotificationsPage()
        self.stacked_widget.addWidget(self.FSNotifications)

        self.FSInsights = FSInsightsPage()
        self.stacked_widget.addWidget(self.FSInsights)

        self.FSLists = FSListsPage()
        self.stacked_widget.addWidget(self.FSLists)

        self.FSVault = FSVaultPage()
        self.stacked_widget.addWidget(self.FSVault)

        self.FSQueue = FSQueuePage()
        self.stacked_widget.addWidget(self.FSQueue)

        self.FSNewPosts = FSNewPostsPage()
        self.stacked_widget.addWidget(self.FSNewPosts)

        self.FSSettings = FSSettingsPage()
        self.stacked_widget.addWidget(self.FSSettings)

        self.FSProfile = FSProfilePagel()
        self.stacked_widget.addWidget(self.FSProfile)

        self.TeamLayoutPage = TeamLayout()
        self.stacked_widget.addWidget(self.TeamLayoutPage)

        self.RotaControl = Rota()
        self.stacked_widget.addWidget(self.RotaControl)

        self.FLSettings = FLSettingsPage()
        self.stacked_widget.addWidget(self.FLSettings)

        self.ManageCreator = ManageCreators()
        self.stacked_widget.addWidget(self.ManageCreator)

        self.main_view = MainViewer()
        self.main_view.setCentralWidget(self.stacked_widget)
        right_layout.addWidget(self.main_view)

        main_layout.addLayout(left_layout, 0)
        main_layout.addLayout(right_layout, 9)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.icon_menu.hide()

        self.setup_connections()
        self.setup_db_worker()
        # self.start_json_processor()
        # self.start_grapher()
        self.load_creators_into_table()
        self.load_model_checkboxes()
    def update_fs_home_url(self, new_url):
        # This will load the new URL in the FSHomePage's browser
        self.FSHome.browser_window.setUrl(QUrl(new_url))





    def load_model_checkboxes(self):
        session = Session()
        try:
            query = select(models.c.name, models.c.image_path, models.c.email).order_by(models.c.name)
            result = session.execute(query).fetchall()
            
            # Enable and update checkboxes with the result
            self.update_dashboard_checkboxes(result)
            self.enable_checkboxes(None)
            
            logging.info("Model checkboxes updated and enabled successfully.")
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
            (self.dashboard.ui.MBox_two, self.dashboard.ui.Model_2Pic),
            (self.dashboard.ui.MBox_3, self.dashboard.ui.Model_3Pic),
            (self.dashboard.ui.MBox_4, self.dashboard.ui.Model_4Pic),
            (self.dashboard.ui.MBox_5, self.dashboard.ui.Model_5Pic),
            (self.dashboard.ui.MBox_6, self.dashboard.ui.Model_6Pic),
            (self.dashboard.ui.MBox_7, self.dashboard.ui.Model_7Pic),
            (self.dashboard.ui.MBox_8, self.dashboard.ui.Model_8Pic),
            (self.dashboard.ui.MBox_9, self.dashboard.ui.Model_9Pic),
            (self.dashboard.ui.MBox_10, self.dashboard.ui.Model_10Pic),
        ]

    def update_dashboard_checkboxes(self, result):
        placeholder_image_path = os.path.join(os.getcwd(), 'assets', 'placeholder.png')
        checkboxes = self.get_checkboxes()

        for i, (model_name, image_path, model_email) in enumerate(result):
            if i < len(checkboxes):
                checkbox, image_label = checkboxes[i]
                normalized_model_name = model_name.lower().replace(" ", "_").replace('_response', '')
                checkbox.setText(normalized_model_name.capitalize())
                checkbox.setProperty('model_email', model_email)
                checkbox.setVisible(True)
                checkbox.setEnabled(True)  # Enable checkbox

                #checkbox.toggled.connect(lambda checked, name=normalized_model_name: self.print_checkbox_state(name, checked))
                checkbox.toggled.connect(lambda checked, name=model_email: self.print_checkbox_state(name, checked))
                



                if image_path and os.path.exists(image_path):
                    self.set_rounded_image(image_label, image_path)
                else:
                    # Use placeholder image if no image path is available
                    self.set_rounded_image(image_label, placeholder_image_path)

                image_label.setVisible(True)
            else:
                checkbox.setVisible(False)
                image_label.setVisible(False)

        for i in range(len(result), len(checkboxes)):
            checkbox, image_label = checkboxes[i]
            checkbox.setVisible(False)
            image_label.setVisible(False)

        QApplication.processEvents()

    def set_rounded_image(self, image_label, image_path):
        image_label.setFixedSize(32, 32)

        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(image_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        mask = QPixmap(image_label.size())
        mask.fill(Qt.transparent)

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
                border: 2px solid #f2f2f2;
                background: transparent;
            }}
        """)

        image_label.repaint()
        QApplication.processEvents()

    # def print_checkbox_state(self, model_name, is_checked):
    #     logging.info(f"Checkbox for {model_name} toggled. Checked: {is_checked}")
    #     if is_checked:
    #         data = self.json_processor.get_metrics_for_model(model_name)
    #         if data:
    #             logging.info(f"Before addition - Total metrics: {self.total_metrics}")
    #             self.total_metrics['tips'] += data['tips']
    #             self.total_metrics['subs'] += data['subs']
    #             self.total_metrics['ptv'] += data['ptv']
    #             self.total_metrics['renewals'] += data['renewals']
    #             self.total_metrics['messages'] += data['messages']
    #             logging.info(f"Added data from {model_name}: {data}")
    #             logging.info(f"After addition - Total metrics: {self.total_metrics}")
    #             self.update_dashboard_with_notifications(self.total_metrics)
    #         else:
    #             logging.error(f"Data for {model_name} could not be retrieved or is empty.")
    #             print(f"Data for {model_name} could not be retrieved.")
    #     else:
    #         data = self.json_processor.get_metrics_for_model(model_name)
    #         if data:
    #             logging.info(f"Before subtraction - Total metrics: {self.total_metrics}")
    #             self.total_metrics['tips'] -= data['tips']
    #             self.total_metrics['subs'] -= data['subs']
    #             self.total_metrics['ptv'] -= data['ptv']
    #             self.total_metrics['renewals'] -= data['renewals']
    #             self.total_metrics['messages'] -= data['messages']
    #             logging.info(f"Subtracted data from {model_name}: {data}")
    #             logging.info(f"After subtraction - Total metrics: {self.total_metrics}")
    #             self.update_DashboardData(self.total_metrics)
    #         else:
    #             logging.error(f"Data for {model_name} could not be retrieved or is empty.")


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

    # def update_DashboardData(self, metrics=None):
    #     logging.info("Updating dashboard data...")
    #     if metrics is None:
    #         logging.warning("Metrics are None, initializing default values...")
    #         metrics = {
    #             'tips': 0,
    #             'subscriptions': 0,
    #             'ptv': 0,
    #             'renewals': 0,
    #             'messages': 0
    #         }

        

    #     total_tips_str = f"${getnotifs.get_sum_of_prices_from_last_days(7,11):,.2f}"
    #     total_subs_str = f"${getnotifs.get_sum_of_prices_from_last_days(7,10):,.2f}"
    #     total_ptv_str = f"${getnotifs.get_sum_of_prices_from_last_days(7,9):,.2f}"
    #     #total_renewals_str = f"${total_renewals:,.2f}"

    #     logging.info(f"Dashboard data: Tips: {total_tips_str}, Subs: {total_subs_str}, PTV: {total_ptv_str}")#, Renewals: {total_renewals_str}

    #     self.dashboard.ui.TipsDollarDash.setText(total_tips_str)
    #     self.dashboard.ui.SubscribersDollarDash.setText(total_subs_str)
    #     self.dashboard.ui.PostsDollarDash.setText(total_ptv_str)
    #     #self.dashboard.ui.MessagesDollarDash.setText(total_renewals_str)

    def setup_connections(self):
        self.icon_menu.ui.DAICON.clicked.connect(self.show_dashboard)
        self.icon_menu.ui.ANIcon.clicked.connect(self.show_AnalyticsSide)
        self.full_menu.ui.DAMain.clicked.connect(self.show_dashboard)
        self.full_menu.ui.ANMain.clicked.connect(self.show_AnalyticsSide)
        self.full_menu.ui.CEMain.clicked.connect(self.show_CreatorSide)
        self.full_menu.ui.TEMain.clicked.connect(self.show_TeamSide)
        self.full_menu.ui.FSMain.clicked.connect(self.show_FanSide)
        self.full_menu.ui.SEMain.clicked.connect(self.show_EmptySidebar)
        self.top_bar.ui.SidebarExpand.clicked.connect(self.toggle_sidebar)
        self.full_menu.ui.ERButton.clicked.connect(self.EmployeeReportsPage)
        self.full_menu.ui.ChatterAnalyticsButton.clicked.connect(self.ChatterAnalyticsPage)
        self.full_menu.ui.HomeButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/home"))
        self.full_menu.ui.DiscoverButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/discover"))
        self.full_menu.ui.InsightsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/insights"))
        self.full_menu.ui.NotificationsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/notifications/all"))
        self.full_menu.ui.NewPostsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/create"))

        #self.full_menu.ui.NotificationsButton.clicked.connect(self.FSNotificationsPage)
        #self.full_menu.ui.NewPostsButton.clicked.connect(self.FSNewPostsPage)
        self.full_menu.ui.ProfileButton.clicked.connect(lambda: self.update_fs_home_url("https://www.fanvue.com/profile"))
        self.full_menu.ui.QueueButton.clicked.connect(lambda: self.update_fs_home_url("https://www.fanvue.com/queue"))
        self.full_menu.ui.VaultButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/vault"))
        self.full_menu.ui.SensitiveWordsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/new-posts"))
        self.full_menu.ui.ManageCreatorsButton.clicked.connect(lambda: self.update_fs_home_url("https://fanvue.com/new-posts"))
        self.full_menu.ui.SEMain.clicked.connect(self.FanlinkkSettingsPage)
        self.full_menu.ui.RotaControlButton.clicked.connect(self.RotaPage)
        self.full_menu.ui.TeamLayoutButton.clicked.connect(self.TeamLayPage)
        self.ManageCreator.ui.LinkAccountButton.clicked.connect(self.link_account)
        self.ManageCreator.ui.LinkAccountButton.clicked.connect(self.fetch_model_data)
         # Connect time buttons to their respective handlers
        self.dashboard.ui.DateTodayButton.clicked.connect(lambda: self.handle_time_button_clicked(1))
        self.dashboard.ui.DateYesterdayButton.clicked.connect(lambda: self.handle_time_button_clicked(2))
        self.dashboard.ui.DateWeekButton.clicked.connect(lambda: self.handle_time_button_clicked(7))
        self.dashboard.ui.DateMonthButton.clicked.connect(lambda: self.handle_time_button_clicked(3000))
        for checkbox, _ in self.get_checkboxes():
            checkbox.toggled.connect(self.on_checkbox_toggled)

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
        # Get the name of the toggled checkbox
        checkbox = self.sender()
        model_email = checkbox.property('model_email')
        
        if checked:
            self.selected_models.append(model_email)
            print(f'anal {model_email}')
        else:
            self.selected_models.remove(model_email)
            

        # Fetch notifications when a checkbox is toggled
        self.fetch_notifications()
        
    def handle_time_button_clicked(self, days):
        # Update the selected time range and fetch notifications
        self.selected_time_range = days
        self.fetch_notifications()

    def fetch_notifications(self):
        if not self.selected_models:
            logging.info("No models selected. Resetting totals to zero.")
            self.total_subs = 0
            self.total_purchases = 0
            self.total_tips = 0
            self.total_all = 0
            self.update_dashboard_with_notifications()
            return

        # Recalculate the totals each time we fetch data
        self.total_subs = 0
        self.total_purchases = 0
        self.total_tips = 0

        for model in self.selected_models:
            # Fetch notifications for the current model
            subs = getnotifs.get_notifications_for_models_and_time(model, self.selected_time_range, event_type=10)
            purchases = getnotifs.get_notifications_for_models_and_time(model, self.selected_time_range, event_type=9)
            tips = getnotifs.get_notifications_for_models_and_time(model, self.selected_time_range, event_type=11)

            # Add new fetched data to the totals
            self.total_subs += subs
            self.total_purchases += purchases
            self.total_tips += tips

            # Store the current model's data for future use
            self.model_data[model] = (subs, purchases, tips)

            logging.info(f"Subscriptions (event_type=10) for {model}: {subs}")
            logging.info(f"Purchases (event_type=9) for {model}: {purchases}")
            logging.info(f"Tips (event_type=11) for {model}: {tips}")


        self.total_all = self.total_subs + self.total_purchases + self.total_tips

        # Update the dashboard UI with the accumulated totals
        self.update_dashboard_with_notifications()

            
    def update_dashboard_with_notifications(self):
        # Update the UI with the new totals
        logging.info(f"Total Subs = {self.total_subs:.2f}, Purchases = {self.total_purchases:.2f}, Tips = {self.total_tips:.2f}")
        logging.info(f"Total All = {self.total_all:.2f}")

        # Set text for dashboard, formatted to 2 decimal places
        self.dashboard.ui.TipsDollarDash.setText(f'${self.total_tips:.2f}')
        self.dashboard.ui.SubscribersDollarDash.setText(f'${self.total_subs:.2f}')
        self.dashboard.ui.PurchasesDollarDash.setText(f'${self.total_purchases:.2f}')

        # Update the "Total Dollar Dash"
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

        


    # def start_grapher(self):
    #     logging.info("Starting grapher...")

    #     if hasattr(self, 'grapher_thread') and self.grapher_thread.isRunning():
    #         logging.info("Waiting for previous grapher thread to finish...")
    #         self.grapher_thread.quit()
    #         self.grapher_thread.wait()

    #     self.grapher_thread = QThread()
    #     self.grapher_worker = GrapherWorker(directory=os.getcwd())
    #     self.grapher_worker.moveToThread(self.grapher_thread)
    #     self.grapher_worker.graph_updated.connect(self.update_graphs)
    #     self.grapher_worker.finished.connect(self.on_grapher_finished)
    #     self.grapher_thread.started.connect(self.grapher_worker.run)
    #     self.grapher_thread.start()

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

    def plot_cumulative_aggregated_data(self, aggregated_data, plot_widget):
        logging.info("Plotting cumulative aggregated data...")
        plot_widget.clear()

        dates = list(aggregated_data.keys())
        dates.sort()
        gross_values = [aggregated_data[date] / 100 for date in dates]

        cumulative_values = []
        cumulative_sum = 0
        for value in gross_values:
            cumulative_sum += value
            cumulative_values.append(cumulative_sum)

        date_objects = [QDateTime.fromString(date, "yyyy-MM-dd").toMSecsSinceEpoch() for date in dates]

        plot_widget.plot(date_objects, cumulative_values, pen=pg.mkPen(color='orange', width=2))

        plot_widget.getAxis('bottom').setTicks(
            [[(date, QDateTime.fromMSecsSinceEpoch(date).toString("yyyy-MM-dd")) for date in date_objects]])
        plot_widget.getAxis('left').setLabel('Gross Value', units='$')

        plot_widget.showGrid(x=True, y=True)
        QApplication.processEvents()

    # def on_grapher_finished(self):
    #     logging.info("Grapher finished processing.")

    # def update_graphs(self, aggregated_data):
    #     logging.info("Updating graphs on dashboard...")
    #     self.plot_cumulative_aggregated_data(aggregated_data, self.dashboard.ui.SalesGraphDashboard)
    #     QApplication.processEvents()


    def on_initialize_finished(self):
        print("Database initialization finished.")

    def on_models_for_user_retrieved(self, models):
        print(f"Models retrieved: {models}")

    def on_cookies_for_model_retrieved(self, cookies):
        print(f"Cookies retrieved: {cookies}")

    def on_data_inserted_or_updated(self, success):
        print(f"Data inserted/updated: {success}")

    def closeEvent(self, event):
        self.db_thread.quit()
        self.db_thread.wait()

        if hasattr(self, 'data_fetcher'):
            self.data_fetcher.quit()
            self.data_fetcher.wait()

        # if hasattr(self, 'grapher_thread'):
        #     self.grapher_thread.quit()
        #     self.grapher_thread.wait()
        # if hasattr(self, 'grapher_timer'):
        #     self.grapher_timer.stop()

        if hasattr(self, 'model_data_thread'):
            self.model_data_thread.quit()
            self.model_data_thread.wait()

        event.accept()

    def on_successful_login(self):
            logging.info("Login successful. Starting data fetcher...")
            self.setup_data_fetcher()
            self.start_data_fetching()
            self.fetch_timer.start(15000)
            self.ClearLogin()

            # Reload creators into the table after successful login
            self.load_creators_into_table()



    def show_dashboard(self):
        self.stacked_widget.setCurrentWidget(self.dashboard)
        self.show_EmptySidebar()

    def EmployeeReportsPage(self):
        self.stacked_widget.setCurrentWidget(self.EmployeeReports)

    def ChatterAnalyticsPage(self):
        self.stacked_widget.setCurrentWidget(self.ChatterAnalytics)

    def FSHomePage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def FSDiscoverPage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def FSNotificationsPage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def FSVaultPage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def FSQueuePage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def FSInsightsPage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def FSProfilePage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def FSNewPostsPage(self):
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def ManageCreatorsPage(self):
        self.stacked_widget.setCurrentWidget(self.ManageCreator)

    def FSFanvueSettingsPage(self):
        self.stacked_widget.setCurrentWidget(self.FSSettings)

    def TeamLayPage(self):
        self.stacked_widget.setCurrentWidget(self.TeamLayoutPage)

    def RotaPage(self):
        self.stacked_widget.setCurrentWidget(self.RotaControl)

    def FanlinkkSettingsPage(self):
        self.stacked_widget.setCurrentWidget(self.FLSettings)

    def show_AnalyticsSide(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.AnalyticsSidebarPage)

    def show_CreatorSide(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.CreatorSidebarPage)

    def show_TeamSide(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.TeamSidebarPage)

    def show_FanSide(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.FanserviceSidebarPage)
        self.stacked_widget.setCurrentWidget(self.FSHome)

    def show_EmptySidebar(self):
        self.full_menu.ui.ButtonPages.setCurrentWidget(self.full_menu.ui.EmptySidebarPage)

    def toggle_sidebar(self):
        if self.full_menu.isHidden():
            self.icon_menu.hide()
            self.full_menu.show()
        elif self.icon_menu.isHidden():
            self.full_menu.hide()
            self.icon_menu.show()

def main():
    db_utils.dbinitialize()  # Ensure database is initialized before login

    # Create application instance
    app = QApplication(sys.argv)

    # Load the styles (optional, depends on your use case)
    with open("styles.qss", "r") as style_file:
        style_str = style_file.read()
    app.setStyleSheet(style_str)

    # Create and show login dialog
    login_dialog = LoginPage()  # LoginPage is the class for the login screen
    if login_dialog.exec() == QDialog.Accepted:
        # If login is successful, show the main window
        main_window = MainWindow()
        main_window.show()

        # Execute the application
        sys.exit(app.exec())

if __name__ == "__main__":
    main()