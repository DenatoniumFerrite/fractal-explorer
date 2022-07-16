import time
import os

def clock_start():
    global begin_time
    begin_time = time.time()

def clock_end():
    print("\nCompleted in " + str(round(time.time()-begin_time, ndigits=4)) + " seconds")

def progress_percent(current_work, total_work):
    print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b", end="")
    print(str(round(current_work/total_work*100, ndigits=1))+"% complete", end="")
