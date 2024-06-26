import time
import datetime
import random
import string

random_str = ''.join(random.choice(string.ascii_lowercase) for i in range(10))

while True:
    print(f'{datetime.datetime.now()}: {random_str}')
    time.sleep(5)
