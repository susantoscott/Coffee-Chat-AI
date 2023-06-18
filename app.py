from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
sys.path.append('src/')

from article import article
from twitter import twitter
from youtube import youtube

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'Message': 'Hello there 👋'})

@app.route('/formData', methods=['POST'])
def form_data():
    d = request.form.to_dict()
    name = d['name']
    article_url = d['article_url']
    twitter_url = d['twitter_url']
    youtube_url = d['youtube_url']

    def add_to_question_bank(questions_list):
        for question in questions_list:
            question_bank.append(question)
    
    question_bank = []
    add_to_question_bank(article(article_url))
    add_to_question_bank(twitter(twitter_url))
    add_to_question_bank(youtube(youtube_url))

    return jsonify({'Name': name, 'Questions': question_bank})

@app.route('/query')
def query():
    return jsonify(list({'Question 1', 'Question 2'}))

if __name__ == '__main__':
    app.run()
