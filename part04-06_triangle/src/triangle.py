# Copy here code of line function from previous exercise
def line(num, text):
    if text == "":
        text = "*"
    print(text[0]*num)

def triangle(size):
    # You should call function line here with proper parameters
    number = 1
    for i in range(size):
        line(number, "#")
        number+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
