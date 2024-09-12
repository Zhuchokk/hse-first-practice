import time


load_str = '|                          |'
print('HSE first practice in work....')

while ' ' in load_str:
    load_str = load_str.replace(' ', '=', 1)
    time.sleep(0.1)
    print(load_str)
print('Completed!')
input()