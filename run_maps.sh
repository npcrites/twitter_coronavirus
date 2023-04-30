#!/bin/bash
for file in /data/Twitter\ dataset/geoTwitter20*; do
    nohup python3 ./src/map.py "--input_path=$file" &
    echo $file
done
