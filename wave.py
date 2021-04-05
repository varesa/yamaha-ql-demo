import socket
import time
import math
import sys

channels = 8

offset = 32768
scale = (32768+1000)/2

def pos_to_val(x):
    return int(math.log10(x) * scale - offset)

if len(sys.argv) > 1:
    address = sys.argv[1]
else:
    address = '10.1.0.15'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((address, 49280))

x = 0

def send_cmd(s, cmd):
    print(cmd)
    s.send(cmd.encode() + b'\n')
    time.sleep(0.01)
    print(s.recv(2048))

while True:
    for i in range(channels):
        value_0_to_1 = (math.sin(x + 0.5 * i) + 1) / 2
        fader = pos_to_val(value_0_to_1 * 100)

        cmd = (f'set MIXER:Current/InCh/Fader/Level {i} 0 {fader}')
        send_cmd(s, cmd)

    x += 0.1
    #time.sleep(0.05)

