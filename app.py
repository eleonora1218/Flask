# WORKING WITH QUERY STRINGS WITH FLASK
# WORKING WITH QUERY STRINGS WITH FLASK
# WORKING WITH QUERY STRINGS WITH FLASK

from flask import Flask, request

# creates an 'Application Object'
# class (class names are always capitalized)
# makes a new server
# "I want flask to do it's thing in this file"
app = Flask(__name__)
# if file is not called app.py: 
# FLASK_APP=filename.py is passing an 'environmental variable'
# ...flask run

#to run in terminal: 'flask run' not '%run app.py'
# Environment: prodiction (default)
# Debug mode: off
# Running on http://127.0.0.1:5000, ^c to quit


# Enabling development envi:
# in terminal: FLASK_ENV=development flask run
# Environment: development
# Debug mode: on
# Running on http://127.0.0.1:5000, ^c to quit
# An easier way:
# When creating the venv, in terminal: export FLASK_ENV=development
# This will keep this envi until window is refreshed/closed


##########
# GET REQUESTS
# GET REQUESTS
# GET REQUESTS

# http://127.0.0.1:5000/
@app.route('/')
def home_page():
    html = """
    <html>
        <body>
            <h1>Homepage</h1>
            <p>Welcome to my site</p>
            <a href='/hello'>Go to our greetings page</a>
        </body>
    </html>
    """
    return html

# http://127.0.0.1:5000/hello
@app.route('/hello')
def say_hello():
    return 'HELLO THERE!'

# http://127.0.0.1:5000/goodbye
@app.route('/goodbye')
def say_bye():
    return 'GOOD BYE!'

# http://127.0.0.1:5000/helpme
@app.route('/helpme')
def help():
    html = """
    <html>
        <body>
            <h1>HELP?</h1>
            <p>This is the help page</p>
        </body>
    </html>
    """
    return html

# ##########

# # http://127.0.0.1:5000/search
# # Handle GET requests like /search?term=fun
# @app.route('/search')
# def search():
#     print(request.args) # ImmutableMultiDict([])
#     return 'Search page'

# http://127.0.0.1:5000/search?term=dog&sort=top
# print(request.args) -> ImmutableMultiDict([('term', 'dog'), ('sort', 'top')])
@app.route('/search')
def search():
    term = request.args['term']
    sort = request.args['sort']
    print(request.args) 
    return f'<h1>Search Results For: {term}.</h1> <p>Sorting by: {sort}.</p>'


##########
# POST REQUESTS
# POST REQUESTS
# POST REQUESTS

# http://127.0.0.1:5000/add-comment
@app.route('/add-comment')
def add_comment_form():
    """Display: form to add comment"""    
    return """
        <h1>Add Comment</h1>
        <form method='POST'>
            <input type='text' placeholder='comment' name='comment'/>
            <input type='text' placeholder='username' name='username'/>
            <button>Submit</button>
        </form>
    """
# When form is submitted, the page responds...
# Extracting the data
@app.route('/add-comment', methods=['POST'])
def save_comment():
    """Display: sucessful submission? & data submited"""  
    comment = request.form['comment']
    username = request.form['username']
    return f""" 
        <h1>Saved your comment!</h1>
        <ul>
            <li>Username: {username}</li>
            <li>Comment: {comment}</li>
        </ul>
    """


##########
# PATH VARIABLES
# PATH VARIABLES
# PATH VARIABLES

#  http://127.0.0.1:5000/r/puffins
@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f'<h1>Browsing The {subreddit} subreddit</h1>'


# Mock database
POSTS = {
    1: 'I like puffins',
    2: 'I like mayo',
    3: 'I like bunnies'
}
# http://127.0.0.1:5000/posts/1
# http://127.0.0.1:5000/posts/2
# http://127.0.0.1:5000/posts/3
@app.route('/posts/<int:id>') 
def find_post(id):
    post = POSTS[id]
    return f'<p>{post}</p>'


# http://127.0.0.1:5000/r/puffins/comments/18
# @app.route('/r/<subreddit>/comments/<post_id>') post_id can be int or str
@app.route('/r/<subreddit>/comments/<int:post_id>') # post_id is strickly int
def show_comments(subreddit, post_id):
    return f'<h3>Viewing comments for post with id: {post_id} from the {subreddit} subreddit</h3>'


# URL parameter: "subject of page" /shop/<toy>
# Query parameter: "extra info about page" /shop?toy=elmo

# http://127.0.0.1:5000/shop/elmo?color=red
@app.route("/shop/<toy>")
def toy_detail(toy):
    """Show detail about a toy."""
    color = request.args.get("color")
    return f"<h1>{toy}</h1>Color: {color}"
