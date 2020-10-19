from flask import Flask, render_template
from Utils import *

app = Flask(__name__)


@app.route('/scores')

def score_server():
    try:
     with open(SCORES_FILE_NAME, 'r') as f:
        return render_template('show_score.html', score = f.read())
    except IOError as e:
        return render_template('show_error.html', error = e.strerror)

app.run(host="0.0.0.0", port=5001, debug=True)

