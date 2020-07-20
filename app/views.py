from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    a view route page function that returns index page and its data
    '''
    return render_template('index.html')


@app.route('/news/<news_id>')
def news(news_id):
    '''
    a news article function that returns news article details and its data
    '''
    return render_template('news.html',id = news_id)