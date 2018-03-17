from flask import Flask
from flask import request, send_file
import readline
import os
import subprocess
app = Flask(__name__)
kurwa=''
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'
@app.route('/mkdir')
def test():
   os.mkdir('test')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/testroute')
def my_route():
  start = request.args.get('start', default = 1, type = int)
  end = request.args.get('end', default = 1, type = int)
  readline.readsl(start,end)
  return send_file('tmp.txt')
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
