import sqlite3

# Create database connection
conn = sqlite3.connect('sensor_data.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS data
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              temperature REAL,
              humidity REAL,
              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')

# Insert initial test data
c.execute("INSERT INTO data (temperature, humidity) VALUES (?, ?)", (25.5, 60.2))

# Commit changes and close connection
conn.commit()
conn.close()