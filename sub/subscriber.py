# BSD 3-Clause License
# Stef van der Struijk

import argparse
import zmq


def subscriber(ip="0.0.0.0", port=5550):
    conn = "tcp://{}:{}".format(ip, port)
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.bind(conn)  
    socket.setsockopt_string(zmq.SUBSCRIBE,"IMU") 

    while True:
        msg = socket.recv_string()
        print(f"received data: {msg}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",default=argparse.SUPPRESS)
    parser.add_argument("--port",default=argparse.SUPPRESS)
    args, _ = parser.parse_known_args()
    subscriber(**vars(args))
