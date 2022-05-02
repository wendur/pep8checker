from flask import Flask, render_template, request
from PepChecker import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    pep = PepChecker()
    text = ""

    if request.method == 'POST':
        text = request.form["comment"]
        pep.get_errors(text)

    errors = pep.error_list

    return render_template('index.html', text=text, errors=errors, num=len(errors))


if __name__ == '__main__':
    app.run()
