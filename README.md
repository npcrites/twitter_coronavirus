About 1% are geotagged. Accessing files with tweets (and their geotags) from each individual day in 2020, we accessed nearly 1.1 billion tweets.

## Project Overview
In this project, I used MapReduce teechniques to combine a years worth of tweets into a single file. When condensing the files, we aggregated a year's worth of language and country data of Covid-19 related hashtags from multiple countries from each hour of the day. Below are the hashtags used:

```
hashtags = [
    '#코로나바이러스',  # korean
    '#コロナウイルス',  # japanese
    '#冠状病毒',        # chinese
    '#covid2019',
    '#covid-2019',
    '#covid19',
    '#covid-19',
    '#coronavirus',
    '#corona',
    '#virus',
    '#flu',
    '#sick',
    '#cough',
    '#sneeze',
    '#hospital',
    '#nurse',
    '#doctor',
    ]
```

## MapReduce
In MapReduce procedure, I first utilized a mapping file map.py. This script is designed to parse all of the tweets in an input zip file from every hour of the day and save each day's file to the output file. Using the run_maps.sh shell script to run 366 days worth of tweets in parallel, I was able to apply the map.py file on all 366 zip fifles from 2020. Next, I used reduce.py compile all the languages and countries attached to the geotag in the file, and store two output files (`reduced.lang` and `reduced.country`) in a seperate folder. After this, I applied the `visualize.py` file to the reduced files to generate outputs for the number of times `#코로나바이러스` and `#coronavirus` were tweeted about in different languages and different countries. Finally, I created `alternative_reduce.py` - a file that essentailly combined `reduce.py` and `visualize.py`, but that takes a list of hashtags as an input and outputs a line plot. The line plot output  where a) there is one line per input hashtag, b) the x-axis is the day of the year, and c) the y-axis is the number of tweets that use that hashtag during the year. For an input list of hashtags, I passed in `#covid19`, `#sick`, and `#flu`. 

## Results
The results are the `#coronavirus_reduced.country.png`, `#coronavirus_reduced.lang.png`, `#코로나바이러스_reduced.country.png`, and `#코로나바이러스_reduced.lang.png` files, which compare the number of `#coronavirus` and `#코로나바이러스` related tweets between languages and countries. In addition, I produced a `tweets-per-day-for-[#covid19,#sick,#flu].png` - the output of `alternative_reduce.py`. 
