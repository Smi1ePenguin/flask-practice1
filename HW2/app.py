from flask import Flask, redirect, render_template, request, url_for
from werkzeug.wrappers import Response

app = Flask(__name__)

todos: list[str] = []


@app.route('/', methods=['GET', 'POST'])
def index() -> str | Response:
    if request.method == 'POST':
        todo = request.form['todo']
        todos.append(todo)
        return redirect(url_for('index'))
    return render_template('index.html', todos=todos)


@app.route('/delete/<int:index>')
def delete(index: int) -> Response:
    if 0 <= index < len(todos):
        del todos[index]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
