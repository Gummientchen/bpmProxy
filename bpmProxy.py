import os
import asyncio
import functools
import websockets
import socket
import json
import csv
from datetime import datetime
from http import HTTPStatus

MIME_TYPES = {
  "html": "text/html",
  "js": "text/javascript",
  "css": "text/css",
  "svg": "image/svg+xml",
}

UDP_IP = "127.0.0.1"
UDP_PORT = 60900

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

globalBpm = ""

## Serves static index.html file
async def process_request(sever_root, path, request_headers):
  """Serves a file when doing a GET request with a valid path."""

  if "Upgrade" in request_headers:
    return  # Probably a WebSocket connection

  if path == '/':
    path = '/index.html'

  response_headers = [
    ('Server', 'asyncio websocket server'),
    ('Connection', 'close'),
  ]

  # Derive full system path
  full_path = os.path.realpath(os.path.join(sever_root, path[1:]))

  # Validate the path
  if os.path.commonpath((sever_root, full_path)) != sever_root or \
      not os.path.exists(full_path) or not os.path.isfile(full_path):
    print("HTTP GET {} 404 NOT FOUND".format(path))
    return HTTPStatus.NOT_FOUND, [], b'404 NOT FOUND'

  # Guess file content type
  extension = full_path.split(".")[-1]
  mime_type = MIME_TYPES.get(extension, "application/octet-stream")
  response_headers.append(('Content-Type', mime_type))

  # Read the whole file into memory and send it out
  body = open(full_path, 'rb').read()
  response_headers.append(('Content-Length', str(len(body))))
  print("HTTP GET {} 200 OK".format(path))
  return HTTPStatus.OK, response_headers, body

## listens for new messages on UDP
def udpReceive(loop):
  data, addr = sock.recvfrom(128) # buffer size is 1024 bytes
  global globalBpm
  globalBpm = data.decode("utf-8")
  
  loop.call_later(0.1, udpReceive, loop)

## handle websocket connection
async def wsBpm(websocket, path):
  print("New WebSocket connection from", websocket.remote_address)
  while websocket.open:
    dt = datetime.now()
    ts = datetime.timestamp(dt)
    ms = round(ts*1000)

    r = ""
    for row in csv.reader([globalBpm.strip()]):
      r = row

    jsonResponse = json.dumps({
      'ms': ms,
      'bpm': r[1],
      'ibi': r[4]
      })

    await websocket.send(jsonResponse)
    # await websocket.send(str(ms)+","+globalBpm.strip())
    await asyncio.sleep(0.1)
  # This print will not run when abrnomal websocket close happens
  # for example when tcp connection dies and no websocket close frame is sent
  print("WebSocket connection closed for", websocket.remote_address)

if __name__ == "__main__":
  # set first argument for the handler to current working directory
  handler = functools.partial(process_request, os.getcwd())
  start_server = websockets.serve(wsBpm, '127.0.0.1', 8765, process_request=handler)
  print("Running server at http://127.0.0.1:8765/")

  # start udp client
  loop = asyncio.get_event_loop()
  loop.call_soon(udpReceive, loop)

  # start websocket server
  asyncio.get_event_loop().run_until_complete(start_server)
  asyncio.get_event_loop().run_forever()

