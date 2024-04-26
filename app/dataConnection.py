import sqlite3
conn = sqlite3.connect('iot_management.db', check_same_thread=False)
curr = conn.cursor()