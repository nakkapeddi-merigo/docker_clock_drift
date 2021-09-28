# Script to normalize time samples
# Copyright 2021 Merigo
# 
# 
from locale import atof
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

BUF = []

def append_to_buf():
    with open('clock_sample.txt') as f:
        for line in f:
            filter_line(line)

def filter_line(ln):
    if 'reply' in ln:
        BUF.append(0) # negative means no adjustment needed
    elif 'adjusting local clock' in ln:
        sublist = ln.split(" ")[-1].rstrip()
        BUF.append(atof(sublist[:-1]))

def count_elements(seq) -> dict:
    """Tally elements from `seq`."""
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def main():
    append_to_buf()
    counts = count_elements(BUF)
    print(counts)

    plt.plot(*zip(*sorted(counts.items())))
    plt.xlim(0, 1)
    plt.show()

if __name__ == "__main__":
    main()