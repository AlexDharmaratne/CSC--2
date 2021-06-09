from tkinter import *
import random

names_list = []
global questions_answers
asked = []
score = 0


# Dictionary has key of number (for each question and number) and : the value for each is a list that has 7 items, so index 0 to 6
questions_answers = {
    1: ["Which team has the AK-47 on their buy menu? CT or T", # item 1, index 0 will be the question
        'CT (Counter Terrorist', # item 2, index 1 will be first choice
        'T (Terrorist)', # item 3, index 2 will be second choice
        'T (Terrorist)' #item 4, index 3 will be the right statement, we need to display the right statement if the user enters the wrong choice 
        ,2], # item 5, index 4 will be the position of the right answer (index where right answer sits), this will be our check if answer is correct or not
    2: ["How much does Armour cost?",
        '$400',
        '1000',
        '250',
        '750',
        '1000'
        ,2],
    3: ["Which of the following guns cost less than $3000?"
        'AK-47',
        'AWP',
        'M4A4',
        'SCAR-20',
        'AK-47'
        ,1],
    4: ["How many grenades are there in CSGO?",
        '2',
        '7',
        '5',
        '6',
        '6'  
        ,4],
    5: ["What does CSGO Stand for?",
        'Counter Strike Global Offense',
        'Conflicting Strike GLobal OFfenseive',
        'Counter Strike Global Offensive',
        'Conflicting Strike General Offensive',
        'Counter Strike Global Offensive'
        ,4],
    6:["How long does it take to defuse the bomb with a defuse kit?",
       '3 Seconds',
       '5 Seconds',
       '10 Seconds',
       '7 Seconds',
       '5 Seconds'
       ,2],
    7:["How many pistols are there in CSGO?",
       '6',
       '10',
       '9',
       '4',
       '9'
       ,3],
    8:["How long does it take to plant the bomb in CSGO",
       '5 Seconds',
       '2.5 Seconds',
       '4 Seconds',
       '6.5 Seconds',
       '4 Seconds'
       ,3],
    9:["When was CSGO Published?",
       '21 August 2012',
       '13 April 2005',
       '15 October 2008',
       '14 February 2002'
       '21 August 2012'
       ,1],
    10:["Whats the maximum amount of rounds played in a competitive match",
        '20',
        '30',
        '15',
        '25',
        '30'
        ,2],    
}

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        randomiser()      



class QuizStarter:
  def __init__(self, parent):
      background_color="blue"
      #frame set up
      self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
      self.quiz_frame.grid()

      #Label widget for our heading
      self.heading_label = Label (self.quiz_frame, text = "CSGO Quiz", font=("Tw Cen Mt", "18", "bold"), bg=background_color)
      self.heading_label.grid(row=0)

      #Label for user name prompt
      self.user_label = Label ( self.quiz_frame, text= "Please enter your name below", font=("Tw Cen MT", "16"), bg=background_color)
      self.user_label.grid(row=1, pady=20)

      #users input is taken by Entry Widget
      self.entry_box=Entry(self.quiz_frame)
      self.entry_box.grid(row=2, pady=20)

      #continue Button
      self.continue_button = Button (self.quiz_frame, text ="Continue", bg="pink", command=self.name_collection)
      self.continue_button.grid(row=3, pady=20)

  def name_collection(self):
      name = self.entry_box.get()
      names_list.append(name)
      print(names_list)
      self.quiz_frame.destroy()
      Quiz(root)


class Quiz:

    def __init__(self, parent):
      background_color = "grey30"
      self.quiz_frame = Frame(parent, bg = background_color, padx = 40, pady = 40)
      self.quiz_frame.grid()

      self.question_label = Label (self.quiz_frame, text = questions_answers[qnum][0], font = ("Tw cen MT", "15", "bold"), bg = background_color)
      self.question_label.grid(row = 0)

      self.var1=IntVar()

      self.rb1= Radiobutton(self.quiz_frame, text=questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1,padx=3,pady=3,                 variable=self.var1,   background = "grey")
      self.rb1.grid(row=2, sticky=W+E)

      self.rb2= Radiobutton(self.quiz_frame, text=questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2,padx=3,pady=3,                 variable=self.var1,   background = "grey")
      self.rb2.grid(row=3, sticky=W+E)

      self.rb3= Radiobutton(self.quiz_frame, text=questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3,padx=3,pady=3,                 variable=self.var1,   background = "grey")
      self.rb3.grid(row=4, sticky=W+E)

      self.rb4= Radiobutton(self.quiz_frame, text=questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4,padx=3,pady=3,                 variable=self.var1,   background = "grey")
      self.rb4.grid(row=5, sticky=W+E)

      self.quiz_instance= Button(self.quiz_frame, text="Confirm", font=("Helvetica", "13", "bold"), bg="grey")
      self.quiz_instance.grid(row=7, padx=5, pady=5)

      self.score_label=Label(self.quiz_frame, text="Score", font=("Tw Cen MT","16"), bg=background_color,)
      self.score_label.grid(row=8, padx=10, pady=1)


      
    




#***************Starting point of program******************#
randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("CSGO Quiz")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#so the window doesn't disappear 
  
