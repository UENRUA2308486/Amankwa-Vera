# Self Multiplication of a Number
def self_multiplication():
    number = float(input("Enter a number: "))
    times = int(input("How many times do you want to multiply it by itself? "))
    
    result = number
    for _ in range(1, times):
        result *= number
        print(f"Current result after multiplying by {number}: {result}")

    print(f"Final result after {times} multiplications: {result}")

self_multiplication()
