import random,sys,time,random,mysql.connector
finalscore=0
def printt(message):
    for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0)    
            if char=="\n":
                time.sleep(0)
            else:
                time.sleep(0)
def dif():
    global dic,name
    dic={1:"Hard",2:"Moderate",3:"Easy"}
    while True:
        global lives,difficulty,finalscore,name
        lives=0
        while True:
            try:
                difficulty=int(input("\nGame Console: Choose your difficulty:\n3:Easy\n2:Moderate\n1:Hard\n"))
                break
            except:
                print("Game Console: Oops! Invalid Entry, Issue: ", sys.exc_info()[0])
        if difficulty<=3:
            print("Game Console: You have chosen: ",dic[difficulty]," mode")
            if difficulty==3:
                lives=3
                printt("\nYour Chaperone 0_0: You have 3 chances use it cautiously\n\n")
                break
            elif difficulty==2:
                lives=2
                printt("\nYour Chaperone 0_0: You have 2 chances use it cautiously\n\n")
                break
            elif difficulty==1:
                lives=1
                printt("\nYour Chaperone 0_0: You have 1 chance use it cautiously\n\n")
                break
        else:
            printt("Your Chaperone 0_0: Invalid Number Please Pick A Number Between 1 to 3\n")
def gamecode():
    printt("Please Enter The Name Of Your Character: ")
    global finalscore,difficulty,name
    name=input()
    print(name,end="")
    with open("Game Console.txt") as file:
        for i in file:
            printt(i)
    file.close()
    dif()
    exitscreen=""
    level1()
    if finalscore>=0:
        level2()
    elif finalscore>=20:
        level3()
    else:
        printt("Game Console: You didnt pass the level, you get trapped in the dungeon with your chaperone and the princess...\n")
        printt("Game Console: You shall soon be the dragon supper say goodbye!\n\nGAME OVER...\n\n")
        printt("Game Console: YOUR SCORE IS: ")
        print(finalscore,"\n\n")
        exitscreen==input("Game Console: Press Enter To Quit This Screen.")
        printt("Thank you for playing.\nYour score will be recorded on our leaderboard.\n")
        printt("Until next time, ")
        print(name)
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="system")
    mycursor = mydb.cursor()
    mycursor.execute("use leaderboard;")
    if difficulty==3:
        sql="insert into scores(USERNAME,SCORE,DIFFICULTY)values(%s,%s,%s);"
        values=(name,str(finalscore),"Easy")
        mycursor.execute(sql,values)
        mydb.commit()
    elif difficulty==2:
        sql="insert into scores(USERNAME,SCORE,DIFFICULTY)values(%s,%s,%s);"
        values=(name,str(finalscore),"Intermediate")
        mycursor.execute(sql,values)
        mydb.commit()
    elif difficulty==1:
        sql="insert into scores(USERNAME,SCORE,DIFFICULTY)values(%s,%s,%s);"
        values=(name,str(finalscore),"Hard")
        mycursor.execute(sql,values)
        mydb.commit()
    time.sleep(2)
    menuscreen()
def level1():
    global finalscore,difficulty,name
    rand1=0
    rand2=0
    ans1=0
    realans1=0
    realans2=0
    ans2=0
    realans3=0
    ans3=0
    rand3=0
    printt("Monster 1: Dr. Linear Equation...\n\n")
    printt("Your Chaperone 0_0: Dr. Linear Equation tests your addition skills\n")
    print(name,end="")
    printt(", These are the number of chances you shall recieve: ")
    print(difficulty,"\n")
    global lives
    while lives!=0:
        rand1=random.randint(0,9)
        rand2=random.randint(0,9)
        realans1=rand1+rand2
        printt("Question 1:\n")
        print(rand1,"+",rand2,"=",end="")
        while True:
                try:
                    ans1=int(input())
                    break
                except:
                    print("Oops! Invalid Entry, Error:",sys.exc_info()[0])
                    print(rand1,"+",rand2,"=",end="")
        if realans1== ans1:
            printt("\n\nDr. Linear Equation X_0 :Tsk you're not as bad as you look after all\nYou wont get this one right!\n\n")
            finalscore+=10
            rand1=random.randint(0,99)
            rand2=random.randint(0,99)
            realans2=rand1+rand2
            printt("Question 2:\n")
            print(rand1,"+",rand2,"=",end="")
            while True:
                try:
                    ans2=int(input())
                    break
                except:
                    print("Oops! Invalid Entry, Error:",sys.exc_info()[0])
                    print(rand1,"+",rand2,"=",end="")
        else:
            printt("\n\nDr. Linear Equation XD :AHAH! WRONG ANSWER!\n\n")
            lives=lives-1
            print("Game Console: Remaning chances:",lives,"\n")
            finalscore-=5
            continue
        if realans2==ans2:
            printt("\n\nDr. Linear Equation -_- :That's right ppfft but I'll let you take the little pickings (͠° ͟ʖ ͡°)\nI'll ask you a question that will not bring you back to this place!\n\n")
            finalscore+=10
            rand1=random.randint(0,99)
            rand2=random.randint(0,99)
            rand3=random.randint(0,99)
            printt("Question 3:\n")
            print(rand1,"+",rand2,"-",rand3,"=",end="")
            realans3=rand1+rand2-rand3
            while True:
                try:
                    ans3=int(input())
                    break
                except:
                    print("Oops! Invalid Entry, Error:",sys.exc_info()[0])
                    print(rand1,"+",rand2,"-",rand3,"=",end="")
        else:
             printt("\n")
             lives=lives-1
             printt("Dr. Linear Equation XD : YOU GOT NOTHING ON THIS PH.D, YOU GOT IT WRONG! ¬ヘ(^∀ ^ )\n\n")
             print("Game Console: Remaning chances:",lives,"\n")
             finalscore-=5
             continue
        if realans3==ans3:
               printt("Dr. Linear Equation >_< : NOOOOO! YOU'RE BETTER THAN ME, UM- THE EXIT IS THAT WAY(⌒_⌒;)\n\n*CONGRATS YOU EMBARRASED THE LINEAR EQUATION MONSTER*\n\n")
               finalscore+=10
               printt("*You now walk towards the exit, a door opens... You walk through a long corridor while you hear a crowd of people,\n")
               printt("You come out the end of the long corridor and what-... YOU'RE IN THE COLOSSEUM!*\n\n")
               break
        else:
            printt("Dr. Linear Equation XD: WHAT A SHAME, YOU AIN'T AS GOOD AS THIS PH.D! ¬ヘ(^∀ ^ )\n")
            lives=lives-1
            if lives!=0:
                printt("Game Console: You will now be taken back to Round 1 with your score reset to 0.\nYou also lose one of your chances. ")
            print("Game Console: Remaning chances:",lives)
            finalscore=0
            continue
    if lives==0:
        printt("Dr. Linear Equation XD: YOU'RE DONE FOR. YOU GOT THAT WRONG.\n\n")
def level2():
    global finalscore,difficulty,name
    print (finalscore)
    printt("\nMonster 2: Mr. Julius Caesar...\n\n")
    a=input("Your Chaperone ^_^: Enter i if you want to see the instructions to Roman Numerals\nPress Enter to skip hint\n")
    if (a=="I" or a=="i")and difficulty>1 :
        with open("Roman Numeral Instructions.txt")as file2: 
            for i in file2:
                printt(i)
        file2.close()
    else:
        printt("Game Console: You chose hard mode XD, No hint for real warriors.\n")
    def roman(romanvalue):
        global finalscore,difficulty,name
        Romanletters = [
            (1000,'M'),
            (900,'CM'),
            (500,'D'),
            (400,'CD'),
            (100,'C'),
            (90,'XC'),
            (50,'L'),
            (40,'XL'),
            (10,'X'),
            (9,'IX'),
            (5,'V'),
            (4,'IV'),
            (1,'I')]
        res=''
        for (num, roman) in Romanletters:
            a= (int)(romanvalue/num)
            b= (int)(romanvalue%num)
            (c, romanvalue)=(a,b)
            res+=roman*c
        return res
    for i in range(0,3):
        Question=random.randint(1,4000)
        ComputerAnswer=roman(Question)
        print("\nRound ",i+1,": ",Question,"\n")
        Answer=input("Julius Caesar @_@ : This one is hard!\nEnter your answer in Roman Numerals:\n")
        if ComputerAnswer == Answer:
            if i!=2:
                printt("Julius Caesar @_@: AGH! I UNDERESTIMATED YOU, YOU WONT GET ANOTHER ONE!\n")
                finalscore+=10
            else:
                printt("Julius Caesar ~>_<~: YOU BEAT ME IN MY OWN STADIUM! CURSE YOU! THE EXECUTIONER WILL SURELY STOP YOU!\n\n")
                finalscore+=10
                level3()
        elif ComputerAnswer != Answer:
            printt("Julius Caesar X): AH HA! WRONG ANSWER! GO HOME TO GRANDMA! XP\n\n")
            if difficulty==1:
                finalscore-=9
            elif difficulty==2:
                finalscore-=7
                a=input("Game Console: Enter H for a hint, press any other key to continue\n")
                if a=="H" or a=="h":
                    printt("Hint:")
                    print("1000=M\n900=CM\n500=D\n400=CD\n100=C\n90=XC\n50=L\n40=XL\n10=X\n9=IX\n5=V\n4=IV\n1=I")
                else:
                    continue
            elif difficulty==3:
                finalscore-=5
                a=input("Enter H for a hint, press any other key to continue:\n")
                if a=="H" or a=="h":
                    printt("Hint:")
                    print("1000=M\n900=CM\n500=D\n400=CD\n100=C\n90=XC\n50=L\n40=XL\n10=X\n9=IX\n5=V\n4=IV\n1=I")
                else:
                    continue
def level3():
    global finalscore,difficulty,name
    print(finalscore)
    printt("\nLevel 3: The Executioner...\n\n")
    a=input("Your Chaperone ^_^: Enter i if you want to see the instructions to Hangman\n")
    if a=="i" or a=="I":
        with open("Hangman Instructions.txt") as file3:
            for i in file3:
                printt(i)
        file3.close()
        c=0
    else:
        c=0
        def hangman():
            global finalscore
            with open("Hangman Word Pool.txt") as f:
                word_list=f.read().split()
            choice = random.choice(word_list)
            choice_upper = choice.upper()
            guessed = False
            guessed_letters = []
            guessed_words = []
            tries = 6
            printt("Executioner T_T: Ready to play Hangman round ")
            print(c+1,end="")
            printt("?\n")
            def hangman_display(tries):
                stages = [  # final state: head, torso, both arms, and both legs
                    """
                        ______
                       |      |
                       |      O
                       |    \|/
                       |      |
                     _|_   / \
                    """,
                    # head, torso, both arms, and one leg
                    """
                        ______
                       |      |
                       |      O
                       |    \|/
                       |      |
                     _|_  /
                    """,
                    # head, torso, and both arms
                    """
                        ______
                       |      |
                       |      O
                       |    \|/
                       |      |
                     _|_
                    """,
                    # head, torso, and one arm
                    """
                        ______
                       |      |
                       |      O
                       |    \|
                       |      |
                     _|_
                    """,
                    # head and torso
                    """
                        ______
                       |      |
                       |      O
                       |      |
                       |      |
                     _|_
                    """,
                    # head
                    """
                        ______
                       |      |
                       |      O
                       |
                       |
                     _|_   
                    """,
                    # initial empty state
                    """
                        ______
                       |      |
                       |
                       |
                       |
                     _|_
                    """
                ]
                return stages[tries]
            underscores = "_" * len(choice_upper)
            printt(hangman_display(tries))
            print("_ " * len(choice_upper))
            underscore_change = list(underscores)
            while not guessed and tries > 0:
                guess = input("\nGame Console: Enter a letter or a word\n")  # user guess
                guess_upper = guess.upper()  # guess in upper to prevent errors
                if len(guess) == 1 and guess_upper.isalpha():  # if letter
                    '''
                    error handling if guess length is 1 it is a digit 
                    or alpha and isalpha checks for simply alpha
                    '''
                    if guess_upper in guessed_letters:
                        printt("Game Console: You have already guessed the letter:")
                        print(guess_upper,"\n")

                    elif guess_upper not in choice_upper:
                        tries = tries - 1
                        guessed_letters.append(guess_upper)
                        print("Your Chaperone 0_0: Oh no!",'"{}"'.format(guess),"is not in the word!\n")

                    else:  # final option- correct guess
                        print("Your Chaperone :D : Good job!", guess_upper, " is in the word!")
                        guessed_letters.append(guess_upper)
                        placeholder = []
                        index=-1
                        for i in choice_upper:
                            index=index+1
                            if guess_upper == i:
                                placeholder.append(guess_upper)
                            else:
                                placeholder.append(underscore_change[index])

                        underscores = ' '.join(placeholder)
                        printt(underscores)
                        underscore_change = placeholder
                        if placeholder  == list(choice_upper) :
                                guessed = True
               #I have to change this logic , loop will never end otherwise
                elif len(guess) > 1 and guess.isalpha():
                    if guess_upper in guessed_words:
                        printt("Your Chaperone T_T: You already guessed that word!\n")
                        printt(underscores)
                    elif guess_upper != choice_upper:
                        print("The Executioner XD: ",guess," is not the word!\n")
                        guessed_words.append(guess.upper())
                        tries = tries - 1
                    else:
                        guessed = True
                        underscores = choice_upper
                    print(" ".join(underscores))
                else:
                    tries = tries -1
                    printt("The Excutioner: Trying to be smart about this EH!?, THAT IS INVALID.")
                if guessed==True:
                    print("Congrats you completed round ", c+1,"\n")
                    printt("Well done you got this word!")
                    break
                else:
                    printt("\n\nThe number of tries you have left: ")
                    print(tries,"\n")
                    print(hangman_display(tries))
            #guess over display where the user is at right now
            if guessed==False:
                printt("Oh no! You lost this round!\n\n")
                if difficulty==1:
                    finalscore-=9
                elif difficulty==2:
                    finalscore-=7
                elif difficulty==3:
                    finalscore-=5
            else:
                if c==0:
                    printt("The Exectutioner: 0_0 You won this round, I shall spare your chaparone.\n*Your chaparone is released*\n\n")
                    finalscore+=10
                if c==1:
                    printt("The Exectutioner: 0_X You won this round, you are spared\n*You are released*\n\n")
                    finalscore+=10
                if c==2:
                    printt("The Exectutioner: X_X You won the last round round, You have defeated me, the princess is now free.\n*The princess is released*\n\n")
                    finalscore+=10
        while c<3:
            hangman()
            c=c+1
        else:
            print("Congragulations! You beat the 3 monsters  and rescued the princess")
            a==input("Game Console: Press Enter To Quit This Screen.")
            printt("Thank you for playing your score will be recorded on our leaderboard.")
            printt("Until next time,")
            print(name)
def leaderboardview():
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="system")
    mycursor=mydb.cursor()
    printt("1 - Show Entire Leaderboard\n2 - Show Highest Scores\n3 - Back to Main Menu\n")
    a=int(input())
    if a==1:
        mycursor.execute("use leaderboard;")
        mycursor.execute("select * from scores")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        menuscreen()
    elif a==2:
        mycursor.execute("use leaderboard;")
        printt("\n1 - Show Highscores for Hard Mode\n2 - Show Highscores for Intermediate Mode\n3 - Show Highscores for Easy Mode\n4 - Quit to Main Menu\n")
        try:
            b=int(input())
            if b==1:
                mycursor.execute("""select * from scores where DIFFICULTY="Hard" order by SCORE desc;""")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print("\n")
                menuscreen()
            elif b==2:
                mycursor.execute("""select * from scores where DIFFICULTY="Intermediate" order by SCORE desc;""")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print("\n")
                menuscreen()
            elif b==3:
                mycursor.execute("""select * from scores where DIFFICULTY="Easy" order by SCORE desc;""")
                myresult = mycursor.fetchall()
                for x in myresult:
                    print(x)
                print("\n")
                menuscreen()
        except:
            print("Invalid Entry, Error:",sys.exc_info()[0])
    elif a==3:
        menuscreen()
def menuscreen():
    printt("---------------------------------------------\nCoolMathGames.com\n\nMain Menu:\n\n")
    print("1 - Play game\n2 - Leaderboard View\n3 - Quit Game\n")
    while True:
        try:
            z=int(input())
            break
        except:
            print("Invalid Entry, Error:",sys.exc_info()[0])
    if z==1:
        gamecode()
    elif z==2:
        leaderboardview()
    elif z==3:
        quit()
name=""
menuscreen()
