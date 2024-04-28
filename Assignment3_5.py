# Problem Statement : Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as 
# MarvellousNum. Name of the function from main python file should be ListPrime(). 

import MarvellousNum 

def ListPrime(Size,List):
    Sum = 0
    for i in List:
        if MarvellousNum.ChkPrime(i):
            Sum = Sum + i
    return Sum

def main():
    print("Enter number of elements : ",end=" ")
    Size = int(input())

    list = []

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())

        list.append(No)

    Ret = ListPrime(Size , list)

    print("Addition of pime numbers: ",Ret,end=" ")
if __name__ == "__main__":
    main()


# Test Case : 
# Input  : Number of elements : 11
# Input : 13  5  45  7  4  56  10  34 2  5  8
# Output : Addition of prime elements is : 32 (13 + 5 + 7 +2 + 5)  