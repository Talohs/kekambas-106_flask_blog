from flask import request
from . import api
from app.models import Post

@api.route('/')
def index():
    return 'Hello this is the API'


#Endpoint to get all of the posts
@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return [p.to_dict() for p in posts]

#Endpoint to get a single post
@api.route('/post/<int:post_id>')
def get_post(post_id):
    post = Post.query.get_or_404(post_id)
    return post.to_dict()        

@api.route('posts', methods=['POST'])
def create_posts():
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    #Get the data from the request body
    data = request.json
    #Validate the incoming data
    for field in ['title', 'body', 'user_id']:
        if field not in data:
            return {'error': f"{field} must be in request body"}, 400
    
    title = data.get('title')
    body = data.get('body')
    user_id = data.get('user_id')

    new_post = Post(title=title, body=body, user_id=user_id)
    return new_post.to_dict(), 201