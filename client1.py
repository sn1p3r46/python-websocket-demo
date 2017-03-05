#!/usr/bin/python3

import asyncio
import websockets

end_point='ws://service.recommendersystem.com/recsys2-course/engine'

voc = {

    'Author name' : "Andrea Galloni",
    'Author email' : 'andreagalloni[92][at]gmail[dot]com',
    'Author id' : 'JGNBMW'

}

async def myclient():
    try:
        async with websockets.connect(end_point) as websocket:
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
