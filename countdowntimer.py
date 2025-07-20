# Countdown Timer Script

import time

# Countdown from 10 to 0
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)  # Pause for 1 second

print("Countdown finished!")
