# Write your solution here:
def sort_by_remaining_stock(items:list):
    #(name, price, remaining)
    return sorted(items, key=order_by_remain)

def order_by_remain(item:tuple):
    return item[2]