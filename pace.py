#!/usr/bin/python

import sys

distances = { "1k" : 1.0,
              "1m" : 1.60934,
              "5k" : 5.0,
              "10k": 10.0,
              "h": 21.0975,
              "m": 42.195,
              "50m" : 80.4672 }

def usage():
    print("usage:")
    sys.exit(1)

def kmph(mps):
    return (mps * (3600.0/1000.0))

def time(secs):
    h = int(secs / 3600)
    secs = secs - (h * 3600)
    m = int(secs / 60)
    secs = secs - (m * 60)
    return "%.2d:%.2d:%.2d" %(h,m,secs)

if __name__ == "__main__":

    try:
        distance = distances[sys.argv[1]]
        t = sys.argv[2].split(":")
        if len(t) == 2:
            s = float(t[0])*60 + float(t[1])
            speed = 1000.0/s
            seconds = distance * 1000.0 / speed
            pace = "%.2d:%.2d" %(int(t[0]),int(t[1]))
        elif len(t) == 3:
            seconds = float(t[0]) * 3600 + float(t[1]) * 60 + float(t[2])
            speed = distance * 1000.0 / seconds
            spk = 1000.0/speed
            m = int(spk) / 60
            s = int(spk) % 60
            pace = "%.2d:%.2d" %(m,s)
            pass
    except KeyError:
        usage()

    print("distance: %.3f km" %distance)
    print("speed:    %.2f km/h" %kmph(speed))
    print("pace:     %s /km" %pace)
    print("time:     %s" %time(seconds))