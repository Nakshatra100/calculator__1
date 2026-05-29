try:
    a=int(input("enter number 1:"))
    b=int(input("enter number 2:"))
    print("enter (+) to add\nenter (-) to subtract\nenter (*) to multiply\nenter (/) to divide")
    o=input("enter the operation to perform:")

    match o:
        case "+":
            print(f"addition ={a+b}")
        case "-":
            print(f"Subtraction ={a-b}")
        case "*":
            print(f"Multiplication ={a*b}")
        case "/":
            if b == 0:
                print("error: cannot divide by zero")
            else:
                print(f"division = {a / b}")
            


except ValueError:
    print("please enter a valid number")

     
