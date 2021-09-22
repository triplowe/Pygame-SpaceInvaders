class RetailItem:

    def __init__(self, description, inventory, price):
        self.__description = description
        self. __inventory = inventory
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_inventory(self):
        return self.__inventory

    def get_price(self):
        return self.__price
        