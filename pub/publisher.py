import argparse
import zmq
import time
import numpy as np
import pandas as pd

def publisher(ip="0.0.0.0", port=5550):
    conn = "tcp://{}:{}".format(ip, port)
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect(conn)  
    imu = pd.read_csv("./imu.csv")
    imu_cols = ['time','acc_x','acc_y','acc_z','gyro_x', 'gyro_y', 'gyro_z']
    while True:
        idx = np.random.randint(0, imu.shape[0])
        time.sleep(1.0)
        message = imu[imu_cols].iloc[idx]
        socket.send_string(f"IMU {message}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",default=argparse.SUPPRESS)
    parser.add_argument("--port",default=argparse.SUPPRESS)
    args, _  = parser.parse_known_args()
    publisher(**vars(args))
