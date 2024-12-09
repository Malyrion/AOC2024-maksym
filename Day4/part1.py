""" Consider input as a matrix, create a matrix of all letters.
Than consider all the cases of letter apperaing.
normal-horizontal
backwards - horizontal
noraml-vertical
backwards -vertical
normal - vertical -diagonal left
normal - vertical -diagonal right
backwards - vertical - dioagana left
backwards - vertical - diagonal right

Total of 8 cases. Loop througth each element in 2d array until you find "X" once found do each test and count positive ones
"""
import pandas as pd

def find_xmas(file_name):
    sum=0
    matrix= pd.read_csv(file_name)
    print(matrix.iloc[2,4:6])
    # with open(file_name) as file:
    #     for index_l,line in enumerate(file):
    #         print(line)
    #         for index_c,char in enumerate(line.strip()):
    #             if(line[index_c:index_c+4]=="XMAS"):
    #                 print("Allo")


find_xmas("input.txt")
