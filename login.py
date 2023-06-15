UserName="OMEGA_APHACO"
password="starlord1"
count=0
while count<4:
    UserName=input("enter your user name: ")
    password=input("enter your password: ")
    if UserName=="OMEGA_APHACO"and password=="starlord1":
        print("LOGIN SUCCESSFUL")
        break
    elif count==3:
        print("TOO MANY FAILED ATTMPTS TRY LOGGINNG IN AGAIN IN 10 MINUTES")
        break
    else:
        print("WRONG USERNAME OR PASSWORD")
        count+=1
        
