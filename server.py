#!/usr/bin/python3

import asyncio
import websockets

questions = ['name?','email?','gender?']

async def handler(websocket,path):
    try:
        for q in questions:
            await websocket.send(q)
            data = await websocket.recv()
            print (q[:-1]+": " + data)

    except websockets.exceptions.ConnectionClosed :
        print( "Connection Unexpectedly Closed by the Client" )


start_server = websockets.serve(handler, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

