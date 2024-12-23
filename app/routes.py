from flask import Flask, render_template


def register_route(app):
    
    #localhost:8080 / get

    @app.route("/")
    def home():
        return "Welcome to Flask"
