a=input("enter age")

if int(a) < 18:
    print(f"{a} is not eligible to vote")

elif int(a) >= 18:
    b=input('do you have voter id?')
    if b=="yes" or b=="Yes":
        print(f"{a} is eligilbe to vote")
    else:
        print(f"{a} is not eligible")



