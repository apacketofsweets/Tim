#!/bin/bash

WORKINGDIR=/path/to/working/dir/

exec 3<$WORKINGDIR/tweetlist.txt

while read -r line
  do
        echo "$(date +%Y-%m-%d):" $line > $WORKINGDIR/nexttweet.txt
        python $WORKINGDIR/timbot.py
        
        # Waits 30 minutes (1750 seconds) before posting again - amend this number as you see fit
        sleep 1750 
done <&3

rm $WORKINGDIR/log.txt
