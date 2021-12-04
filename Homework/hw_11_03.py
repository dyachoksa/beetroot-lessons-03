"""
Product Store

Write a class Product that has three attributes:
    type
    name
    price

Then create a class ProductStore, which will have some Products and will operate with 
all products in the store. All methods, in case they can’t perform its action, should 
raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. 
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price 
    premium for your store(30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products 
    specified by input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name, amount) - removes a particular amount of products from the store 
    if available, in other case raises an error. It also increments income 
    if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""

class Product:
    def __init__(self, type_, name, price):
        self.type = type_
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = []
        self.income = 0

    def add(self, product, amount):
        self.products.append({
            "product": product,
            "amount": amount
        })

    def set_discount(self, identifier, percent, identifier_type='name'):
        pass

    def sell_product(self, product_name, amount):
        for p in self.products:
            product_in_store = p["product"]
            amount_in_store = p["amount"]

            if product_in_store.name != product_name:
                continue

            if amount_in_store < amount:
                raise ValueError(f"Can't sell {amount} product(s). Store contains only {amount_in_store}.")

            p['amount'] -= amount

            self.income += product_in_store.price * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        for product in self.products:
            product_in_store = product["product"]
            amount_in_store = product["amount"]

            print("{}\t | {}\t | ${}\t | {}".format(
                product_in_store.type,
                product_in_store.name,
                product_in_store.price,
                amount_in_store if amount_in_store > 0 else "Not in store"
            ))

    def get_product_info(self, product_name):
        for p in self.products:
            product_in_store = p["product"]
            amount_in_store = p["amount"]

            if product_in_store.name != product_name:
                continue

            return (product_in_store.name, amount_in_store)
        
        raise ValueError("Product not found")


def main():
    store = ProductStore()

    p1 = Product("Sport", "Football T-Shirt", 100)
    p2 = Product("Food", "Ramen", 1.5)

    store.add(p1, 10)
    store.add(p2, 100)

    print("Initial store state:")
    store.get_all_products()

    print("Selling 10 ramens...")
    store.sell_product("Ramen", 10)

    print("Store state after selling:")
    store.get_all_products()

    print("Total income: ${}".format(store.get_income()))


if __name__ == "__main__":
    main()
