#!/usr/bin/env python3
import sys

#Author: Tsz Him Ko
#Author ID: thko1
#Date Created: 2025/05/22
if len(sys.argv)==2:
    timer=int(sys.argv[1])
else:
    timer=3    

while timer!=0:
    print(timer)
    timer -= 1

print("blast off!")
