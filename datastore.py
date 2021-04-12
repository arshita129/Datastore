import time
import threading

d={}

#CRD operations

def create(key,value,time_to_live=0):
    if not key.isalpha():
        print("Error: Invalid key name")
        return
    if key in d:
        print("KeyError: this key already exists")
        return
    if len(d)>(1024*1024*1024):
        print("MemoryError: File size exceeded")
        return
    if int(value)>(16*1024*1024):
        print("ValueError: Value size exceeded")
        return
    if len(key)>32:
        print("KeyError: Key size exceeded")
        return
    if time_to_live==0:
        d[key]=[value,time_to_live]
    else:
        d[key]=[value,time_to_live+time.time()]


def read(key):
    if key not in d:
        print("KeyError: Key not found")
        return
    if d[key][1]==0:
        return '{} : {}'.format(key,d[key][0])
    else:
        if d[key][1]>=time.time():
            print("Error: This key has expired")
        else:
            return '{} : {}'.format(key,d[key][0])

def delete(key):
    if key not in d:
        print("KeyError: Key not found")
        return
    if d[key][1]==0:
        del d[key]
    else:
        if d[key][1]>=time.time():
            print("Error: This key has expired")
        else:
            del d[key]