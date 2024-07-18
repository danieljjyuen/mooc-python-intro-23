# Write your solution here
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)

def greatest_number( a, b, c):
    great = a
    if a>=b:
        great = a
    else: 
        great = b
    if great >= c:
        great = great
    else:
        great = c

    return great