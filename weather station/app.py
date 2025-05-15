from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def dashboard():
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT temperature, humidity, timestamp FROM data ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return render_template('dashboard.html',
                               temperature='N/A',
                               humidity='N/A',
                               temperatures=[],
                               humidities=[],
                               timestamps=[])

    # If data exists
    temperatures = [row[0] for row in reversed(rows)]
    humidities = [row[1] for row in reversed(rows)]
    timestamps = [row[2][-8:] for row in reversed(rows)]

    return render_template('dashboard.html',
                           temperature=temperatures[-1],
                           humidity=humidities[-1],
                           temperatures=temperatures,
                           humidities=humidities,
                           timestamps=timestamps)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

