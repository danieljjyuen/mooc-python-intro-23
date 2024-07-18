# Write your solution here
def read_input(prompt:str, low, high):
    while True:
        try:
            number = int(input(prompt))
            if number >= low and number <= high:
                print(f"You typed in: {number}")
                return number
            else:
                print(f"You must type in an integer between {low} and {high}")
        except:
            print(f"You must type in an integer between {low} and {high}")

# read_input("tst", 5, 10)