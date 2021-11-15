import matplotlib.pyplot as plt
from os import system
import time

FILE_NAME = 'registry.txt'
MA_LEN = 100

while True:
    data = []
    dct = {}
    system('clear')
    with open(FILE_NAME, 'r') as f:
        cnt = f.read()
        for i in range(len(cnt)):
            ch = cnt[i]
            if ch not in dct:
                dct[ch] = 0
            dct[ch] += 1

    print(f'Total registries: {len(data)}')

    for k in dct:
        v = dct[k]
        print('\'%s\' registries: %d (%.2f%%)' % (k, v, v / len(data) * 100))

    time.sleep(1)