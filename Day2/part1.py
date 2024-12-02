def find_safe_entries(file_name)->[int]:
    """
    Read the txt file in specific format check if the line contains ascending numbers ascending at a rate 1 to 3
    or descending numbers descend at rate -1 to -3

    Args:
         file_name (txt): a txt file in specific format

    Returns:
        count: the sum valid entires in txt file

    """
    array2=[]
    count = 0;
    file = open(file_name)
    for line in file:
        array1=line.split(" " or "\n")
        for item in array1:
            array2.append(int(item))
        print(array2)
        for i in range(1,len(array2)):
            if(array2[0]-array2[1]>0):
                descend=True
            elif(array2[0]-array2[1]<0):
                descend=False
            else:
                count-=1
                break
            if(array2[i-1]-array2[i]==0 or array2[i-1]-array2[i]>3 or array2[i-1]-array2[i]<0 and descend==True):
                print("desending array should be positive")
                print(array2[i-1]-array2[i])
                count-=1
                break
            if(array2[i-1]-array2[i]==0 or array2[i-1]-array2[i]<-3 or array2[i-1]-array2[i]>0 and descend==False):
                print("ascending array should be negative")
                print(array2[i-1])
                print(array2[i])
                print(array2[i-1]-array2[i])
                count-=1
                break
        count+=1
        array2=[]
    return count




print(find_safe_entries("input.txt"))
