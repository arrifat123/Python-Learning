username = "root"
pas = "admin"

print("U r going to input username ")
name = input("Enter your name :")
print("You are supposed to enter password ")
password = input("Enter your password :")

if name == username and password == pas :
    print(f"Welcome Back!")

else :
    print(f"Ahh! U mesed something up. Try again.")