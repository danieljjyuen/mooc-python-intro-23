# Write your solution here
def prime_numbers():
    number = 2
    while True:
        for x in range(2,number):
            if number % x ==0:
                break
        else:    
            yield number
        number+=1 
