import flask
import requests
import re
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return """<h1>Invalid Route! <br> Use <a href="http://localhost/getTimeStories">http://localhost/getTimeStories</a></h1>"""

@app.route('/getTimeStories',methods=['GET'])
def getTimeStories():
    response = requests.get("https://time.com")
    pattern = "<li class=\"latest-stories__item\">\s*.*<a href=\"(.*)\">\s*<h3 class=\"latest-stories__item-headline\">(.*)</h3>"
    data = re.findall(pattern,response.text)
    output_list=[]
    for i in range(0,len(data)):
        temp = {'title':data[i][1], 'link':"https://time.com"+data[i][0]}
        output_list.append(temp)
    return (json.dumps(output_list))

app.run(host= '0.0.0.0',port=80)