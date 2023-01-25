#!/usr/bin/python3
import os
import sys
ret = os.fork()
if ret == 0:
    print("Child Proccess: pid{}, Parent Proccess pid={}".format(os.getpid(), os.getppid()))
    exit()
elif ret > 0:
    print("Parent Proccess: pid{}, Child Proccess pid={}".format(os.getpid(), ret))
    exit()
sys.exit()

