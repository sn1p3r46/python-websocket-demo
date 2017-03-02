#!/usr/bin/python3

import asyncio
import websockets

voc = {

    'name?' : "Andrea Galloni",
    'email?' : 'JustAnAddress@gmail.com',
    'gender?' : 'M'

}

async def myclient():
    try:
        async with websockets.connect('ws://localhost:8765') as websocket:
            while (True):

                try:
                    question = await websocket.recv()
                    print ("Received: " + question)
                    print ("Answering with: " + voc[question])
                    await websocket.send(voc[question]) 

                except websockets.exceptions.ConnectionClosed :
                    print ("Connection Closed by the Server!")
                    break

                except KeyError :
                    print ("Malformed request: " + question)
                    break

    except ConnectionRefusedError :
        print ("Connection Refused!")

asyncio.get_event_loop().run_until_complete(myclient())
