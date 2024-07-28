import asyncio
import websockets
import json
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand
from djangoapp.models import Alert 

ws_endpoint = "wss://stream.binance.com:9443/ws/btcusdt@ticker"

async def handle_messages():
    async with websockets.connect(ws_endpoint) as websocket:
        async for message in websocket:
            data = json.loads(message)
            current_price = float(data['c'])
            alerts = await sync_to_async(list)(Alert.objects.all())
            for alert in alerts:
                if alert.current<alert.target:
                    if current_price <= float(alert.target):
                        print(f"Alert Triggered for {alert.name} at {current_price} with mail id {alert.email}")
                        return  
                else:
                    if current_price >= float(alert.target):
                        print(f"Alert Triggered for {alert.name} at {current_price} with mail id {alert.email}")
                        return

class Command(BaseCommand):
    help = 'Starts the WebSocket client to listen for price alerts'

    def handle(self, *args, **options):
        asyncio.run(handle_messages())