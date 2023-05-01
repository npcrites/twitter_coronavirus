#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--hashtag',nargs='+',required=True)
args = parser.parse_args()
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import glob
# imports
import os
import json
from collections import Counter,defaultdict

parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True)
args = parser.parse_args()

# Hardcode the path to the outputs folder
inputs_folder = './outputs/'

# Find all files in the inputs folder
input_files = glob.glob(os.path.join(inputs_folder, "*"))
# Load each of the input paths
counts_per_day = defaultdict(lambda: Counter())
hashtags_input = args.hashtags[0]
hashtags = hashtags_input.split(",")
hashtags[0] = hashtags[0][1:]
hashtags[-1] = hashtags[-1][:-1]

print(input_files[0][20:28])

for file in input_files:
    date = file[20:28]
    print("date" + str(date))
    with open(file) as f:
        tmp = json.load(f)
            #print(tmp)
            #break
        for ht, daily_counts in tmp.items():
            if ht in hashtags:
                #print("firstcondiitoin")
                for day, count in daily_counts.items():
                    print("incrementing " + str(date) + " count for " + str(ht))
                    counts_per_day[ht][date] += count
# Make line plot
for hashtag, daily_counts in counts_per_day.items():
    days = sorted(daily_counts.keys())
    counts = [daily_counts[day] for day in days]
    plt.plot(days, counts, label=hashtag)

plt.xlabel('Day of the year')
plt.ylabel('Number of tweets')
plt.title('Number of tweets per hashtag per day')
plt.legend()
plt.savefig("tweets-per-day-for-" + '-'.join(args.hashtags) + ".png")
