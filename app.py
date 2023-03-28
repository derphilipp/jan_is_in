#!/usr/bin/env python
# encoding: utf-8

from flask import Flask
from gevent.pywsgi import WSGIServer

FILENAME = "/status/status.txt"
FILENAME_IN = "/html/in.html"
FILENAME_OUT = "/html/out.html"
FILENAME_ERR = "/html/err.html"


app = Flask(__name__)


def read_status():
    f = open(FILENAME, "r")
    data = f.read()
    f.close()
    return data


def write_status(status):
    f = open(FILENAME, "w")
    f.write(status)
    f.close()


@app.route("/", methods=["GET"])
def query_records():
    status = read_status()

    if status == "in":
        f = open(FILENAME_IN, "r")
        data = f.read()
        return data
    if status == "out":
        f = open(FILENAME_OUT, "r")
        data = f.read()
        return data
    f = open(FILENAME_ERR, "r")
    data = f.read()
    return data


@app.route("/in", methods=["GET"])
def write_in():
    write_status("in")
    return "OK"


@app.route("/out", methods=["GET"])
def write_out():
    write_status("out")
    return "OK"


if __name__ == "__main__":
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
