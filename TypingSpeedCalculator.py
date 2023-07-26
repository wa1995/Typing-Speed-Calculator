# In this Speed Typing calculator, we calculate speed word per minute
# For this we need time module which will calculate time

from time import *          #This will import time module and we can use all functions of this module
import random as r


def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error                

def timespeed(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

test = ["My name is Waqas", "And I'm learning programming"]
test1 = r.choice(test)   #This will print random string
print("typing Speed")
print(test1)
print()
print()
time1 = time()
testinput = input(" Enter: ")
time2 = time()

print("speed", timespeed(time1,time2,testinput), "w/sec")
print("error", mistake(test1,testinput))