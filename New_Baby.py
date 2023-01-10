from guizero import App, Window, PushButton, Picture, Text, TextBox, Box

babies = []
bby1_temp = []
bby2_temp = []
baby_num = 0

#below is the menu for the application it uses a grid
#layout and pushbuttons to direct the user to the right window
def menu():
    button_new = PushButton(app, grid=[0,0], command=new_baby, height=5, width=12, text="Add new baby")
    name_label = Text(app, text="Add New baby", grid=[0,1], font="catamaran")
    button_new = PushButton(app, grid=[0,2], command=baby, height=5, width=12)
    button_new.bg = "lightblue"
    name_label = Text(app, text="Babies", grid=[0,3], font="catamaran")
    button_new = PushButton(app, grid=[1,0], command=data_entry, height=5, width=12, text="Data entry")
    name_label = Text(app, text="Enter temperature", grid=[1,1], font="catamaran")
    button_new = PushButton(app, grid=[1,2], height=5, width=12, text="Statistics", command=statistics)
    name_label = Text(app, text="Statistics", grid=[1,3], font="catamaran")

def new_baby():
    global baby_num, babies
    #in this window the save function saves the information in a dictionary and appends it to a list
    def save_info():
        global babies
        #Below is the dictionary i created as a way to store data as a new baby is created
        dict = {
        "name: ": baby_name.value,
        "Birth Date: ": birth_date.value,
        "Birth Time: ": birth_time.value,
        "Baby Sex: ": sex.value,
        }
        babies.append(dict)
    window_1 = Window(app, height=650, width=650, layout="grid")
    window_1.bg = "white"
    window_1.show(wait = True)
    baby_pic = Picture(window_1, image="ezgif.com-gif-maker.gif", grid=[0,0], height=100, width=100)
    icon_infant = Picture(window_1, image="ezgif.com-gif-maker.gif", grid=[1,0], height=100, width=100)
    name_label = Text(window_1,text="Babies full name: ", grid=[0,2], width=30, height=5, font="Atkinson Hyper Legible")
    name_label.bg = "#f1feea"
    baby_name = TextBox(window_1, grid=[1,2], width=40, height=5)
    baby_name.bg = "#a8dadc"
    date_label = Text(window_1,text="Date of Birth: ", grid=[0,3], width=30, height=5, font="Atkinson Hyper Legible")
    date_label.bg = "#f1feea"
    birth_date = TextBox(window_1, grid=[1,3], width=40, height=5)
    birth_date.bg = "#a8dadc"
    time_label = Text(window_1,text="Time of Birth: ", grid=[0,4], width=30, height=5, font="Atkinson Hyper Legible")
    time_label.bg = "#f1feea"
    birth_time = TextBox(window_1, grid=[1,4], width=40, height=5)
    birth_time.bg = "#a8dadc"
    sex_label = Text(window_1, text="Baby Sex: ", grid=[0,5], width=30, height=5, font="Atkinson Hyper Legible")
    sex_label.bg  = "#f1feea"
    sex = TextBox(window_1, grid=[1,5], width=40, height=5)
    sex.bg = "#a8dadc"
    baby_num += 1
    num_label = Text(window_1, text="Baby Number: ", grid=[0,6], width=30, height=5, font="Atkinson Hyper Legible")
    num_label.bg  = "#f1feea"
    num = Text(window_1, grid=[1,6], width=40, height=5, text=baby_num, font="Atkinson Hyper Legible")
    num.bg = "#a8dadc"
    print("Baby number: " + str(baby_num))
    #Bellow is the save and quit button, save is defined on line 24
    save_button = PushButton(window_1, grid=[0,7], text="Save", height=5, width=25, command=save_info)
    quit_button = PushButton(window_1, grid=[1,7], text="Quit", command=window_1.destroy, height=5, width=25)

def baby():
    global babies
    window_2 = Window(app, layout="auto", height=650, width=650)
    window_2.show(wait = True)
    banner = Box(window_2, height=20, width=650)
    banner.bg = "grey"
    banner_name = Text(banner, text="Babies", align="left", size=15, font="Atkinson hyperlegible")
    title = Text(window_2, text="Babies:", size=25, font="Catamaran")
    baby_box = Box(window_2, height=75 , width=500, border=True)
    baby_box.bg = "white"
    baby = Text(baby_box, text=babies[0])
    baby1 = Text(baby_box, text=babies[1])
    quit_button = PushButton(window_2, text="Quit", command=window_2.destroy, height=5, width=25)


def data_entry():
    global bby1_temp
    #this is the defintion of the save function it appends the information entered in the text box to a list
    def save_temp():
        if int(num_temp.value) == 1:
            if entry_temp.value > str(37.5):
                window_3.info("window", "Baby temperature is too high, act immediately")
                bby1_temp.append(entry_temp.value)
            elif entry_temp.value < str(36):
                window_3.info("window", "Baby temperature too low, act immediately")
                bby1_temp.append(entry_temp.value)
        elif int(num_temp.value) == 2:
            bby2_temp.append(entry_temp.value)
            if entry_temp.value > str(37.5):
                window_3.info("window", "Baby temperature is too high, act immediately")
            elif entry_temp.value < str(36):
                window_3.info("window", "Baby temperature too low, act immediately")
    window_3 = Window(app, layout="auto", height=650, width=650)
    window_3.show(wait = True)
    banner = Box(window_3, height=20, width=650)
    banner.bg = "grey"
    banner_name = Text(banner, text="Data Entry", align="left")
    baby_pic = Picture(window_3, image="ezgif.com-gif-maker.gif", height=120, width=130)
    info_display = Box(window_3, height=75 , width=500, border=True)
    info_display.bg = "white"
    baby = Text(info_display, text=babies[0])
    baby1 = Text(info_display, text=babies[1])
    entry_label = Text(window_3, text="Enter Temperature: ")
    entry_temp = TextBox(window_3, height=5, width=30)
    num_label = Text(window_3, text="Enter Baby Number: ")
    num_temp = TextBox(window_3, height=5, width=30)
    save_button = PushButton(window_3, text="Save", command=save_temp, height=5, width=30, align="left")
    quit_button = PushButton(window_3, text="Quit", command=window_3.destroy, height=5, width=30, align="right")

def statistics():
    global babies, bby1_temp
    def enter():
        if int(num_bby.value) == 1:
            data = Text(data_box, text=babies[0])
            data01 = Text(data_box, text=bby1_temp)
        elif int(num_bby.value) == 2:
            data1 = Text(data_box, text=babies[1])
            data11 = Text(data_box, text=bby2_temp)
        elif int(num_bby.value) == 3:
            data2 = Text(data_box, text=babies[2])
    window_4 = Window(app, layout="auto", height=650, width=650)
    window_4.show(wait=True)
    banner = Box(window_4, height=18, width=650)
    banner.bg = "grey"
    banner_name = Text(banner, text="Statistics", align="left", size=12)
    num_label = Text(window_4, text="Enter Baby Number: ", size=15, font="Atkinson Hyper legible")
    num_bby = TextBox(window_4, height=5, width=30)
    enter = PushButton(window_4, text="enter", command=enter, height=5, width=30)
    data_box = Box(window_4, border=True, height=75, width=500)

app = App(layout="grid")
app.bg = "white"

menu()

app.display()
