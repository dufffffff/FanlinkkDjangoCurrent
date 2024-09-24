# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.user_group_name = f"user_{self.user.id}"

        # Add this user to a group based on their ID
        await self.channel_layer.group_add(
            self.user_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.user_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # No need to handle received data, only pushing notifications to client
        pass

    async def send_notification(self, event):
        notification = event['notification']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'notification': notification
        }))