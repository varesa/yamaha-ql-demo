import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.0.15',49280))

while True:
    s.send(b'set MIXER:Current/InCh/Fader/On 0 0 1 "ON"\n')
    time.sleep(1)
    s.send(b'set MIXER:Current/InCh/Fader/On 0 0 0 "OFF"\n')
    time.sleep(1)

