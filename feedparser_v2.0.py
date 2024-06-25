import feedparser
import csv
#import os
import requests

#CURDIR = "/opt/automate/NEWS"
#os.chdir(CURDIR)

#function for validating urls to avoid timeout for feedparser
def urltester(u):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    }
    try:
        #   print(f'Processing URL: {u}') # For testing only
        response = requests.get(u, headers=header, timeout=20)
        response.raise_for_status()
    except Exception:
        pass
    else:
        return u

# read url list for a file
urls=[]
with open('workingurls.txt','r') as f:
    for line in f:
        url=line.strip()
        if url:
            urls.append(url)


# create new csv file, write pared data
with open('news.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter = ',', quotechar='"')
    writer.writerow(["Source", "Title","Published time","Link"])
#write working urls to a txt file for using next time
    with open('workingurls.txt','w') as workingurls:
        for url in urls:
            urltester(url)
            try:
                feed = feedparser.parse(url)
                feed_title = feed.feed.title[:25]
                for entry in feed.entries[:10]:
                    writer.writerow([feed_title, entry.title, entry.published, entry.link])
#                print(url)    #for testing only
                workingurls.write(url+"\n")
            except Exception:
    #            print("Can not parse this link:",url)
                pass
