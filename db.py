import sqlite3

conn = sqlite3.connect('inventoryStock.db')
c = conn.cursor()

try:
 c.execute("CREATE TABLE inventoryStock (Name TEXT NOT NULL, Description TEXT NOT NULL, Price INTEGER NOT NULL, DateAdded TEXT NOT NULL, ID INTEGER NOT NULL, Status boolean NOT NULL, checkInTrackerCount INTEGER NULL, checkOutTrackerCount INTEGER NULL)")
except:
  pass