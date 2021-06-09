from tkinter import *
import random

names_list = []

global questions_answers
asked = []


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
        ''
       
       ] 
   
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
      
    







#***************Starting point of program******************#
randomiser()
if __name__ == "__main__":
  root = Tk()
  root.title("CSGO Quiz")
  quizStarter_object = QuizStarter(root)
  root.mainloop()#so the window doesn't disappear 
  
