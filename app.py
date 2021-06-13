from flask import *
import analysis
import os

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def do_analysis():
    print("Post method called")
    try:
        first_username = Markup(request.form['first-username'])
        second_username = Markup(request.form['second-username'])
        prediction, similarities, posts = analysis.compare_users(first_username, second_username)
        return render_template('analysis.html', prediction=prediction, similarities=similarities.keys(), posts=posts)
    except Exception as e:
        print(e)
        flash('Something gone wrong! Check that you entered usernames right and try again!')
        return render_template('index.html')


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)
    # analysis.compare_users('tardis2snej', 'minortismay')
