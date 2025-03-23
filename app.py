from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from routes.auth import auth_bp
    from routes.reviews import reviews_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(reviews_bp)

    @app.route("/")
    def home():
        return "🚛 LoadTrust API is running!"

    return app








