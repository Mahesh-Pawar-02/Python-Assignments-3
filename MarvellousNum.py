# This user define module which is imported in Assignment3_5.py file

def ChkPrime(List):
    if List > 1 :
        for i in range(2, int(List**0.5) + 1):
            if(List % i == 0):
                return False
        else:
            return True
    else:
        return False