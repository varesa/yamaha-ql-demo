import socket
import time
import math

"""
NOTIFY set MIXER:Current/InCh/Fader/On 0 0 1 "ON"
NOTIFY set MIXER:Current/InCh/Fader/On 0 0 0 "OFF"
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.0.15',49280))

x = 0

def send_cmd(s, cmd):
    print(cmd)
    s.send(cmd.encode() + b'\n')
    time.sleep(0.01)
    print(s.recv(2048))

while True:
    for bit in range(8):
        value = x & (1 << bit)
        if value:
            send_cmd(s, f"set MIXER:Current/InCh/Fader/On {bit} 0 1")
        else:
            send_cmd(s, f"set MIXER:Current/InCh/Fader/On {bit} 0 0")

    x += 1
    time.sleep(1)

