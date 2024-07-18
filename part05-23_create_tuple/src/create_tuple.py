def create_tuple(x:int, y: int, z:int):
    unsorted = [x, y, z]

    unsorted.sort()
    return (unsorted[0], unsorted[2], sum(unsorted))


#print(create_tuple(1,2,3))