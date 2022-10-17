from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'app secret key'

@app.route('/')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return 'Counter: '+str(session['counter'])

if __name__ == '__main__':
    app.debug = True
    app.run()