from tkinter import *

window = Tk()
window.title("Graphics Test")
window.geometry('1000x1000')
window.configure(bg = 'Sky blue')

insult=[" eats sh*t" , " is doo doo butter biscuit" ,
        " is a idotic psycopath who eats pants" ,
        " is a slimy farting turkish dragon" ,
        " is a ducknose shi*t goblin" ,
        " is a creepy shart hammer" ,
        " is a slutty butt clown" ,
        " is a stinky communist sh*t pirate" ,
        " is a pompus duck blossom" ,
        " is a jackalope ass hound" ,
        " is a butterface ass waffle" ,
        " is a smelly turd" ,
        " is a white trash nut monster" ,
        " is a insecure turd socket" ,
        " is a slimy pie eating bitch"
        ]

comment=[" Who asked your name?" ,
         " Are you dumb? Cause nobody cares about your name" ,
         "Shut up!"]

Nemo = PhotoImage(file = 'cursed nemo.png')
nemo = Label(bg = 'Sky blue' , image = Nemo)
nemo.place(x = 425 , y = 1)

Name = Entry(window , width = 30 , bg = 'Sky blue' , font = ('Little Comet Bubling Demo Version', 26))
Name.place(x = 1, y = 149)

def Insult():
    get = Name.get()

    import random
    q = random.choice(insult)
    r = random.choice(comment)

    result = Label(window  , text = get + q , width = 66 , justify = "left" , bg = 'Sky blue' , font = ('Little Comet Bubling Demo Version', 26))
    result.place(x = 1 , y = 650)

def Comment():

    import random
    q = random.choice(insult)
    r = random.choice(comment)

    result = Label(window  , text = r , width = 66 , justify = "left" , bg = 'Sky blue' , font = ('Little Comet Bubling Demo Version', 26))
    result.place(x = 1 , y = 650)

 
text = Label(window ,text = "Hello my name is Nemo :)" , bg = 'Sky blue' , font = ('Little Comet Bubling Demo Version', 26))
text.place(x =  1 , y = 1)

text2 = Label(window ,text = "Anyways, what is your name?" , bg = 'Sky blue' , font = ('Little Comet Bubling Demo Version', 26))
text2.place(x =  1 , y = 75)

import random

random_num1 = 42069
random_num2 = random.random()

if random_num1 > random_num2:
    button = Button(window , width = 10 , text = "Go" , command = Insult , bg = 'Sky blue' , font = ('Little Comet Bubling Demo Version', 26)) 
    button.place(x = 1 , y = 226)
else:
    button = Button(window , width = 10 , text = "Go" , command = Comment , bg = 'Sky blue' , font = ('Little Comet Bubling Demo Version', 26)) 
    button.place(x = 1 , y = 226)

window.mainloop()
