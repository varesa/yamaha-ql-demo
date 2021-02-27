import socket
import time
import math

values = ["995","960","930","905","875","850","820","795","770","715","715","660","635","605","580","550","525","495","465","405","375","350","320","295","270","175","90","65","-30","-55","-170","-200","-290","-290","-365","-365","-450","-480","-580","-605","-660","-690","-715","-790","-820","-930","-955","-1080","-1140","-1340","-1390","-1610","-1670","-1770","-1810","-1870","-1920","-1970","-2020","-2140","-2200","-2410","-2410","-2610","-2670","-2830","-2890","-3050","-3110","-3330","-3390","-3680","-3730","-4040","-4140","-4720","-4720","-5160","-5280","-5620","-5700","-6100","-6100","-9400","-12000","-32768"]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.1.0.15',49280))

x = 0

def send_cmd(s, cmd):
    print(cmd)
    s.send(cmd.encode() + b'\n')
    time.sleep(0.01)
    print(s.recv(2048))

while True:
    a = (math.sin(x) + 1) / 2
    b = (math.sin(x + 0.5) + 1) / 2
    c = (math.sin(x + 1) + 1) / 2
    d = (math.sin(x + 1.5) + 1) / 2
    e = (math.sin(x + 2) + 1) / 2
    f = (math.sin(x + 2.5) + 1) / 2
    g = (math.sin(x + 3) + 1) / 2
    h = (math.sin(x + 3.5) + 1) / 2
    fader1 = values[round(a * 85)]
    fader2 = values[round(b * 85)]
    fader3 = values[round(c * 85)]
    fader4 = values[round(d * 85)]
    fader5 = values[round(e * 85)]
    fader6 = values[round(f * 85)]
    fader7 = values[round(g * 85)]
    fader8 = values[round(h * 85)]
    #fader = round(val_0_to_1 * -32768)

    cmd = (f'set MIXER:Current/InCh/Fader/Level 0 0 {fader1}')
    send_cmd(s, cmd)
    cmd = (f'set MIXER:Current/InCh/Fader/Level 1 0 {fader2}')
    send_cmd(s, cmd)
    cmd = (f'set MIXER:Current/InCh/Fader/Level 2 0 {fader3}')
    send_cmd(s, cmd)
    cmd = (f'set MIXER:Current/InCh/Fader/Level 3 0 {fader4}')
    send_cmd(s, cmd)
    cmd = (f'set MIXER:Current/InCh/Fader/Level 4 0 {fader5}')
    send_cmd(s, cmd)
    cmd = (f'set MIXER:Current/InCh/Fader/Level 5 0 {fader6}')
    send_cmd(s, cmd)
    cmd = (f'set MIXER:Current/InCh/Fader/Level 6 0 {fader7}')
    send_cmd(s, cmd)
    cmd = (f'set MIXER:Current/InCh/Fader/Level 7 0 {fader8}')
    send_cmd(s, cmd)

    x += 0.1
    #time.sleep(0.05)

