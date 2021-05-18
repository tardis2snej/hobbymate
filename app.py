from flask import *
import analysis

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def hello_world_post():
    print("Post method called")
    analysis.compare_users(request.form['first-username'], request.form['second-username'])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)