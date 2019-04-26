# Tim
A Twitter bot that posts from a list of messages stored in a text file

Tim is a simple Twitter bot written in Python and Bash. It reads from a text file with a list of messages in them, and line-by-line it posts each message on Twitter with a delay between each message. The delay is set as 1750 seconds (almost 30 minutes) as default, but that number can be altered to make it post faster or slower. 

Twitter will not allow a message to be posted more than once unless it's slightly different to what's been posted before, so each message will be posted with the day's date at the start of the tweet, that way Tim will be able to cycle through every message in that file time and time again.

### Requirements
* Bash or bash-compatible shell
* Python 2+
* Tweepy (To install: pip install tweepy)
* Twitter API tokens and keys

### Setup

* Add all files (main.sh, timbot.py & tweetlist.txt) into its own directory
* Add the path to that directory into the _WORKINGDIR=_ variable in _main.py_
* Add Twitter access tokens and consumer keys/secrets into the relevant fields within _timbot.py_ [Guide](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html)
* Add lines into _tweetlist.txt_ for Tim to post at 30 minute intervals
* Run _main.sh_ to execute Tim. To keep the session open, it's highly recommended you install and use [Screen](https://linux.die.net/man/1/screen) so you don't have to keep your Terminal open.
