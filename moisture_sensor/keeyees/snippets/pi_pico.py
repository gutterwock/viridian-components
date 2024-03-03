import time
import board
from analogio import AnalogIn

output = AnalogIn(board.GP28)

# no water contact, full water contact is ~33000
zero = 65535

while True:
    level =  output.value / zero
    print(level)
    time.sleep(2.0)