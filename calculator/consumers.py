import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Equation

class CalcConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            "history",
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            "history",
            self.channel_name
        )

    @database_sync_to_async
    def newEquation(self, string):
        # connection = psycopg2.connect(user="postgres",
        #                           password="postgres",
        #                           host="192.168.99.100",
        #                           port="5432",
        #                           database="postgres_db")

        # cursor = connection.cursor()
        # postgres_insert_query = """ INSERT INTO calculator_equation (equation_string) VALUES (%s)"""
        # record_to_insert = ("5 * 5 = 25")
        # cursor.execute(postgres_insert_query, record_to_insert)
        # connection.commit()
        Equation.objects.create(equation_string=string)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("Attempt to INSERT")
        await self.newEquation(message)
        # Send message to room group
        await self.channel_layer.group_send(
            "history",
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))