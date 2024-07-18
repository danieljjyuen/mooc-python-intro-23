# write your solution here
def row_sums():
    lists = []
    with open("matrix.txt") as file_main:
        for line in file_main:
            line = line.replace("\n","")
            parts = [int(x) for x in line.split(",")]
            lists.append(sum(parts))
    return lists

def matrix_sum():

    list = row_sums()
    
    return sum(list)


def matrix_max():
    great = 0
    with open("matrix.txt") as file_main:
        for line in file_main:
            line = line.replace("\n","")
            parts = [int(x) for x in line.split(",")]
            if great < max(parts):
                great = max(parts)

    return great

# print(matrix_max())