# Problem Statement : Write a program which accepts N numbers from user and store it into List. Return addition of all elemnts from that list.

def Addition(List):
    Sum = 0
    for i in List:
        Sum = Sum + i
    return Sum

def main():
    print("Enter number of elements : ",end=" ")
    Size = int(input())

    Array = list()

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())

        Array.append(No)

    Ret = Addition(Array)

    print('Addition of list elements is : ',Ret,end=" ")
if __name__ == "__main__":
    main()

# Test Case : 
# Input  : Number of elements : 6
# Input : 13  5  45  7  4  56
# Output : Addition of list elements is : 130  