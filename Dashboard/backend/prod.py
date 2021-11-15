import asyncio
import websockets
import time
import json

async def produce(message: str, host: str, port: int) -> None:
	async with websockets.connect(f"ws://{host}:{port}") as ws:
		await ws.send(message)
		await ws.recv()


# a,b,c,d = input().split()
if __name__ == '__main__':
	a = 0
	b=0
	for i in range(10):
		a+=1
		b+=10
		msg = json.dumps({'Time': a, 'PM10': b, 'PM25': a, 'CO2': a,'Temp':b})
		asyncio.run(produce(message=msg, host='localhost', port=4000))
