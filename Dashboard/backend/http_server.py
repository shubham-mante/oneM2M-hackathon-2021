#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import subprocess
import json
import asyncio
import websockets
import time
import csv

async def produce(message: str, host: str, port: int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        x = json.loads(post_data.decode('utf-8'))
        a = x["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]['lt']
        b = x["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]['PM10']
        c = x["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]['PM25']
        d = x["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]['CO2']
        e = x["m2m:sgn"]["m2m:nev"]["m2m:rep"]["m2m:fcnt"]['Temp']
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        check_head = False
        data_file=open('DATA.csv','r')
        datareader = csv.reader(data_file, delimiter=',')
        for i in datareader:
            check_head = True
            break
        data_file=open('DATA.csv','a')
        keys = ["Time","PM10","PM25","CO2","Temp"]
        out_csv=csv.writer(data_file)
        if not check_head:
            out_csv.writerow(keys)
        arr=[a,b,c,d,e]
        # print(arr)
        out_csv.writerow(arr)
        data_file.close()
        msg = json.dumps({'Time': a, 'PM10': b, 'PM25': c, 'CO2': d, 'Temp': e})
        asyncio.run(produce(message=msg, host='localhost', port=4000))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=1400):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
