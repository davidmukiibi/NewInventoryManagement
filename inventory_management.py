import sqlite3

import csv

from tabulate import tabulate

from db import c, conn

from pathlib import Path


class Inventory(object):

    def __init__(self, status=False, check_in_count=0, check_out_count=0):

        self.status = status

        self.check_in_count = check_in_count

        self.check_out_count = check_out_count

    def add_item(self, name, description, price, date_added, item_id):

        self.check_in_count += 1

        c.execute("INSERT INTO inventoryStock VALUES (?,?,?,?,?,?,?,?)", (name, description,
                                                                          price, date_added, item_id, self.status, self.check_in_count, self.check_out_count))

        conn.commit()
        

        print('Successfully added')

    def remove_item(self, id):

        c.execute("DELETE FROM inventoryStock WHERE ID=:item_id",{"item_id":id})
        conn.commit()
        print('you have deleted successfully')

        #print('you have deleted %s' % (item_to_remove))

    def list_all_remaining_stock(self):  # done
        remaining_stock_object = c.execute('SELECT * FROM inventoryStock')
        remaining_stock = remaining_stock_object.fetchall()
        for each_item in remaining_stock:
            stock_item_name = each_item[0]
            stock_item_status = each_item[4]
            print('{} {}'.format(stock_item_name, stock_item_status))

    def item_view_id(self, id_to_search_for):

        if id_to_search_for is not '':

            all_items_with_id_object = c.execute(
                'SELECT * FROM inventoryStock WHERE ID=(?)', (id_to_search_for,))

            all_items_with_id = all_items_with_id_object.fetchall()

            print(tabulate(all_items_with_id, headers=[
                  "Name", "Description", "Price", "Date Added", "ID", "Status", 'Check In', "Check out"]))

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
        print('Your inventory is worth')
        print(total)

    def check_in_item(self, check_in_item_id):

        check_in_item_object = c.execute(
            "SELECT Name FROM inventoryStock WHERE ID = (?)", (check_in_item_id,))

        check_in_item_result = check_in_item_object.fetchall()

        check_in_item = check_in_item_result[0][0]

        status = False

        c.execute("UPDATE inventoryStock SET Status = (?) WHERE Name = (?)",
                  (status, check_in_item))

        self.check_in_count += 1

        c.execute("UPDATE inventoryStock SET checkInTrackerCount = (?) WHERE Name = (?)",
                  (self.check_in_count, check_in_item))

    def check_out(self, check_out_item_id):

        check_out_item_object = c.execute(
            "SELECT Name FROM inventoryStock WHERE ID = (?)", (check_out_item_id,))

        check_out_item_result = check_out_item_object.fetchall()

        check_out_item = check_out_item_result[0][0]

        status = True

        c.execute("UPDATE inventoryStock SET Status = (?) WHERE Name = (?)",
                  (status, check_out_item))

        self.check_out_count += 1

        c.execute("UPDATE inventoryStock SET checkOutTrackerCount = (?) WHERE Name = (?)",
                  (self.check_out_count, check_out_item))

    def search(self, item_to_search):

        search_result_object = c.execute(
            "SELECT * FROM inventoryStock WHERE Name = (?)", (item_to_search,))

        search_result = search_result_object.fetchall()

        print('These are the items in the inventory that match your search string')

        for k, results in enumerate(search_result):

            print('{} {}'.format(k + 1, results))

    def list_export(self, filename='friday'):
        stock_left = c.execute('SELECT * FROM inventoryStock')
        with open(filename +'.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Description', 'Price' 'Date Added', 'Item ID', 'Check Count', 'Checkout Count'])
            writer.writerows(stock_left)
            print("Inventory successfully exported as a CSV file!")
        conn.commit()
