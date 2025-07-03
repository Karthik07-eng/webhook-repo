```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from utils import is_fresh_data

app = Flask(__name__)

last_displayed = set()
REFRESH_WINDOW_MINUTES = 10

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400

    timestamp_str = data.get('timestamp')
    entry_id = data.get('id')

    if not timestamp_str or not entry_id:
        return jsonify({"error": "Missing required fields"}), 400

    # Parse timestamp
    try:
        timestamp = datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return jsonify({"error": "Invalid timestamp format"}), 400

    # Check if data is fresh and unique
    if is_fresh_data(timestamp, REFRESH_WINDOW_MINUTES) and entry_id not in last_displayed:
        last_displayed.add(entry_id)
        print(f"✅ New webhook data received: {data}")
        return jsonify({"status": "data processed"}), 200

    return jsonify({"status": "ignored duplicate/stale data"}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
