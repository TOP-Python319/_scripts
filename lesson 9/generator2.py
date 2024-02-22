with open('/home/maks/Work/top-academy/python 319/.practice/lesson 8/2023-11-08T20_01_03_571Z-debug-0.log', 'r') as log_file:
    verbose_list = [st for st in log_file if 'verbose' in st]