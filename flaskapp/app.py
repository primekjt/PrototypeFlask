# file name : app.py
# pwd : /project_name/app_name/appmain.py

from flaskapp import app
from flask import render_template

#from flask import request, url_for, current_app


@app.before_request
def before_request():
    #print('before_request')
    return

@app.after_request
def after_request(response):
    #print('after_request')
    return response

@app.route('/')
def flask_app():
    return render_template('content/index.html')

@app.route('/hello')
def hello_world():
    # Movie Titles - Stored as an array
    movie_names = ['Avatar',
                   'Pirates of the Caribbean',
                   'Spectre',
                   'The Dark Knight Rises',
                   'John Carter',
                   'Spider-Man 3',
                   'Tangled']

    # Movie Titles with Attributes - Stored in a Dictionary
    movies = {
        'Avatar': {'critical_reviews': 723, 'duration': 178, 'imdb_score': 7.9},
        'Pirates of the Caribbean': {'critical_reviews': 302, 'duration': 169, 'imdb_score': 7.1},
        'Spectre': {'critical_reviews': 602, 'duration': 148, 'imdb_score': 6.8},
        'The Dark Knight Rises': {'critical_reviews': 813, 'duration': 164, 'imdb_score': 8.5},
        'John Carter': {'critical_reviews': 462, 'duration': 132, 'imdb_score': 6.6},
        'Spider-Man 3': {'critical_reviews': 392, 'duration': 156, 'imdb_score': 6.2},
        'Tangled': {'critical_reviews': 324, 'duration': 100, 'imdb_score': 7.8},
    }
    return render_template('content/hello.html', movie_names=movie_names, movies=movies)

@app.route('/login')
def login():
    return render_template('content/login.html')



def before_request_func():
    """html 코딩 시 서버 재시작 없이 html 리로드하기 설정 함수"""
    app.jinja_env.cache = {}

if __name__ == '__main__':
    # 런타임으로 html 코딩을 위해 html 코딩 시 서버 재시작 없이 html 리로드하기 설정
    app.before_request(before_request_func)

    # 실행
    app.run(host='localhost', port=80, debug=True)