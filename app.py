from flask import Flask, request, render_template
import random

# Global variable:
# answer for the guessing game
answer = random.randint(1,1000)

# counting how many times you guess
count = 0

# higher bound for the game
higher_bound = 1000

# low bound for the game
lower_bound = 0

app = Flask(__name__)

@app.route('/')
def my_form():
    # This will be the name of html file
    return render_template("number.html")

@app.route('/', methods = ['POST'])
def my_post():
    global answer
    global count
    global higher_bound
    global lower_bound

    # print out message
    msg1 = ''
    msg2 = ''
    
    # if trial time is lower than 10, keep 
    if count < 10:

        # get the input from user
        text1 = request.form['text1']
        text1 = int(text1)
        
        # if the text is larger or smaller than bound, pop up the error message
        if text1 > higher_bound:
            msg1 = 'valid number is '+ str(lower_bound) + ' ~ '+ str(higher_bound)+'.'
            msg2 = 'Your input: '+ str(text1) +' is too large.'
            return render_template("number.html",msg1=msg1,msg2 = msg2)
        elif text1 < lower_bound:
            msg1 = 'valid number is '+ str(lower_bound) + ' ~ '+ str(higher_bound)+'.'
            msg2 = 'Your input: '+ str(text1) +' is too small.'
            return render_template("number.html",msg1=msg1,msg2 = msg2)
        else:


            count = count + 1
            # chance is for how many chances user can try
            chance = 10 - count 

            # if the input is not correct but in the bound, the message will give hint and 
            # tell user that how many chances they have
            if text1 < answer:
                lower_bound = text1
                msg1 = 'Your guess is too low. Guess from '+str(lower_bound)+' to '+str(higher_bound)
                msg2 = 'You have '+str(chance)+' chances.'
                return render_template("number.html",msg1=msg1,msg2 = msg2)

            elif text1>answer:
                higher_bound = text1
                msg1 = 'Your guess is too high. Guess from '+str(lower_bound)+' to '+str(higher_bound)
                msg2 = 'You have '+str(chance)+' chances.'
                return render_template("number.html",msg1=msg1,msg2 = msg2)
            else:
                # if the user get the correct answer, the message will tell you how many chances you use
                msg1 = 'Congratulation!!!!!'
                msg2 = 'You got correct number '+str(answer)+' in '+str(count)+' guesses.'
                count= 0 
                answer = random.randint(1,1000)
                higher_bound = 1000
                lower_bound = 0
                return render_template("number.html",msg1=msg1,msg2 = msg2)

    # if you don't get the answer within 10 trial, the message will told you the correct answer
    else:
        num = 'Oops! The correct number is '+str(answer)
        count= 0 
        answer = random.randint(1,1000)
        higher_bound = 1000
        lower_bound = 0
        return render_template("number.html",num = num)

if __name__ == '__main__':
    app.run()