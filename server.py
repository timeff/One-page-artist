from flask import Flask
from flask import render_template
from flask import request
import requests
import json
import wikipedia
import os

app = Flask(__name__)

# def youtube_search(term):
# 	r = requests.get('https://www.googleapis.com/youtube/v3/search?part=snippet&key=AIzaSyABqdxsRus8IUMwnYqpyKmsbGBhM4SMtqc&type=video&q='+term)
# 	r.text

# 	data = json.loads(r.text)

# 	youtube=[]

# 	for x in data['items']:
# 		temp=[]
# 		url="https://www.youtube.com/embed/"+x['id']['videoId']
# 		temp.append(url)
# 		temp.append(x['snippet']['title'])
# 		temp.append(x['snippet']['description'])
# 		temp.append(x['snippet']['thumbnails']['default']['url'])
# 		youtube.append(temp)

# 	return youtube

# def wiki_search(term):
# 	result = wikipedia.page(term)
# 	return result

# @app.route('/')
# def index():
# 	return render_template('index.html')
    

# @app.route('/result',methods=['GET'])
# def result():
# 	searchword = request.args.get('search', '')
# 	youtube_list=youtube_search(searchword)
# 	article=wiki_search(searchword)
# 	img="";
# 	for x in article.images:
# 		if x.find(searchword[0:1])!=-1:
# 			img=x
# 			break


# 	return render_template('result.html',youtube_list=youtube_list,article=article,image=img)

@app.route('/test')
def test():
	return "test"

if __name__ == "__main__":
    app.run()