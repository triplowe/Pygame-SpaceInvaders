import RetailItemClass as i

def main():
    item1 = i.RetailItem("Jacket", 12, 59.95)
    item2 = i.RetailItem("Designer Jeans", 40, 34.95)
    item3 = i.RetailItem("Shirt", 20, 24.95)

    print(item1.get_description(), item1.get_inventory(), item1.get_price())
    print(item2.get_description(), item2.get_inventory(), item2.get_price())
    print(item3.get_description(), item3.get_inventory(), item3.get_price())


main()