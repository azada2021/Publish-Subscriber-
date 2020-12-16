import zmq

HOST = '127.0.0.1'
PORT = "2000"
p = 'tcp://' + HOST + ':' + PORT

context = zmq.Context()
s = context.socket(zmq.SUB)
s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, 'FOLDER')

while True:
    filename = s.recv()  # receiving file name
    print(filename)  #printing them
