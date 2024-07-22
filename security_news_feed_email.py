#!/usr/bin/python3
import feedparser
import yagmail

url = ["http://thehackernews.com/feeds/posts/default",
       "https://www.bleepingcomputer.com/feed/",
       "http://feeds.feedburner.com/Securityweek",
       "https://www.freebuf.com/feed",
       "https://api.anquanke.com/data/v1/rss",
       "http://blog.nsfocus.net/feed",
       "https://www.4hou.com/feed"]

email_content = ""
addons = ""
for u in url:
    feed = feedparser.parse(u)
    feed_title = feed.feed.title[:21]
    email_content = (email_content + "\n"+ "="*10 + feed_title + "="*10 +"\n")
    n = 1
    for entry in feed.entries[:5]:

        addons = f"{n}. {entry.title}\n* Link:{entry.link}\n* Published Data:{entry.published}\n\n"
        email_content = email_content + addons
        n += 1


# print(email_content)

pass_01 = ""
#set gmail app password here
username =""
#set gmail account here, without @gmail.com

yag = yagmail.SMTP(username, pass_01)
contents = ['IT Security News Feed for Today:\n\n',email_content]
yag.send('zhangtingca@gmail.com', 'IT Security News for the Day', contents)
