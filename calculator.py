def add(a,b):
    return a + b

def subtract(a,b):
    return a - b 

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
def main():
    a = 10
    b = 5
    print("Python calculator")
    print("first Number:", a)
    print("second Number:", b)
    print("Addition:",add(a,b))
    print("subtract:",subtract(a,b))
    print("multiply:",multiply(a,b))
    print("divide:",divide(a,b))

if __name__ == "__main__":
    main()
        
        
        
    

