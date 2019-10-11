import random
print("hello user , welcome to the game.now u shall guess the number\nHINT:It's between 0 and 200")
x=random.randint(random.randint(0,100),random.randint(100,200))
p=5
while(p>0):
   if(p>1):
      n=input("you have "+str(p)+" turns left\n")
   else:
      n=input("Enter carefully ,this is your last chance\n")
   p-=1
   if(n==x):
      print("You win!")
      break
   if(int(p)>0):
      if(int(n)>int(x)):
         print("Try something lower than that")
      else:
         print("Try something higher than that")
   if(p==0):
      print("BETTER LUCK NEXT TIME!")
      f=input("press any key to exit")
