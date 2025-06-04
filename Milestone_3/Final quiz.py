import random
good_comments=["Way to go","Keep it up", "Fantastic"]
bad_commemts=["Keep trying","Maybe next time", "Don't give up"]#Comments
#Questions and answers list
QUESTION=["Australia","India","Scotland","Canada","Brazil","South Korea","Finland","Chile","China","USA"]
OPTIONS=[["Adelaide","Canberra","Melbourne","Sydney"],
        ["Chennai","New Delhi","Kolkata","Mumbai"],
        ["Edinburgh", "Glasgow", "Dundee", "Aberdeen"],
        ["Toronto","Vancouver","Ottawa","Montreal"],
        ["Rio de Janeiro","São Paulo","Brasília","Buenos Aires"],
        ["Seoul","Tokyo","Hong Kong","Beijing"],
        ["Helsinki","Stockholm","Oslo","Copenhagen"],
        ["Buenos Aires","Santiago","Lima","Bogotá"],
        ["Shanghai","Beijing","Guangzhou","Hong Kong"],
        ["New York City","Los Angeles","Washington, D.C.","Chicago"]]
SHORT_OPTIONS=["a","b","c","d"]
ANSWERS=[1,1,0,2,2,0,0,1,1,2]

play="yes"
score=0
correctly_answered_times=0
#Ask user their name
name=input("Please enter your name before you get started.    -:")
#Greet te user and introduce the game
print("Hello", name, "welcome to this quiz")
print("This quiz is about capital cities in the world")
note="This quiz is totally based on multiple choice questions so when you select the answer please try type the letter of the option (eg: A or B or C or D), otherwise, you would make some mistakes when you spell the answer"
print("{}".format(note))
while True:
    note1=input("Please note that you should avoid from entering any of your personal data or any other data that you think is private. \nPlease enter \"A\" to say that you understand this.").lower()
    if note1=="a":
        break
    else:
        print("You must type \"A\" to continue")
while play=="yes":
    while True:
        try:
            tries=int(input("How many attempts do you need for each question? Maximum is 3   -:"))
            if 1<= tries <=3:
                break
            else:
                print("The number that you entered should be a number between 1 and 3")
        except:
            print("Please enter a valid number")
#Ask the user questions
    correctly_answered_times=0
    score=0
    for i in range (len(QUESTION)):
        question_attempts=tries
        score_increment=3
        while question_attempts>0:
            answer=input("What is the capital of {}?(a/b/c/d)\nA.{}  B.{}  C.{}  D.{} -:\n".format(QUESTION[i],OPTIONS[i][0],OPTIONS[i][1],OPTIONS[i][2],OPTIONS[i][3])).lower()
            correct_answer=OPTIONS[i][ANSWERS[i]].lower()
            if answer in SHORT_OPTIONS:
                selected_answer=OPTIONS[i][SHORT_OPTIONS.index(answer)]
                if selected_answer.lower()==correct_answer:
                    print("You are correct")
                    score+=score_increment
                    print("You are correct, got {} points added into the total and the current total is {}".format(score_increment,score))
                    print(random.choice(good_comments))
                    break
                else:
                    print("You are wrong")
                    print(random.choice(bad_commemts))
                    score_increment=max(1,score_increment-1)
                    question_attempts-=1
                    print("you have {} attempts left".format(question_attempts))
            elif answer in [opt.lower() for opt in OPTIONS[i]]:
                if answer==correct_answer:
                    print("You are correct")
                    score+=score_increment
                    correctly_answered_times+=1
                    print("You are correct, got {} points added into the total and the current total is {}".format(score_increment,score))
                    print(random.choice(good_comments))
                    break
                else:
                    print("You are wrong")
                    print(random.choice(bad_commemts))
                    score_increment=max(1,score_increment-1)
                    question_attempts-=1
                    print("you have {} attempts left".format(question_attempts))
            else:
                print("That wasn't an option.Choose a valid answer.")
        if question_attempts==0:
            print("you got 0 attempts left. The answer is ",correct_answer,)
    #End the quiz
    print("This is the end of this quiz thank you for attempting this quiz")
    def final_score(sc):
        if score < 11:        
            print(f"You need some improvements {name}, your score is only {score} out of 30 and you have answered correctly for {correctly_answered_times} questions out of {len(QUESTION)}")
        elif score < 16:
            print(f"Well try, the score is {score} out of 30 and you have answered correctly for {correctly_answered_times} questions out of {len(QUESTION)}")
        elif score < 24:
            print(f"Great job, the score is {score} out of 30 and you have answered correctly for {correctly_answered_times} questions out of {len(QUESTION)}")
        elif score >= 24:
            print(f"Excellent work, the score is {score} out of 30 and you have answered correctly for {correctly_answered_times} questions out of {len(QUESTION)}")
    final_score(score)
    while True:
        play=input("Do you want to play again? (Yes/No):").lower()
        if play in ["yes","no"]:
            break
        else:
            print("Please enter yes or no")
print("Thanks for playing")