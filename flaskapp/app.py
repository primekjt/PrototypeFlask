# file name : app.py
# pwd : /project_name/app_name/appmain.py

from flaskapp import app

@app.before_request
def before_request():
    """html 코딩 시 서버 재시작 없이 html 리로드하기 설정 함수"""
    app.jinja_env.cache = {}
    return

@app.after_request
def after_request(response):
    #print('after_request')
    return response


if __name__ == '__main__':
    # 런타임으로 html 코딩을 위해 html 코딩 시 서버 재시작 없이 html 리로드하기 설정
    app.before_request(before_request)

    # 실행
    app.run(host='localhost', port=80, debug=True)