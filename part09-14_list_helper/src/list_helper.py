# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        count = 0
        result = None
        for item in my_list:
            freq = my_list.count(item)
            if freq > count :
                count = freq
                result = item
        
        return result
    
    @classmethod
    def doubles(cls, my_list:list):

        setlist = list(set(my_list))

        count = 0

        for item in setlist:
            if my_list.count(item) >1:
                count+=1

        return count