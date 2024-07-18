# Copy here code of line function from previous exercise and use it in your solution
def line(num, text):
    if text == "":
        text = "*"
    print(text[0]*num)

def shape(num1, char1, num2, char2):
    number = 1
    for i in range(num1):
        line(number, char1)
        number+=1
    for i in range(num2):
        line(num1, char2)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")