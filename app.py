from flask import Flask,request,render_template
import requests
import json

import prediction

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('news.html')

@app.route('/pred',methods = ['POST','GET'])
def login():
    # if request.method=="POST" or request.method=="GET":
    news = request.form["news1"]
    news1 = request.form["news2"]
    news_predict = prediction.detecting_fake_news(news1)
    # print(news_predict)
    url = "https://newsapi.org/v2/everything?q=" + news + "&from=2021-10-05&to=2021-10-05&sortBy=popularity&language=en&apiKey=c2fa4ac945b044d2838257fa92306e74"
    response = requests.get(url)
    val = response.json()
    val1 = json.dumps(val)
    loadval = json.loads(val1)
    r = loadval["articles"][0]["title"]
    r1 = loadval["articles"][1]["title"]
    r2 = loadval["articles"][2]["title"]
    l1 = loadval["articles"][0]["url"]
    l2 = loadval["articles"][1]["url"]
    l3 = loadval["articles"][2]["url"]
    i1 = loadval["articles"][0]["urlToImage"]
    i2 = loadval["articles"][1]["urlToImage"]
    i3 = loadval["articles"][2]["urlToImage"]
    total=loadval["totalResults"]
    return render_template('out.html',out1=r,out2=r1,out3=r2,link1=l1,link2=l2,link3=l3,img1=i1,img2=i2,img3=i3,final=news_predict[0],final2=news_predict[1],result=total)



if __name__ == '__main__':
    app.run()
