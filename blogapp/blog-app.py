from flask import Flask

app = Flask(__name__)

# random data I added for blog posts using HTML
posts = [
    {
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'author': 'Jiya Bharti',
        'date_posted': 'January 1, 2024'
    },
    {
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'author': 'Taylor Swift',
        'date_posted': 'February 15, 2024'
    }
]

@app.route('/')
def homepage():
    return """
    <!doctype html>
    <html>
        <head>
            <title>Cute Cats Blog</title>
        </head>
        <body>
            <h1>Welcome to the Cute Cats Blog!</h1>
            <h2>Latest Posts:</h2>
            <ul>
                <li><a href="/posts/1">First Post</a> by Jiya Bharti (January 1, 2024)</li>
                <li><a href="/posts/2">Second Post</a> by Taylor Swift (February 15, 2024)</li>
            </ul>
        </body>
    </html>
    """

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = posts[post_id - 1]  # adjusting index since post_id starts from 1
    return """
    <!doctype html>
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h1>{title}</h1>
            <p>{content}</p>
            <p>Written by {author} on {date_posted}</p>
            <a href="/">Back to Home</a>
        </body>
    </html>
    """.format(title=post['title'], content=post['content'], author=post['author'], date_posted=post['date_posted'])

if __name__ == '__main__':
    app.run(debug=True)
