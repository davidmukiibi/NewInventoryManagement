import sqlite3 
from pathlib import Path 
 

conn = sqlite3.connect('inventoryStock.db') 
c = conn.cursor() 
 

db_name = Path('inventoryStock.db')
if not db_name.is_file(): 
  # Create table as the program starts to execute 
  c.execute("CREATE TABLE inventoryStock (Name TEXT NOT NULL, Description TEXT NOT NULL, Price INTEGER NOT NULL, DateAdded TEXT NOT NULL, Status boolean NOT NULL, ID INTEGER NOT NULL, checkInTrackerCount INTEGER NULL, checkOutTrackerCount INTEGER NULL)")   

class B(object):
  
  
      def __init__(self): 
        self.check_in_count = 0
        self.check_out_count = 0 
     
     
      def add_item(self):  # done 
        input_checker = input('Enter another item? (Yes Or No):') 
        if input_checker == 'Yes' or input_checker == 'YES' or input_checker == 'Y' or input_checker == 'y': 
          name = input('Enter the gadget name:') 
          description = input('Enter The Description of the Device:') 
          price = int(input('Enter The Price of the Device:')) 
          date_added = input('Date when Device Arrived at Store:') 
          item_id = int(input('Device ID:')) 
          self.check_in_count += 1 
          self.check_out_count = 0 
          status = False
          c.execute("INSERT INTO inventoryStock VALUES (?,?,?,?,?,?,?,?)", (name, description, price, date_added, status, item_id, self.check_in_count, self.check_out_count)) 
          conn.commit() 
          self.add_item() 
           
        else: 
          stock_in_object = c.execute('SELECT * FROM inventoryStock') 
          stock_in = stock_in_object.fetchall() 
          for i,item_with_its_details in enumerate(stock_in): 
            print ('{} {}'.format  (i+1, item_with_its_details)) 
 
 
      def remove_item(self): 
        item_to_remove = input('enter an item u want to delete:') 
        if item_to_remove is not '': 
          item_in_charge = c.execute('SELECT * FROM inventoryStock WHERE Name=(?)', (item_to_remove,)) 
          final_id = item_in_charge.fetchone() 
          print(final_id)
          id_to_item = final_id[5] 
          c.execute("DELETE FROM inventoryStock WHERE ID=(?)", (id_to_item,)) 
          conn.commit()  
          print( 'you have deleted %s' % (item_to_remove)) 
        else: 
          print('Please provide an item to delete and try again!') 
          self.remove_item() 
 
 
      def list_all_remaining_stock(self):  # done 
        remaining_stock_object = c.execute('SELECT * FROM inventoryStock') 
        remaining_stock = remaining_stock_object.fetchall()
        for each_item in remaining_stock:
          stock_item_name = each_item[0]
          stock_item_status = each_item[4]
          print('{} {}'.format(stock_item_name, stock_item_status))
          
 
 
      def item_view_id(self): 
        id_to_search_for = input('enter an ID you would like to search for:') 
        if id_to_search_for is not '': 
            all_items_with_id_object = c.execute('SELECT * FROM inventoryStock WHERE ID=(?)', (id_to_search_for,)) 
            all_items_with_id = all_items_with_id_object.fetchall() 
            print(all_items_with_id) 
                   
        elif id_to_search_for is 'X' or id_to_search_for is 'x': 
            print('bye') 
     
        else: 
            print('Please type in an ID whose items you want to see and press enter') 
            self.item_view_id() 
             
 
      def asset_value_of_inventory(self): 
        price_list = [] 
        actual_price_list = [] 
        price_list_object = c.execute('SELECT Price FROM inventoryStock') 
        price_list_values = price_list_object.fetchall() 
        for i in price_list_values: 
          j = i[0] 
          price_list.append(j) 
        total = sum(price_list) 
        print(total) 
         
         
      def check_in(self):
        check_in_item_id = input("enter an ID to checkin:")
        check_in_item_object = c.execute("SELECT Name FROM inventoryStock WHERE ID = (?)", (check_in_item_id,))
        check_in_item_result = check_in_item_object.fetchall()
        check_in_item = check_in_item_result[0][0]
        status = False 
        c.execute("UPDATE inventoryStock SET Status = (?) WHERE Name = (?)", (status, check_in_item)) 
        self.check_in_count += 1 
        c.execute("UPDATE inventoryStock SET checkInTrackerCount = (?) WHERE Name = (?)", (self.check_in_count, check_in_item))

 
 
      def check_out(self):
        check_out_item_id = input('enter an ID to checkout:') 
        check_out_item_object = c.execute("SELECT Name FROM inventoryStock WHERE ID = (?)", (check_out_item_id,))
        check_out_item_result = check_out_item_object.fetchall()
        check_out_item = check_out_item_result[0][0]
        status = True 
        c.execute("UPDATE inventoryStock SET Status = (?) WHERE Name = (?)", (status, check_out_item)) 
        self.check_out_count += 1 
        c.execute("UPDATE inventoryStock SET checkOutTrackerCount = (?) WHERE Name = (?)", (self.check_out_count, check_out_item))



      def search(self):
        item_to_search = input('enter a value to search:')
        search_result_object = c.execute("SELECT * FROM inventoryStock WHERE Name = (?)", (item_to_search,)) 
        search_result = search_result_object.fetchall()
        print('These are the items in the inventory that match your search string')
        for k,results in enumerate(search_result): 
            print ('{} {}'.format(k+1, results)) 






if __name__ == ("__main__"):
  new_item = B()
  new_item.add_item()
  new_item.remove_item()
  new_item.search() 
  new_item.check_in() 
  new_item.check_out()
  new_item.asset_value_of_inventory()
  new_item.item_view_id()
  new_item.list_all_remaining_stock()

