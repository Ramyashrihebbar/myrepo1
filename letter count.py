#Letter count app

print("Welcome to Letter Counting App ")

#input the name
name = input("\nWhat's your name Buddy : ").title().strip()
print("Hello,"+ name + "!")

print("I will help you to count the specific letter occurence in the messsage\n")
#write the message
sentence = input("Write the message : ")

letter= input("\nEnter the letter you would like to count : ")

sentence=sentence.lower()
letter=letter.lower()
No_count=sentence.count(letter)

print("\n{} is occured {} times".format(letter,No_count))      
      
      
