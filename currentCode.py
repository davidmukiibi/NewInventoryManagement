import sqlite3

conn = sqlite3.connect('inventoryStock.db')
c = conn.cursor()


class B(object):
    def __init__(self):
      pass

    def addItem(self):  # done

        # Create table
        c.execute("CREATE TABLE inventoryStocK (Name TEXT, ID INTEGER, Description TEXT, Price INTEGER, DateAdded TEXT, Status boolean )")
        Name = input('Enter the gadget name:')
        Description = input('Enter The Description of the Device:')
        Price = int(input('Enter The Price of the Device:'))
        DateAdded = input('Date when Device Arrived at Store:')
        Status = False
        ID = int(input('Device ID:'))
        c.execute("INSERT INTO inventoryStocK VALUES (?,?,?,?,?,?)", (Name, Description, Price, DateAdded, Status, ID))

        conn.commit()


        def removeItem(self):
        itemToRemove = input('enter an item u want to delete:')
        if itemToRemove is not '':
            itemInCharge = c.execute('SELECT * FROM inventory WHERE Name=(?)', (itemToRemove,))
            finalID = itemInCharge.fetchone()
            IdToItem = finalID[5]
            c.execute("DELETE FROM inventory WHERE ID=(?)", (IdToItem,))
            conn.commit() 
            print( 'you have deleted %s' % (itemToRemove))
        else:
            print('Please provide an item to delete and try again!')
            self.removeItem()