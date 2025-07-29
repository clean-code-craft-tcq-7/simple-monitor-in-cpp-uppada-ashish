import sys
from time import sleep

def flash_alert():
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)

def are_vitals_normal(temp, pulse, oxygen):
    if temp > 102 or temp < 95:
        print('Temperature is critical!')
        flash_alert()
        return False
    elif pulse < 60 or pulse > 100:
        print('Pulse rate is out of normal range!')
        flash_alert()
        return False
    elif oxygen < 90:
        print('Oxygen level is too low!')
        flash_alert()
        return False
    return True
