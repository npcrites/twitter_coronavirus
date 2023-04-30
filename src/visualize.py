#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]
print("here")
# print the count values
#items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
items = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=True)[:10]

print(len(items))
labels = [k for k, v in items]
values = [v for k, v in items]
print(labels)
print(values)
plt.bar(labels, values)
plt.title(args.key + " + " + args.input_path)
plt.ylabel('Count')
if args.percent:
    plt.ylabel('Percentage')
print("1")
plt.xticks(range(len(labels)), labels, fontsize='small', rotation=45)

# fig, ax = plt.subplots()
# ... add your plot elements ...

# save the plot to a file
plt.savefig(args.key + "_" + args.input_path + ".png")
# for k,v in items:
    # print(k,':',v)
