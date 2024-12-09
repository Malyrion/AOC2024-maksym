''' Read the file line by line. find the position of "m" check if the next leters "mult(" if not do nothing
 else if its a match if the next , loop max of 8 times (3 +3 +, + )) if no ")" than skip this case, if ")" is less than 4
 than also skip the case, check if the "," is present and check that items are either "," or a number. If all good we take the
 string of the loop and split on , and get the two digits, we multipy and save result to counter
 '''

def find_mult(file_name):
    """
    Read the file and find in "mul(" string exist if yes than loop 8 times or until you found ")" at last position or before
    if you find it before and all items were int with a comma, you have made 2 strings with number, multiply them and
    calculate the sum of all occurrences. If the "don't()" was found skip all "mul(" until you find "do("
    :param file_name: input file
    :return:
    """
    sum = 0
    count_mul=0
    do=True
    with open(file_name) as file:
        for line in file:
            i = 0
            while i < len(line):
                if line[i:i+4] == "do()":
                    do=True
                if line[i:i+7] == "don't()":
                    do=False
                if line[i:i+4] == "mul(" and do:
                    count_mul+=1
                    pointer = i + 4
                    number1 = ""
                    number2 = ""
                    switch=False
                    while pointer < i+12 and line[pointer] != ")":
                        char = line[pointer]
                        # print("char is: ", char)
                        if char.isdigit():
                            if(not switch):
                                number1+=char
                            else:
                                number2+=char
                        elif char == ",":
                            switch=True
                        elif not char.isspace():
                            # print(f"{char} is not an int current sum {sum}")
                            break
                        pointer += 1
                    # print(f"Found 'mul' with numbers: {number1} and {number2}")

                    try:
                        if(line[pointer]==")"):
                            sum += int(number1)*int(number2)
                        else:
                            pass
                    except:
                        # print(f"trying to multiply this: {number1} and {number2}")
                        pass
                    print(sum)
                i += 1
    print("final", count_mul)

find_mult("input.txt")
