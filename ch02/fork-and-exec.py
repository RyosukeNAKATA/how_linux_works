#!/usr/bin/python3
import os
import sys
ret = os.fork()
if ret == 0:
    print("Child Process: pid{}, Parent Process pid={}".format(os.getpid(), os.getppid()))
    os.execve("/bin/echo", ["echo", "Hello from pid={}".format(os.getpid())], {})
    exit()
elif ret > 0:
    print("Parent Process: pid{}, Child Process pid={}".format(os.getpid(), ret))
    exit()
sys.exit(1)

