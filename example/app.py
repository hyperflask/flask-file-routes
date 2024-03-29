from flask import Flask
from flask_file_routes import FileRoutes


app = Flask(__name__)
FileRoutes(app)


POSTS = [
    {
        "slug": "hello-world",
        "title": "Hello world",
        "content": "hello"
    }
]