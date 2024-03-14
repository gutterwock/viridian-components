import time
import board
from analogio import AnalogIn

input = AnalogIn(board.GP28)

while True:
    level = input.value * (3.3 / 65535)
    print(level)
    time.sleep(2.0)
