import os
from dotenv import load_dotenv
from flask import Flask

def create_app():
    load_dotenv()
    template_path=os.path.join(os.path.dirname(__file__),"..","templates")
    app=Flask(__name__,template_folder=template_path)
    app.secret_key=os.getenv("SECRET_KEY","default_secrets")
    from src.routes import main

    app.register_blueprint(main)
    return app
