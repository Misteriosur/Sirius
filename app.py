from flask import Flask, render_template, url_for
from flask import request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user')
def user():
    name = str(request.args.get('name'))
    id = str(request.args.get('id'))
    return 'user page: ' + name + '-' + str(id)

@app.route('/auth', methods=['get', 'post'])
def auth():
    if request.method == "POST":
        name = str(request.form.get('name'))
        id = str(request.form.get('id'))
        return render_template('user.html', name=name, id=id)
    elif request.method == "GET":
        return render_template('auth.html')



if __name__ == '__main__':
    app.run(debug=True)
