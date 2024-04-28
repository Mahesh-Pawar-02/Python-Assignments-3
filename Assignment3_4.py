# Problem Statement : Write a program which accept N numbers from user and store it into List. Accept one another number from user and return
#  frequency of that number from List. 

def Frequency(List,No):
    
    Frequency = 0
    for i in range(0,len(List)):
        if(List[i] == No):
            Frequency = Frequency + 1
    return Frequency

def main():
    print("Enter number of elements : ",end=" ")
    Size = int(input())

    Array = list()

    print("Enter elements : ")
    for i in range(Size):
        No = int(input())

        Array.append(No)

    print("Enter the element that you want to search : ")
    Value = int(input())

    Ret = Frequency(Array,Value)

    print('Frequency of that elements is : ',Ret,end=" ")
if __name__ == "__main__":
    main()

    
# Test Case : 
# Input  : Number of elements : 11
# Input : 13  5  45  7  4  56  5  34  2  5  65
# Output : Frequency of that elements is : 3 