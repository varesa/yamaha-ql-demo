import socket
import time
import re


class QL:
    socket = None
    
    def __init__(self, ip, port=49280):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def _cmd(self, cmd):
        #print(cmd)
        self.socket.send(cmd.encode() + b'\n')

    def _read(self):
        time.sleep(0.01)
        return self.socket.recv(10000).decode().split('\n')

    def get_on_state(self, channel: int) -> int:
        self._cmd(f'get MIXER:Current/InCh/Fader/On {channel} 0')
        state = None
        lines = self._read()
        for line in lines:
            if match := re.match(f'OK get MIXER:Current/InCh/Fader/On {channel} 0 ([0-1])', line):
                # Do not return early to make use the latest information if socket buffer has old unconsumed data
                state = int(match.group(1))
        assert state is not None, f"Failed to read ON state for channel {channel}. Output: {lines}"
        return state

    def set_on_state(self, channel: int, state: int):
        self._cmd(f'set MIXER:Current/InCh/Fader/On {channel} 0 {state}')
        lines = self._read()
        for line in lines:
            if match := re.match(f'OK set MIXER:Current/InCh/Fader/On {channel} 0 {state}', line):
                break
        else:
            assert False, f"Did not get OK for setting ON state for channel {channel}. Output: {lines}"

    def get_fader(self, channel: int) -> int:
        self._cmd(f'get MIXER:Current/InCh/Fader/Level {channel} 0')
        state = None
        lines = self._read()
        for line in lines:
            if match := re.match(f'OK get MIXER:Current/InCh/Fader/Level {channel} 0 ([0-9-]+)', line):
                # Do not return early to make use the latest information if socket buffer has old unconsumed data
                state = int(match.group(1))
        assert state is not None, f"Failed to read fader for channel {channel}. Output: {lines}"
        return state

    def set_fader(self, channel: int, state: int):
        self._cmd(f'set MIXER:Current/InCh/Fader/Level {channel} 0 {state}')
        lines = self._read()
        for line in lines:
            if match := re.match(f'OK set MIXER:Current/InCh/Fader/Level {channel} 0 {state}', line):
                break
        else:
            assert False, f"Did not get OK for setting fader for channel {channel}. Output: {lines}"
