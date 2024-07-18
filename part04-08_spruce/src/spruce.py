# Write your solution here
def spruce(n):
    print("a spruce!")
    num = 1
    for i in range(1,n+1):
        print(" "*(n-i) + "*"*num)
        num+=2
    print(" "*(n-1)+"*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)