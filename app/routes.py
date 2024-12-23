from flask import Flask, render_template


def register_route(app):
    # localhost: 5000/ get
    @app.route("/")
    def home():
        return "Welcome to Flask"
    
    # localhost:5000/ get
    @app.route("/about")
    def about():
        return "This is the about page"
    
