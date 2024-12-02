from typing import List, Dict

def make_two_arrays(file_name)->[[int],[int]]:
    """
    Read the txt file in specific format and returns two arrays

    Args:
         file_name (txt): a txt file with two list of numbers saperated by "   " and "/n" on the second number in line

    Returns:
        array1: first array of int
        array2: second array of int
    """
    array1:[int]=[]
    array2:[int]=[]

    file = open(file_name)
    for line in file:
        pointer=line.split("   ")
        array1.append(int(pointer[0]))
        array2.append(int(pointer[1][:-1]))

    print(array1)
    print(array2)

    return array1, array2


"""
    Run through second array make a dictionary of howmuch would you multiply 
    than run and multiply by index of the dictionary
"""

def find_similarity_score(array1:[int],array2:[int])->int:

    """
    Run through array2 and make a dictionary of how many times each number is appearing
    than multiple each element form array1 based on count in the dictionary via the same key

    Args:
         array1: first array of integers
         array2: second array of integers

    Returns:
        similarity_score: the similarity_score between all elements in two arrays

    """
    repetition: Dict[int,int]={}
    for number in array2:
        repetition[number]=array2.count(number)
    print(repetition)
    simularity_score:int = 0
    for number in array1:
        try:
            simularity_score+=number*repetition[number]
        except:
            pass
    return simularity_score

array1,array2 = make_two_arrays('input.txt')
print(find_similarity_score(array1,array2))
