#!/usr/bin/python3
"""Flask app for HBNB project"""
from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
app.config['JSONIFY_PRETYYPRINT_REGULAR'] = True

CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown_appcontext(execption):
    """Teardown app context"""
    storage.close()

@app.teardown_appcontext
def close_storage(exception):
    """Close the storage when the app context is closed"""
    storage.close()

@app.errorhandlder(404)
def not_found(error):
    """Handle 404 errors by returning a JSON-formatted response"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
