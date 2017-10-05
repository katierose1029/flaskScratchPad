from flask import Flask
import datetime
from time import gmtime, strftime
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello who cares!'

@app.route('/time')
def time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

@app.route('/gekki')
def gekki():
    return 'gekki all your base belong to me!'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
