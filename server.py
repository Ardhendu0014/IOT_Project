from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/latest_temperature', methods=['GET'])
def latest_temperature():
    conn = sqlite3.connect('temperature_data.db')
    cursor = conn.cursor()
    cursor.execute('SELECT value, timestamp FROM temperature ORDER BY timestamp DESC LIMIT 1')
    result = cursor.fetchone()
    conn.close()
    return jsonify({'temperature': result[0], 'timestamp': result[1]})

if __name__ == "__main__":
    app.run(debug=True)
