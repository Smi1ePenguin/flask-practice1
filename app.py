from flask import Flask, request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index() -> str:
    return f"<a href='{url_for('about')}'>소개로</a>"

@app.route('/about')
def about() -> str:
    return '소개 페이지'

@app.route('/user/<username>')
def profile(username: str) -> str:
    return f'{username} 님의 프로필'

@app.route('/post/<int:pid>')
def post(pid: int) -> str:
    return f'{pid}번 글 (자료형: {type(pid).__name__})'

@app.route('/notes/')         
def notes() -> str:
    return '메모 목록'

@app.route('/hello')
@app.route('/hello/<name>')   
def hello(name: str | None = None) -> str:
    if name:
        return f'안녕하세요, {name} 님'
    return '안녕하세요'


@app.route('/search')
def search() -> str:
    query = request.args.get('q', '')
    page = request.args.get('page', '1')

    if not query:
        return '검색어를 입력하세요'

    return f'"{escape(query)}" 검색 결과 ({escape(page)} 페이지)'


@app.route('/write', methods=['GET', 'POST'])
def write() -> str:
    if request.method == 'POST':
        banana = request.form['banana']
        melon = request.form['melon']
        return (
            f'banana = {escape(banana)} ({type(banana).__name__}) / '
            f'melon = {escape(melon)} ({type(melon).__name__})'
        )

    return '''
    <form method="post">
        <label>banana: <input type="text" name="banana"></label><br>
        <label>melon: <input type="number" name="melon"></label><br>
        <button type="submit">보내기</button>
    </form>'''


@app.route('/attach', methods=['GET', 'POST'])
def attach() -> str:
    if request.method == 'POST':
        f = request.files.get('cherry')
        if f is None:
            return 'cherry 가 files 에 없습니다'
        return f'{escape(f.filename)} / {len(f.stream.read())} 바이트'

    return '''
    <form method="post" enctype="multipart/form-data">
        <label>banana: <input type="text" name="banana"></label><br>
        <label>cherry: <input type="file" name="cherry"></label><br>
        <button type="submit">보내기</button>
    </form>'''
