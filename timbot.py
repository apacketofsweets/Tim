from random  import randint
from time    import sleep
from tweepy  import OAuthHandler, API

infile = open('nexttweet.txt', 'r')
Facts = []
for line in infile:
    Facts.append(line.strip('\n'))
infile.close()

#Fill the below with hashtags seperated by commas if required
Hashtags = ['', ' ']

# Credentials to access Twitter API
ACCESS_TOKEN    = 'entertokenhere'
ACCESS_SECRET   = 'entersecrethere'
CONSUMER_KEY    = 'enterconsumekeyhere'
CONSUMER_SECRET = 'entersecretkeyhere'

# Initiate the connection to Twitter API
Auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
Auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
TwitterBot = API(Auth)

outfile = open('log.txt', 'a')
i = 0
while i < len(Facts):
        TwitterBot.update_status(Facts[i]+' '+Hashtags[randint(0,len(Hashtags)-1)]) # Tweet a fact as well as a random $
        outfile.write(str(i)+': '+Facts[i]+'\n') # Keep a log of tweeted facts in case server shuts off
        outfile.flush()
        i += 1
