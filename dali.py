import datetime
from pytz import timezone
from glob import glob
import os,requests

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
post =f"feedback-{feedbackDelta.days}-{feedbackDelta.seconds//3600}-{(feedbackDelta.seconds%3600)//60}.md" 
if post in posts:
    print("ok")
    with open(post,mode = "r",encoding="UTF-8") as postFile:
        postContent = {"text" : postFile.read()}
        requests.post("https://agit.io/webhook/"+token,postContent)




