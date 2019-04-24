#!/bin/bash

WORKINGDIR=/path/to/working/dir/

exec 3<$WORKINGDIR/TweetList.txt

while read -r line
  do
        echo "$(date +%Y-%m-%d):" $line > $WORKINGDIR/NextTweet.txt
        python $WORKINGDIR/twitterbot.py
        sleep 1750
done <&3

rm $WORKINGDIR/Log.txt
