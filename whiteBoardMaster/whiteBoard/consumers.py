# board/consumers.py
import json
from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer

class WhiteBoardConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        self.room_name = 'whiteboard'
        self.room_group_name = 'whiteboard_group'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_disconnect(self, event):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        raise StopConsumer()

    async def websocket_receive(self, event):
        data = json.loads(event['text'])
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'whiteboard.message',
                'message': data
            }
        )

    async def whiteboard_message(self, event):
        message = event.get('message', {})  # Use .get() to avoid KeyError
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(message)
        })
