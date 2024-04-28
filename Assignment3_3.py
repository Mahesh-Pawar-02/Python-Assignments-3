# Problem Statement : Write a program which accepts N numbers from user and store it into List. Return Minimum of all elemnts from that list.

def Minimum(List):
    Min = List[0]

    for i in range(0,len(List)):
        if(List[i] < Min):
            Min = List[i]
    return Min

def main():
    print("Enter number of elements : ",end=" ")
    Size = int(input())

    Array = list()

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())

        Array.append(No)

    Ret = Minimum(Array)

    print('Minimum number of list elements is : ',Ret,end=" ")
if __name__ == "__main__":
    main()

    
# Test Case : 
# Input  : Number of elements : 4
# Input : 13  5  45  7
# Output : Minimum number in list elements is : 5 