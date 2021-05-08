from tkinter import *
from functools import partial

class Question():
    def Answered(currentQuestion):
        # TODO: impliment checking of the answer

        # retrieves the hidden main window and destroys the question window
        root.deiconify()
        currentQuestion.destroy()
        
    def onButtonClick(i,j):
        #root.wm_title(str(i)+","+str(j))
        
        # checks that the previous question is taken
        if not(i==0 or Quiz.buttons[(i-1)*6+j]["state"]=="disabled"):
            return
        
        # disable the button that was pressed
        Quiz.buttons[i*6+j].config(state="disabled", bg="grey") #bg=background

        # hides the main window
        root.withdraw()

        # setups the question window
        question=Tk()
        question.geometry("300x200")
        question.wm_title(f"Question value: {(i+1)*400}")

        # TODO: Add question and four answer buttons
        answer = Button(master=question, text="Answer", command=lambda:Question.Answered(question))
        answer.pack()
        question.mainloop()

class Quiz:
    buttons = []
    def __init__(self):
       
        for i in range(5):
            root.rowconfigure( i, weight=1, minsize=25)

            for j in range(6):
                root.columnconfigure(j, weight=1, minsize=75)
    
                frame = Frame(
                    master=root,
                    relief=RAISED,
                    borderwidth=1
                    )
                frame.grid(row=i, column=j, sticky="nsew")
                button = Button(master=frame, text=str(400*(i+1)), padx=20, pady=5, command=partial(Question.onButtonClick, i, j))
                button.pack()
                self.buttons.append(button)

# initialize tkinter
root = Tk()

# set window title and resolution
root.wm_title("JEOPARDY!")
root.geometry("500x300")

# initializes a Quiz
app = Quiz()

# show window
root.mainloop()

