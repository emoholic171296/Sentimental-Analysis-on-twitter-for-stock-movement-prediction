import csv
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
'''emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""'''
def remove_digits(tweet):
	example=list(word_tokenize(tweet))
	l=""
	for w in example:
		if not w.isdigit():
			l=l+w
			l=l+" "
	return l
def clean_tweet( tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        tweet = tweet.lower() 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
def stopword_removal(tweet):
	example_words=list(word_tokenize(tweet))
	stop_words = list(stopwords.words('english'))
	k=""
	for w in example_words:
		if w not in stop_words:
			k=k+w
			k=k+" "
	return k
def extra(tweet):
	example=list(word_tokenize(tweet))
	k=""
	l=""
	for w in example:
		if "b"!=str(w):
			k=k+w
			k=k+" "
	example1=list(word_tokenize(k))
	for w in example1:
		if "rt"!=str(w):
			l=l+w
			l=l+" "
	return l
def remove_images(tweet):
        example=list(word_tokenize(tweet))
        k=""
        for w in example:
                if re.search(r'[\\x90-\\xff]',w):
                        continue
                else:
                        k=k+w
                        k=k+" "
        return k
csvfile = open('twitter_dataset9.csv','r',newline='\n')
csvfile1= open('twitter_dataset17.csv','a',newline='\n')
csvWriter = csv.writer(csvfile1)
csvFileArray = []
counter=0
i=0
csvWriter.writerow(['text','polarity'])
for row in csv.reader(csvfile, delimiter = ','):
        if counter==0:
                counter+=1
                continue
        else:
                csvFileArray.append(row)
                ls=clean_tweet(csvFileArray[i][1])
                w=stopword_removal(ls)
                h=remove_digits(w)
                f=extra(h)
                g=remove_images(f)
                i=i+1
                counter+=1
                csvWriter.writerow([g,])




