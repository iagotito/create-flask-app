import time

from flask import Flask
from flask import jsonify

START_TIMESTAMP = int(time.time())

app = Flask(__name__)


@app.route("/status", methods=["GET"])
def get_status():
    """Returns server status"""
    current_timestamp = int(time.time())
    status = {
        "status": "operational",
        "timestamp": current_timestamp,
        "started_at": START_TIMESTAMP,
        "service": "Flask app", # [[EDIT]]
    }
    return jsonify(status), 200
