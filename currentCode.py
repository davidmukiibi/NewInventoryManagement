import sqlite3

conn = sqlite3.connect('inventoryStock.db')
c = conn.cursor()

# Create table as the program starts to execute
c.execute("CREATE TABLE inventoryStock (Name TEXT, ID INTEGER, Description TEXT, Price INTEGER, DateAdded TEXT, Status boolean )")  

class B(object):
    def __init__(self):
      pass
    
    def addItem(self):  # done

        
        Name = input('Enter the gadget name:')
        Description = input('Enter The Description of the Device:')
        Price = int(input('Enter The Price of the Device:'))
        DateAdded = input('Date when Device Arrived at Store:')
        Status = False
        ID = int(input('Device ID:'))
        c.execute("INSERT INTO inventoryStock VALUES (?,?,?,?,?,?)", (Name, Description, Price, DateAdded, Status, ID))

        conn.commit()


    def removeItem(self):
        itemToRemove = input('enter an item u want to delete:')
    if itemToRemove is not '':
        itemInCharge = c.execute('SELECT * FROM inventoryStock WHERE Name=(?)', (itemToRemove,))
        finalID = itemInCharge.fetchone()
        IdToItem = finalID[5]
        c.execute("DELETE FROM inventoryStock WHERE ID=(?)", (IdToItem,))
        conn.commit() 
        print( 'you have deleted %s' % (itemToRemove))
    else:
        print('Please provide an item to delete and try again!')
        self.removeItem()



    def listAllRemainingStock(self):  # done
        remainingStockObject = c.execute('SELECT * FROM inventoryStock')
        remainingStock = remainingStockObject.fetchone()
        print(remainingStock)    


    def itemViewId(self):
        idToSearchFor = input('enter an ID you would like to search for:')
        if idToSearchFor is not '':
            allItemsWithIDObject = c.execute('SELECT * FROM inventoryStock WHERE ID=(?)', (idToSearchFor,))
            allItemsWithID = allItemsWithIDObject.fetchone()
            print(allItemsWithID)
                  
        elif idToSearchFor is 'X' or idToSearchFor is 'x':
            print('bye')
    
        else:
            print('Please type in an ID whose items you want to see and press enter')
            self.itemViewId()


    def assetValueOfInventory(self):
        priceList = c.execute('SELECT Price FROM inventoryStock')
        totalAssetValue = sum(priceList.fetchone())
        print(totalAssetValue)       
