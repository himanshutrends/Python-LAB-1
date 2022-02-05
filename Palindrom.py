while True:
    s=input("Enter somthing: ")

    y=s[::-1]

    print("Reversed String : "+y)
    if y==s:
        print("It is a Palindrom")
    else:
        print("Not a palindrom")