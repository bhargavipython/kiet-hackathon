score = 0
score = int(score)

#Ask user for their name
name = input("What is your name?")
name = name.title()
print("""Hello {}, welcome to Quiz night! 
You will be presented with 5 questions.
Enter the appropriate number to answer the question
Good luck!""".format(name))

#Question1
print("""when did virat kohli born?
1.  november 5
2.  December10
3.  december 24
4.  january13 """)

answer1 = "1"
response1 = input("Your answer is: ")

if (response1 != answer1):
    print("sorry this is not correct!")
else:
    print("well done, that is correct!")
    score = score + 1

print("Your current score is " + str(score) + " out of 6")

#Question2
print("""tripitakas are scared books of ?
1. buddhists
2. hindus
3. jains 
4. none of the above""")

answer2 = "1"
response2 = input("Your answer is:")

if (response2 != answer2):
    print("sorry this is not correct")
else:
    print("well done,this is correct")
    score = score + 1

print("Your current score is " + str(score) + " out of 6")

#Question3
print("""which is most senstive organ in our body?
1.brain  
2.skin
3.eyes  
4.tongue """)

answer3 = "2"
response3 = input("Your answer is:")

if (response3 != answer3):
    print("sorry this is not correct")
else:
    print("well done,this is correct")
    score = score + 1

print("Your current score is " + str(score) + " out of 6")

#Question4
print("""who invented ball point pen?
1. waterman brothers 
2. bicc brothers
3. wright brothers
4. biro brothers""")

answer4 = "4"
response4 = input("Your answer is:")

if (response4 != answer4):
    print("Sorry, that is incorrect")
else:
    print("well done,this is correct")
    score = score + 1

print("Your current score is " + str(score) + " out of 6")

#Question5
print("""3000*4000=
1. 12,000,000
2. 12,00,000
3. 12,000,00
4. 12,00,000   """)

answer5 = "1"
response5 = input("Your answer is:")

if (response5 != answer5):
    print("Sorry, that is incorrect!")
else:
    print("well done,this is correct")
    score = score + 1

 
#Question6
print("""if 1=3
    2=3
    3=5
    4=4
    5=4
    then 6=? 
1.2
2.3
3.4
4.5 """)
answer6 = "2"
response6 = input("Your answer is:")
if (response6 != answer6):
    print("Sorry, that is incorrect!")
else:
    print("well done,this is correct")
    score = score + 1
    
print("Your total score is " + str(score) + " out of 6")
print("Thank you for playing {}, goodbye!".format(name))
print("welldone,congrats")
print("correct answers")
print("1.1\n 2.1\n 3.2\n 4.4\n 5.1\n 6.2\n")

       
    




