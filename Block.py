# pass in urls
# determine whether urls have already been passed in
# set date&time variables

from datetime import datetime as dt
import time


url_block = "hosts"
redirect_to = "127.0.0.1"
urls = ["www.gamegape.org", "gamegape.org", "poptropica.com", "www.poptropica.com"]

cur_yr = dt.now().year
cur_mn = dt.now().month
cur_dy = dt.now().day

while True:
    with open(url_block, 'r+') as file:
        if dt(cur_yr, cur_mn, cur_dy, 5) < dt.now() < dt(cur_yr, cur_mn, cur_dy, 16):
            content = file.read()
            for url in urls:
                if url in content:
                    pass
                else:
                    file.write(redirect_to + ' ' + url + '\n')
            print('work work work')
        else:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(url in line for url in urls):
                    file.write(line)
                file.truncate()
            print('party time')
        time.sleep(5)
    pass

