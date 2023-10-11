"""
Automatically shutdown running snakeviz instances after the browser opened
the flame chart.
"""

import os 
import sys
from time import sleep
from signal import SIGTERM


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise AssertionError('Please provide the process ID')
    try:
        pid = int(sys.argv[1])
    except ValueError:
        raise AssertionError(f'Invalid process ID "{sys.argv[1]}"')
    
    sleep(5)
    os.kill(pid, SIGTERM)