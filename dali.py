import datetime,os,requests

from pytz import timezone
from glob import glob
from re import findall 

token = os.getenv('AGIT_TOKEN')

feedbackWeekday = int(os.getenv('FB_WEEKDAY'))
feedbackHour = int(os.getenv('FB_HOUR'))
feedbackMinute = int(os.getenv('FB_MINUTE'))

nowTime = datetime.datetime.now(timezone("Asia/Seoul"))
nowTime = datetime.datetime(nowTime.year,nowTime.month,nowTime.day,nowTime.hour,nowTime.minute,0)

feedbackTime = nowTime + datetime.timedelta(days = (feedbackWeekday+7-nowTime.weekday())%7) 
feedbackTime = datetime.datetime(feedbackTime.year,feedbackTime.month,feedbackTime.day,feedbackHour,feedbackMinute)
feedbackDelta = feedbackTime - nowTime

os.chdir("posts")
posts =  glob("*.md")
for post in posts:
    beforeDays,beforeHours = map(int,findall("\d+-\d",post)[0].split("-"))
    if beforeDays == feedbackDelta.days and feedbackDelta.seconds//3600 <= beforeHours:
        print("ok")
        with open(post,mode = "r",encoding="UTF-8") as postFile:
            postContent = {"text" : postFile.read()}
            requests.post("https://agit.io/webhook/"+token,postContent)
         



