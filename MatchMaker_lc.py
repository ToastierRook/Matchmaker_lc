#Liam Cleary
#Computer Science
#Matchmaker

desiredResponse1=1
desiredResponse2=2
desiredResponse3=3
desiredResponse4=4
desiredResponse5=5


questionWeight1=1
questionWeight2=2
questionWeight3=3
questionWeight4=4
questionWeight5=5

print("") 
print("""
-------------------------------------------------------------------------
===============WELCOME TO LIAM'S MATCHMAKING EXTRAVAGANZA!===============
-------------------------------------------------------------------------
""")
print("")
print("")
print("""

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                        HOW COMPATIBLE ARE WE?
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
""")


#Functions
def Validate(response):
    ans = 0
    while not ans:
        try:
            ans = int(input("You select: "))
            if ans not in(1, 2, 3, 4, 5):
                raise ValueError
        except ValueError:
            ans = 0
            print("Please select a number between 1 - 5")

            
("""
---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
""")

userResponse1=input("Led Zeppelin is the greatest band of all time: ")

userResponse1=validate(userResponse1)
("""
---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
""")

userResponse2=input("vinyl records are fun to collect: ")

userResponse2=Validate(userResponse2)
("""
---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
""")
userResponse3=input("Dogs are better than cats: ")

userResponse3=Validate(userResponse3)
("""
---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
""")

userResponse4=input("very nice: ")

userResponse4=Validate(userResponse4)
("""
---------------------------------------------------------------------------
---------------------------------------------------------------------------
---------------------------------------------------------------------------
""")







