from flask import Flask
from delivery.web.blueprints.migrate import migrate_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(migrate_bp)
    return app
