import sqlite3

conn = sqlite3.connect('inventoryStock.db')
c = conn.cursor()


class B(object):

    def __init__(self):
        self.checkInTracker = []
        self.checkOutTracker = []

    def addItem(self):  # done
        #  create another table for tracking checkin and checkout
        c.execute("CREATE TABLE checkInOrOutTracking (checkInCount real, checkOutCount real)")
        # Create table
        c.execute("CREATE TABLE inventoryStocK (Name TEXT, ID INTEGER, Description TEXT, Price INTEGER, DateAdded TEXT, Status boolean )")
        Name = input('Enter the gadget name:')
        Description = input('Enter The Description of the Device:')
        Price = int(input('Enter The Price of the Device:'))
        DateAdded = input('Date when Device Arrived at Store:')
        Status = False
        self.checkIn()
        ID = int(input('Device ID:'))
        c.execute("INSERT INTO inventoryStock VALUES (?,?,?,?,?,?)", (Name, Description, Price, DateAdded, Status, ID))

        conn.commit()
        

def removeItem(self, itemToRemove):
    if itemToRemove is not '':
        IdToItem = c.execute('SELECT ID FROM inventoryStock WHERE (?)', (itemToRemove))
        c.execute("DELETE FROM inventoryStock WHERE ID=(?)", (IdToItem))
        checkOut()
        return 'you have deleted %s' % (itemToRemove)
    else:
        print('please provide an item to delete')


def checkIn():
    self.checkInTracker.append('a')
    checkInCount = len(self.checkInTracker)
    c.execute("INSERT INTO checkInOrOutTracking VALUES (?)", (checkInCount))


def checkOut():
    self.checkOutTracker.append('b')
    checkOutCount = len(self.checkOutTracker)
    c.execute("INSERT INTO checkInOrOutTracking VALUES (?)", (checkOutCount))


def viewInventoryForItemWithID(Id):
    Id = input('Enter ID of item you want to view:')
    if Id is not '':
        returnedIdItem =  c.execute("SELECT * FROM inventoryStock" )
        CHECKINCOUNT = c.execute("SELECT checkInCount FROM checkInOrOutTracking")
        CHECKOUTCOUNT = c.execute("SELECT checkOutCount FROM checkInOrOutTracking")
        return (returnedIdItem, CHECKINCOUNT, CHECKOUTCOUNT)
    else:
        print('please enter a value in the search box!')


def ListAllRemainingStock():  # done
    remainingStock = c.execute('SELECT * FROM inventoryStock')
    print(remainingStock)


def searchInventory(self):
    userSearchInput = input('what do ypu want to find?')
    if userSearchInput is not '':
        searchResult = c.execute('SELECT * FROM inventoryStock WHERE Name=userSearchInput')
        return searchResult
    else:
        print('please enter a value in the search area')
        self.searchInventory()



conn.close()


newItem = B()
newItem.addItem()