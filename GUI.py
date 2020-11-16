from guizero import App,Text,ButtonGroup,PushButton,TextBox		#https://pypi.org/project/guizero/
from datetime import date, datetime
from time import sleep

app = App(title="Mira", layout="grid",bg="black",height=1024,width=600)
#app.full_screen = True

#Date and Time
today = date.today()
today_date = today.strftime("%B %d, %Y")
now = datetime.now()
now_conv = now.strftime("%I:%M:%S")
curr_time = now_conv
Date_display = Text(app, today_date, size=30, font="Century Gothic Bold", color="light gray", grid=[0,0],align="left")
Time_display = Text(app, curr_time, size=40, font="Century Gothic Bold", color="light gray", grid=[0,1],align="left")
def time_get():
    now = datetime.now()
    now_conv = now.strftime("%I:%M:%S")
    Time_display.value = now_conv

#To-do List
To_do_list_Title = Text(app, "To-do List:", size=20, color="light gray", grid=[0,2],align="left")


Todolist=[]
Selectedlist=[]

global Display_list
Display_list = ButtonGroup(app, options=Todolist, selected=Selectedlist, align="left", grid=[0,3])
Display_list.text_color="light gray"
Display_list.text_size=20
Display_list.font="Century Gothic Bold"    

def clear_todolist():
    global Display_list
    for i in Todolist:
        Display_list.remove(i)
    Display_list.destroy()
    Todolist.clear()
    create_list()
def create_list():
    global Display_list
    Display_list = ButtonGroup(app, options=Todolist, selected=Selectedlist, align="left", grid=[0,3])
    Display_list.text_color="light gray"
    Display_list.text_size=20
    Display_list.font="Century Gothic Bold"

#print(Display_list.options)

Add_textbox=TextBox(app,grid=[0,4],width=30,align="left")
Add_textbox.text_size=12
Add_textbox.text_color="Black"
Add_textbox.font="Century Gothic Bold"
Add_textbox.bg="white"
def addto_todolist():
    global Display_list
    if(Add_textbox.value):
        Todolist.append(Add_textbox.value)
        Display_list.append(Add_textbox.value)
        print(Todolist)
        Add_textbox.clear()
Addbutton = PushButton(app, command=addto_todolist, text="Add", grid=[0,4], align="right")
Addbutton.text_color="Black"
Addbutton.bg="light gray"
Addbutton.font="Century Gothic Bold"
Addbutton.text_size="12"


Clearbutton = PushButton(app, command=clear_todolist, text="Clear", grid=[0,5], align="left")
Clearbutton.text_color="Black"
Clearbutton.bg="light gray"
Clearbutton.font="Century Gothic Bold"
Clearbutton.text_size="12"


    
Time_display.repeat(1000, time_get)
app.display()
