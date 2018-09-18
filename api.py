from flask import Flask

app = Flask(__name__)


@app.route('/jobs')
def jobs():
    return 'jobs'


@app.route('/')
def hello():
    return 'Hello world'


app.run(port=80)
