print("ENTER THE STARTING DATE:--")
date=int(input("Enter the date:"))
month=int(input("Enter the Month:"))
a=int(input("Enter the Year:"))

print("ENTER THE ENDING DATE:--")
DATE=int(input("Enter the date:"))
MONTH=int(input("Enter the Month:"))
b=int(input("Enter the Year:"))

print(f"({date}/{month}/{a})",end=" to ")
print(f"({DATE}/{MONTH}/{b})")

leap=[]
n_leap=[]
for i in range(a,b+1):
    if i%4==0 and i%100!=0:
        leap.append(i)
    elif i%100==0 and i%400==0:
        leap.append(i)
    else:
        n_leap.append(i)
print("\n")
print("Leap Year Are:")
print("\n")
print(*leap,sep=",")
print("\n")
print("Non Leap Year Are:")
print("\n")
print(*n_leap,sep=",")
