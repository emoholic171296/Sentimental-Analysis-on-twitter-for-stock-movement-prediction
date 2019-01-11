import tweepy
import csv
#You need to generate api keys by registering yourself for twitter developer's account
consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""
# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####Microsoft
# Open/Create a file to append data
csvFile = open('twitter_dataset9.csv','a',newline='\n')
#Use csv Writer
csvWriter = csv.writer(csvFile)
search_terms=('Microsoft OR #Microsoft OR #XboxOne OR #XboxGames OR #microsoftedge OR #microsoftsurface OR #microsoftoffice OR #Windows10 OR #Windows OR #bing OR #Cortana OR #Skype ')
csvWriter.writerow(['created_at','text'])
for status in tweepy.Cursor(api.search,q=search_terms,since='2018-12-12', until='2018-12-20',lang="en").items():
        print(status.created_at,status.text.encode('utf-8','ignore'))
        csvWriter.writerow([status.created_at, status.text.encode('utf-8','ignore')])

