# file name : main.py
# pwd : /project_name/main.py

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
    title_text = 'Flask Web Page'
    dept = '조직'
    return render_template('content/index.html', title=title_text, dept=dept+':좋은팀')

@app.route('/hello')
def hello_world():
    return "Hello Flask World!!!"

def before_request_func():
    """html 코딩 시 서버 재시작 없이 html 리로드하기 설정 함수"""
    app.jinja_env.cache = {}

if __name__ == '__main__':
    # 런타임으로 html 코딩을 위해 html 코딩 시 서버 재시작 없이 html 리로드하기 설정
    app.before_request(before_request_func)

    # 실행
    app.run(host='localhost', port=80, debug=False)