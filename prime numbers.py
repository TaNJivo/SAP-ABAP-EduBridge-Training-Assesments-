def prime_number(num):
    cat = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cat += 1
    if cat == 2:
        print("It is a prime number")
    else:
        print("it is not a prime number")

num = int(input("Enter the number: "))
prime_number(num)
   
    
    