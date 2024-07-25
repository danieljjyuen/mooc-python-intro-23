# Write your solution here
#(name, price, amount

def search(products: list, criterion: callable):
    return [product for product in products if criterion(product)]