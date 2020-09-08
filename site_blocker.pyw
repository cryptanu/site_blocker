import time
from datetime import datetime as dt

host_path = "hosts"
redirect_to = "127.0.0.1"
websites = []

while True:
    cur_yr = dt.now().year
    cur_mn = dt.now().month
    cur_dy = dt.now().day
    if dt(cur_yr, cur_mn, cur_dy, 8) < dt.now() < dt(cur_yr, cur_mn, cur_dy, 16):
        print('work time')
        with open(host_path, 'r+') as hp:
            content = hp.read()
            for website in websites:
                if website in content:
                    pass
                else: 
                    hp.write(redirect_to + ' ' + website + '\n')
    else:
        with open(host_path, 'r+') as hp:
            content = hp.readlines()
            hp.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    hp.write(line)
            hp.truncate()
        print('fun hours')
    time.sleep(5)