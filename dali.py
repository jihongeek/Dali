import datetime
from pytz import timezone
import os,requests

weekdays = [0,1,2,3,4,5,6]
nowTime = datetime.datetime.now(timezone("Asia/Seoul"))
nowTime = datetime.datetime(nowTime.year,nowTime.month,nowTime.day,nowTime.hour,nowTime.minute,0)

feedbackTime = nowTime + datetime.timedelta(days = weekdays[1-nowTime.weekday()]) 
feedbackTime = datetime.datetime(feedbackTime.year,feedbackTime.month,feedbackTime.day,15,47)

if feedbackTime == nowTime + datetime.timedelta(minutes=3):
    postFile = open("posts/feedback-0-0-3.md",mode = "r",encoding="UTF-8")
    post = {"text" : postFile.read()}
    requests.post("https://agit.io/webhook/"+token,post)






