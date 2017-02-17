"""
Usage:
    inventory add <name> <description> <price> <date_added> <item_id>
    inventory remove <item_name>
    inventory list [--export]
    inventory checkout <item_id>
    inventory checkin <item_id>
    inventory item_view <item_id>
    inventory search <item_name>
    inventory assetvalue
    inventory list_export
    inventory export
    inventory 
    inventory (-i | --interactive)
    inventory (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
from docopt import docopt, DocoptExit
import cmd
import os
import sys
from pyfiglet import Figlet
from colorama import Fore, Back, Style, init
from inventory_management import Inventory
inventory = Inventory()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match
            # We print a message to the user and the usage block
            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():

    print(__doc__)


class InventoryCLI(cmd.Cmd):

    os.system("cls")

    init()

    font = Figlet(font = 'rev')

    print (Fore.YELLOW + font.renderText('Inventory Manager'))
    prompt = 'InventoryCLI >>> '

    @docopt_cmd
    def do_add(self, arg):
        """Usage: add <name> <description> <price> <date_added> <item_id>"""
        name = arg["<name>"]
        description = arg["<description>"]
        price = arg["<price>"]
        date_added = arg["<date_added>"]
        item_id = arg["<item_id>"]
        inventory.add_item(name, description, price, date_added, item_id)


    @docopt_cmd
    def do_remove(self, arg):
        """Usage: remove <item_id>"""
        id = arg["<item_id>"]
        inventory.remove_item(id)

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list [--export]"""
        inventory.list_all_remaining_stock()

    @docopt_cmd
    def do_item_view(self, arg):
        """Usage: item_view <item_id>"""
        id_to_search_for = arg["<item_id>"]
        inventory.item_view_id(id_to_search_for)

    @docopt_cmd
    def do_assetvalue(self, arg):
        """Usage: assetvalue"""
        inventory.asset_value_of_inventory()

    @docopt_cmd
    def do_check_in(self, arg):
        """Usage: checkin <item_id>"""
        check_in_item_id = arg["<item_id>"]
        inventory.check_in(check_in_item_id)

    @docopt_cmd
    def do_check_out(self, arg):
        """Usage: checkout <item_id>"""
        check_out_item_id = arg["<item_id>"]
        inventory.check_out(check_out_item_id)

    @docopt_cmd
    def do_list_export(self, arg):
        """Usage: list_export <filename>"""
        filename = arg["<filename>"]
        inventory.list_export(filename)

    @docopt_cmd
    def do_search_inventory(self, arg):
        """Usage: search <item_name>"""
        item_to_search = arg["<item_name>"]
        inventory.search(item_to_search)    


    def do_quit(self, arg):
        """Usage: quit"""
        os.system('clear')
        print ('Application Exiting')
        exit()


opt = docopt(__doc__,sys.argv[1:])
if opt["--interactive"]:
    InventoryCLI().cmdloop()
print(opt)    


       