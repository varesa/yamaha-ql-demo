import libql

N_CHANNELS = 4

ql = libql.QL('10.1.0.15')
#state = ql.get_on_state(0)
#ql.set_on_state(0, 1-state)

channels = [0] * N_CHANNELS

while True:
    input()
    for i in range(N_CHANNELS):
        channels[i] = ql.get_on_state(i)
        ql.set_on_state(i, 0)

    print(channels)
        
    input()
    for i in range(N_CHANNELS):
        ql.set_on_state(i, channels[i])

    print(channels)
