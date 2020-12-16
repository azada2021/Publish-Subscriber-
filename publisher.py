import time
import zmq
import os

HOST = '127.0.0.1'
PORT = "2000"
p = 'tcp://' + HOST + ':' + PORT

context = zmq.Context()
s = context.socket(zmq.PUB)
s.bind(p)

inpt = input()  # taking input
os.chdir(inpt)

while True:
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            s.send_string("FOLDER " + inpt + " has " + os.path.join(root, name))
            time.sleep(4)  # Adding delay
        for name in dirs:
            s.send_string("FOLDER " + inpt + " has " + os.path.join(root, name))
            time.sleep(4)  # Adding delay
