# Problem Statement : Write a program which accepts N numbers from user and store it into List. Return Maximum of all elemnts from that list.

def Maximum(List):
    Max = List[0]

    for i in range(0,len(List)):
        if(List[i] > Max):
            Max = List[i]
    return Max

def main():
    print("Enter number of elements : ",end=" ")
    Size = int(input())

    Array = list()

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())

        Array.append(No)

    Ret = Maximum(Array)

    print('Maximum of list elements is : ',Ret,end=" ")
if __name__ == "__main__":
    main()

    
# Test Case : 
# Input  : Number of elements : 7
# Input : 13  5  45  7  4  56  34
# Output : Maximum number of list elements is : 56  