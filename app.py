from flask import Flask, render_template

app = Flask(__name__)
posts = {
    0: {
        'title': 'Hello, wolrd!',
        'content': 'This is my first blog post!'
    }
}

@app.route('/')
def home():
    return 'Hello, world'

@app.route('/post/<int:post_id>') # /post/0
def post(post_id):
    return render_template('post.html', post=posts.get(post_id))

if __name__ == '__main__':
    app.run(debug=True)