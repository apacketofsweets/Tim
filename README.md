# Tim
A Twitter bot that posts from a list of messages stored in a text file

Tim is a simple Twitter bot written in Python and Bash. It reads from a text file with a list of messages in them, and line-by-line it posts each message on Twitter with a delay between each message. The delay is set as 1750 seconds (almost 30 minutes) as default, but that number can be altered to make it post faster or slower. 

Twitter will not allow a message to be posted more than once unless it's slightly different to what's been posted before, so each message will be posted with the day's date at the start of the tweet, that way Tim will be able to cycle through every message in that file time and time again.

## Wiki
* [Requirements](https://github.com/apacketofsweets/Tim/wiki/Requirements)
* [Setup](https://github.com/apacketofsweets/Tim/wiki/Setup)
