#from simple_web_server import Handler
from inventory_web import *

def test_inventory_web():
    '''
    Test various features
    '''

    invent = create_inventory()    # Create inventory

    print(invent.print_inventory(3, 6))   # Print items from 3 to 5, inclusive

    # Print the name and the type of first and last item
    print('first:')
    print(str(invent.items[0].name))
    print('type:', invent.check_type(invent.items[0]))

    print('last:')
    print(str(invent.items[invent.count-1].name))
    print('type:', invent.check_type(invent.items[invent.count-1]))

    # Print the total value of the inventory
    print('Total value of the inventory: $' + str(invent.compute_inventory()))

    # Print a particular category of items
    print(str(invent.print_category('fashion')))
    print(str(invent.print_category('Book')))

    # Search and print items that contain the term as a substring in its name
    print(str(invent.search_item('Time')))
    print(str(invent.search_item('Gar')))

test_inventory_web()

