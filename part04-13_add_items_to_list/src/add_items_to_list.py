# Write your solution here
list =[]

number = int(input("How many items:"))
for i in range(1, number+1):
    num = int(input(f"Item {i}:"))
    list.append(num)
print(list)