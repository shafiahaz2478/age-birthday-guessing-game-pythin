#this is the module that we imported
import time
from colored import fg 
import sys
import os


#this are the colours that presented in the output
for_main_screen=fg("red")
age=fg("blue")
age_born_yes=fg("cyan_2")
age_born_no=fg("blue_violet")
colour5=fg("red")
colour6=fg("white")
birthday=fg("yellow")
colour8=fg("blue")
colour9=fg("green")



# this is a welcome text
for x in (f"{for_main_screen}welcome to the age and birthday guessing game.\nI know that you have known these tricks but i just needed to make a programm of it and have fun \n \n"):
   sys.stdout.write(x)
   sys.stdout.flush()
   time.sleep(0.03)
	
time.sleep(0.5)

#this is the first question
for x in (f"{for_main_screen}which do i want to guess?age or birthday? \n>>> "):
  sys.stdout.write(x)
  sys.stdout.flush()
  time.sleep(0.03)

age_birthday=input()




if age_birthday == "age" or age_birthday == "age".upper:
  for x in ((f"\n\n{age}pick a number from 1 to 10 \n>>> ")):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

  number_picking= int(input())
  for x in (f"\n\n{age}i am going to multiply the number which you picked by 2 \nmultiplying by 2........\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

  
  multiplied = int(number_picking * 2)
  print(multiplied , "\n\n")
  time.sleep(1)
  for x in ("now i am going to add 5 to the number\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)


  adding= int(multiplied + 5)
  print(adding , "\n\n")
  time.sleep(1)
  for x in ("now i will times the number by 50\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)



  multiplying_fifty= int( adding * 50)
  print(multiplying_fifty , "\n\n")
  for x in ("have you had your birthday this year?(yes/no) \n>>> "):
     sys.stdout.write(x)
     sys.stdout.flush()
     time.sleep(0.03)


  born_year=input()
  if born_year=="yes":

    for x in (f"\n\n{age_born_yes}which is the year you were born \n>>> "):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)


    a=input()
    
    year=int(a)

    for x in (f"\n\n{age_born_yes}as you had your birthday i will add 1770 to the answer \nadding 1770\n\n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)



    time.sleep(2)
    adding_seventy=int(1770 + multiplying_fifty)


    for x in (f"now i will subtract the ans by your year of birth  {year} \nsubtracting........\n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)

    
    time.sleep (2)
    subracted = int(adding_seventy - year)
    subracted_of_string = str(subracted)
    for x in (subracted_of_string , "\n\n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)


    for x in (f"the first digit of the number is the number you picked and the last two digits is your age \n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)
    exit
    
  elif born_year=="no":
   
    for x in (f"\n\n{age_born_no}which is the year you were born \n>>> "):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)


    a=input()
    
    year=int(a)

    for x in (f"\n\nas you had your birthday i will add 1769 to the answer \nadding 1769\n\n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)



    time.sleep(2)
    adding_seventy=int(1769 + multiplying_fifty)


    for x in (f"now i will subtract the ans by your year of birth  {year} \nsubtracting........\n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)

    
    time.sleep (2)
    subracted = int(adding_seventy - year)
    subracted_of_string = str(subracted)
    for x in (subracted_of_string , "\n\n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)


    for x in (f"the first digit of the number is the number you picked and the last two digits is your age \n"):
      sys.stdout.write(x)
      sys.stdout.flush()
      time.sleep(0.03)
    exit
    
    


    
elif age_birthday=="birthday":

  for x in (f"{birthday}what is the date of your birth.like 16th in january\n>>> "):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)


  date_asking=int(input())

  print("\n")

  for x in ("now im going to multiply your birthdate by 2 \n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

  time.sleep(1)
  multiply_birthdate= date_asking * 2
  print(multiply_birthdate ,  "\n\n")
  
  for x in ("now i am going to add 5 to your birthdate \n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

  time.sleep(1)
  adding_birthdate5= multiply_birthdate + 5
  print(adding_birthdate5, "\n\n")

  for x in ("now i am going to multiply the number by 50\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

    

  fifty_multiply=50 * adding_birthdate5
    
  

  for x in ("multiplying.......\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

  time.sleep (2)


  for x in (f"{fifty_multiply}\n\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

  

  for x in ("what is the number of the month you were born?\n>>> "):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)

  asking_month2=input()

  print("\n")

  asking_month= int(asking_month2)

  

  c = fifty_multiply+asking_month
  
  for x in (f"Now I am going to add the number of month to the answer\n{c}\n\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)
    

  for x in ("Finally, I am going to subtract 250 from the answer\n\n"):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.03)
  print(c)
  result = c - 250
  for x in ( f"The answer is {result}.\n\nThe first one/two digits in the three/four digit number is/are the date of you birthday\n\nThe last two digits are the month of your birthday \n"):
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.03)

  exit   

exit