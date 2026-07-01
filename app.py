from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'
app.debug = True
toolbar = DebugToolbarExtension(app)

@app.route('/')
def index():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run()