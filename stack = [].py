stack = []
while True:
    print("Choose the operation:")
    print("1.Push")
    print("2.Pop")
    print("3.Display")
    print("4.Exit")

    choice = input("Choose from 1~4: ")

    if choice == '1':
        item = input("Enter the item: ")
        stack.append(item)
        print(f"{item} has been pushed onto stack")

    elif choice == '2':
        if not stack:
            print("Stack is empty")
        else:
            popped = stack.pop()
            print(f"The {popped} is popped from the stack")

    elif choice == '3':
        if stack:
            print("Current Stack: ",)
            for i in reversed(stack):
                print("|", i)
            print("---------")
        else:
            print("stack is empty")

    elif choice == '4':
        print("Exiting.....")
        break

    else:
        print("Choose from 1~4")
    
        
        
