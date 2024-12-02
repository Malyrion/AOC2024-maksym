# create two lists reading form the txt file
# order the list in to ascending order
# loop through and calculate the distance inot a sum variable

def make_two_arrays(file_name)->[[int],[int]]:
    """
    Read the txt file in specific format and returns two arrays

    Args:
         file_name (txt): a txt file with two list of numbers separated by "   " and "/n" on the second number in line

    Returns:
        array1: the sum distances between all elements in two arrays
        array2:
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




def sum_distance(array1:[int], array2:[int])->int:
    """
    Sum the difference between values in two arrays

    Args:
         array1 ([nums]): first array of numbers
         array2 ([nums]): second array of numbers

    Returns:
        int: the sum of distances between all elements in two arrays
    """

    #sort both arrays into ascending order
    array1.sort()
    array2.sort()
    sum=0
    print(array1)
    print(array2)

    for i in range(0,len(array1)):
        if(array1[i]>array2[i]):
            print(array1[i]-array2[i])
            sum+=array1[i]-array2[i]
        else:
            print(array2[i]-array1[i])
            sum+=array2[i]-array1[i]
    return sum

array1, array2 = make_two_arrays("input.txt")
print(sum_distance(array1,array2))
