#-*- coding:utf-8 -*-
"""this is a test python file"""
from datetime import datetime
import random
import time

#命令行输入参数处理
ODDS = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35,
        37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in ODDS:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = random.randint(1, 5)
    time.sleep(wait_time)

print(abs(-100))
