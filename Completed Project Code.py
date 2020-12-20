import tkinter as tk
from tkinter import ttk
import datetime
import NSFC
import time

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
#Create canvas
HEIGHT = 800
WIDTH = 800
blue = '#80c1ff'

root = tk.Tk()
root.title("NSFC stalls")
root.resizable(0, 0)                      #to lock the window to the default size 

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

#Create background image
background_image = tk.PhotoImage(file = 'NSFC_Photo.png')
background_label = tk.Label(root,image = background_image)
background_label.place(relwidth = 1, relheight = 1)

#Create top blue frame
frame = tk.Frame(root,bg = blue,bd=10)
frame.place(relx=0.5, rely=0.02, relwidth = 0.75, relheight = 0.15, anchor = 'n')

#Create bottom blue frame
lower_frame = tk.Frame(root, bg = blue,bd=15)
lower_frame.place(relx = 0.5, rely = 0.19, relwidth = 0.75, relheight = 0.78, anchor = 'n')

##-----------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#Input date
#assigning variables
textfont = ('courier', 14, "bold")
menufont = ('courier', 9, "bold")
menufont2 = ('Times', 8, "bold")
dmy_rely = 0.1
dmy_relwidth = 0.15
dmy_relheight = 0.3

#listing all the options for day
options_day = ['01','02','03','04','05','06','07','08','09',10,
                11,12,13,14,15,16,17,18,19,20,
                21,22,23,24,25,26,27,28,29,30,31]

#listing all the options for month
options_month = ['01','02','03','04','05','06','07','08','09',10,11,12]

#listing all the options for year
options_year = [2019,2020,2021,2022,2023,2014,2025,2026,2027,2028,2029,
                2031,2032,2033,2034,2035,2036,2037,2038,2039,2040,2041,
                2042,2043,2044,2045,2046,2047,2048,2049,2050,2051,2052,2053,
                2054,2055,2056,2057,2058,2059,2060]


label_date = tk.Label(frame,text = 'Date(dd/mm/yyyy): ',bg = blue, font = textfont,anchor = 'w')
label_date.place(rely = dmy_rely,relwidth = 0.35,relheight = dmy_relheight)

#Date with dropdown function & scroll
#day
var_day = tk.StringVar(root)

dropdown_day = ttk.Combobox(frame,font = textfont, textvariable = var_day, values = options_day)
dropdown_day.place(relx = 0.31,rely = dmy_rely,relwidth = dmy_relwidth,relheight = dmy_relheight)


#month
var_month = tk.StringVar(root)

dropdown_month = ttk.Combobox(frame,font = textfont, textvariable = var_month, values = options_month)
dropdown_month.place(relx = 0.46,rely = dmy_rely,relwidth = dmy_relwidth,relheight = dmy_relheight)


#year
var_year = tk.StringVar(root)

dropdown_year = ttk.Combobox(frame,font = textfont, textvariable = var_year, values = options_year)
dropdown_year.place(relx = 0.61,rely = dmy_rely,relwidth = dmy_relwidth,relheight = dmy_relheight)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#Input time
#assign variables
time_rely = 0.6

#listing all the options for hour
options_hour= ['00','01','02','03','04','05','06','07','08','09',10,
               11,12,13,14,15,16,17,18,19,20,21,22,23]

#listing all the options for min
options_mins= ['00','01','02','03','04','05','06','07','08','09',10,
               11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
               31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
               51,52,53,54,55,56,57,58,59]


label_time = tk.Label(frame,text = 'Time(hr/mins): ',bg = blue, font = textfont,anchor = 'w')
label_time.place(rely =time_rely, relwidth = 0.35,relheight = dmy_relheight)

#Time with dropdown function & scroll
#hours
var_hour = tk.StringVar(root)

dropdown_hour = ttk.Combobox(frame,font =textfont,textvariable = var_hour, values = options_hour) 
dropdown_hour.place(rely =time_rely,relx = 0.31, relwidth = dmy_relwidth, relheight = dmy_relheight)

#mins
var_mins = tk.StringVar(root)

dropdown_mins = ttk.Combobox(frame,font = textfont,textvariable = var_mins, values = options_mins) 
dropdown_mins.place(rely =time_rely,relx = 0.46, relwidth = dmy_relwidth, relheight = dmy_relheight)


####------------------------------------------------------------------------------------------------------------------------------------------------------------
##COMMAND FOR SEARCH BUTTON IS BELOW
##Functions

#Convert menu dictionary to string
def display(stall):
    lists = []
    for key,value in stall.items():         
        result = key + ": " + value                     #retrieve key and values of dictionary
        lists.append(result)                            #convert to list
    conv_str = ','.join(str(i) for i in lists)          #convert list to string
    str_sep_newline = conv_str.replace(',','\n')        #replace string's comma with new line
    return str_sep_newline

    
#Western menu - call display function
def Western(day_num,hour_sel,mins_sel):
        if day_num == 0 or day_num == 1 or day_num == 2 or day_num == 3 or day_num == 4:#Weekdays menu
            if 8 <= hour_sel < 11:
                return display(NSFC.Western_B_D_item_price)                             
            elif 11 <= hour_sel < 12:
                if 00 <= mins_sel <=59:
                    return display(NSFC.Western_B_D_item_price)
            elif 12 <= hour_sel < 20:
                return display(NSFC.Western_L_D_item_price)
            elif 20 <= hour_sel < 21:
                if 00 <= mins_sel <=59:
                    return display(NSFC.Western_L_D_item_price)
            else:
                return "Stall is closed."
        elif day_num == 5:                                                  #Saturdays menu
            if 8 <= hour_sel < 11:
                return display(NSFC.Western_B_E_item_price)
            elif 11 <= hour_sel < 12:
                if 00 <= mins_sel <=59:
                    return display(NSFC.Western_B_E_item_price)   
            elif 12 <= hour_sel < 16:
                return display(NSFC.Western_L_E_item_price)
            elif 16 <= hour_sel < 17:
                if 00 <= mins_sel <=59:
                    return display(NSFC.Western_L_E_item_price)
            else:
                return "Stall is closed."       
        elif day_num == 6:                                                  #Sundays menu
            if 8 <= hour_sel < 11:
                return display(NSFC.Western_B_E_item_price)
            elif 11 <= hour_sel < 12:
                if 00 <= mins_sel <=59:
                    return display(NSFC.Western_B_E_item_price)   
            else:
                return "Stall is closed."

#Chicken Rice menu - call display function
def ChickenRice(day_num,hour_sel,mins_sel):
        if day_num == 0 or day_num == 1 or day_num == 2 or day_num == 3 or day_num == 4:#Weekdays menu
            if 8 <= hour_sel < 20:
                return display(NSFC.CR_item_price)
            elif 20 <= hour_sel < 21:
                if 00 <= mins_sel <=59:
                    return display(NSFC.CR_item_price)
            else:
                return "Stall is closed."
        elif day_num == 5:                                                  #Saturdays menu
            if 8 <= hour_sel < 16:
                return display(NSFC.CR_item_price)
            elif 16 <= hour_sel < 17:
                if 00 <= mins_sel <=59:
                    return display(NSFC.CR_item_price)
            else:
                return "Stall is closed."       
        elif day_num == 6:                                                  #Sundays
            if 8 <= hour_sel <= 11:
                return display(NSFC.CR_item_price)
            elif 11 <= hour_sel < 12:
                if 00 <= mins_sel <=59:
                    return display(NSFC.CR_item_price)
            else:
                return "Stall is closed."

#Xin Mei Noodle Menu - call display function
def XinMeiNoodleStall(day_num,hour_sel,mins_sel):
        if day_num == 0 or day_num == 1 or day_num == 2 or day_num == 3 or day_num == 4:#Weekdays menu
            if 8 <= hour_sel < 20:
                return display(NSFC.XM_item_price)
            elif 20 <= hour_sel < 21:
                if 00 <= mins_sel <=59:
                    return display(NSFC.XM_item_price)
            else:
                return "Stall is closed."
        elif day_num == 5:                                                  #Saturdays menu
            if 8 <= hour_sel < 16:
                return display(NSFC.XM_item_price)
            elif 16 <= hour_sel < 17:
                if 00 <= mins_sel <=59:
                    return display(NSFC.XM_item_price)
            else:
                return "Stall is closed."       
        elif day_num == 6:                                                  #Sundays menu
            if 8 <= hour_sel < 11:
                return display(NSFC.XM_item_price)
            elif 11 <= hour_sel < 12:
                if 00 <= mins_sel <=59:
                    return display(NSFC.XM_item_price)
            else:
                return "Stall is closed."

#Xin Mei Noodle Menu - call display function
def MVRStall(day_num,hour_sel,mins_sel):
        if day_num == 0 or day_num == 1 or day_num == 2 or day_num == 3 or day_num == 4:#Weekdays menu
            if 8 <= hour_sel < 20:
                return display(NSFC.MVR_item_price)
            elif 20 <= hour_sel < 21:
                if 00 <= mins_sel <=59:
                    return display(NSFC.MVR_item_price)
            else:
                return "Stall is closed."
        elif day_num == 5:                                                  #Saturdays menu
            if 8 <= hour_sel < 16:
                return display(NSFC.MVR_item_price)
            elif 16 <= hour_sel < 17:
                if 00 <= mins_sel <=59:
                    return display(NSFC.MVR_item_price)
            else:
                return "Stall is closed."       
        elif day_num == 6:                                                  #Sundays menu
            if 8 <= hour_sel < 11:
                return display(NSFC.MVR_item_price)
            elif 11 <= hour_sel < 12:
                if 00 <= mins_sel <=59:
                    return display(NSFC.MVR_item_price)
            else:
                return "Stall is closed."       

#display menu and price----------------------------------------------------------------------------------------------------------------------------------------------------
#Try-Except to test for invalid inputs
def price():
    try:
        day_num = datetime.datetime(int(var_year.get()),int(var_month.get()),int(var_day.get())).weekday()
        hour_sel = int((var_hour.get()))
        mins_sel = int((var_mins.get()))
        if 0 <= hour_sel <= 23:
                if 0 <= mins_sel <= 59:
                        label1['text'] = Western(day_num,hour_sel,mins_sel)             #Call Western function --> calls display function --> print menu in string
                        label1['font'] = menufont
                        label2['text'] = ChickenRice(day_num,hour_sel,mins_sel)         #Call Chicken Rice function --> calls display function --> print menu in string
                        label2['font'] = menufont
                        label3['text'] = XinMeiNoodleStall(day_num,hour_sel,mins_sel)   #Call Xin Mei Noodle function --> calls display function --> print menu in string
                        label3['font'] = menufont
                        label4['text'] = MVRStall(day_num,hour_sel,mins_sel)            #Call MVR function --> calls display function --> print menu in string
                        label4['font'] = menufont
                else:
                        label1['text'] = 2/0    #to force an error out if the user inputs something out of the selected range
                        label2['text'] = 2/0    #to force an error out if the user inputs something out of the selected range
                        label3['text'] = 2/0    #to force an error out if the user inputs something out of the selected range
                        label4['text'] = 2/0    #to force an error out if the user inputs something out of the selected range
        else:
                label1['text'] = 2/0            #to force an error out if the user inputs something out of the selected range
                label2['text'] = 2/0            #to force an error out if the user inputs something out of the selected range
                label3['text'] = 2/0            #to force an error out if the user inputs something out of the selected range
                label4['text'] = 2/0            #to force an error out if the user inputs something out of the selected range
    except:
        label1['text'] = "Invalid input! Please try again."
        label1['font'] = menufont
        label2['text'] = "Invalid input! Please try again."
        label2['font'] = menufont
        label3['text'] = "Invalid input! Please try again."
        label3['font'] = menufont
        label4['text'] = "Invalid input! Please try again."
        label4['font'] = menufont

def reset():
    label1['text'] = ""
    label2['text'] = ""
    label3['text'] = ""
    label4['text'] = ""
    

button = tk.Button(frame,text ='Search',font = textfont,relief=tk.RAISED,command=price)
button.place(relx = 0.83,rely = time_rely, relheight = 0.30, relwidth = 0.17)

button = tk.Button(frame,text ='Clear',font = textfont,relief=tk.RAISED,command=reset)
button.place(relx = 0.65,rely = time_rely, relheight = 0.30, relwidth = 0.17)

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Display current time
def current_menu():
    now = datetime.datetime.now()
    day_num = datetime.datetime.today().weekday()
    hour_sel = now.hour
    mins_sel = now.minute
    label1['text'] = Western(day_num,hour_sel,mins_sel)             #Call Western function --> calls display function --> print menu in string
    label1['font'] = menufont
    label2['text'] = ChickenRice(day_num,hour_sel,mins_sel)         #Call Chicken Rice function --> calls display function --> print menu in string
    label2['font'] = menufont
    label3['text'] = XinMeiNoodleStall(day_num,hour_sel,mins_sel)   #Call Xin Mei Noodle function --> calls display function --> print menu in string
    label3['font'] = menufont
    label4['text'] = MVRStall(day_num,hour_sel,mins_sel)            #Call MVR function --> calls display function --> print menu in string
    label4['font'] = menufont

clock = tk.Button(frame,font = textfont,relief=tk.RAISED,command= current_menu)
clock.place(relx = 0.79,rely = dmy_rely, relheight = 0.35, relwidth = 0.2)

time_past = ''
def tick():
    global time_past
    time_now = time.strftime('%H:%M:%S')            #retrieve time from PC
    if time_now != time_past:
        time_past = time_now                        #Update the time
        clock.config(text=time_now)
    clock.after(200, tick)                          # calls itself every 200 milliseconds, update time display
tick()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#function to create new window for waiting time estimation
def wait_time_cal():

        root2 = tk.Tk()
        root2.title("Waiting Time Estimation")
        tk.Label(root2, text='Input number of people waiting in queue (cap at 49):').grid(row=0)
        root2.resizable(0,0)
        e1 = tk.Entry(root2)
        e1.grid(row=0, column=1)

        wait_time_frame = tk.Label(root2)
        wait_time_frame.grid(row=1 , column=1)

        def estimate():
            try:
                time = int(e1.get())*2                               #get the integer value fo input and perform calculation
                if 0 <= time < 100:                                  #put a cap on the number of people in the queue
                    if 0 <= time <= 9:
                        time1 = "{:02d}".format(time)                #to add a "0" if the number is a single digit
                        wait_time_frame['text'] = time1, "mins" 
                    else:
                        wait_time_frame['text'] = time, "mins"
                elif time >= 100:
                    wait_time_frame['text'] = "Wait time is too long. You are advised to go to another stall."
                else:                                                #if user inputs negative values
                    wait_time_frame['text'] = "Input is out of range." 
            except:
                wait_time_frame['text'] = "Input is invalid."        #try and except blocks to deal with user not imputting integer

        estimate_button = tk.Button(root2, text = 'Estimate',                 
                                    command = estimate).grid(row=2, column=0)   #to create a button for the estimate function
##------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Full Menu of all stores

    
def stall_info_Western():
    label1['text'] = NSFC.Western
    label1['font'] = menufont2

def stall_info_ChickenRice():
    label2['text'] = NSFC.Chicken_Rice
    label2['font'] = menufont2

def stall_info_XinMeiNoodleStall():
    label3['text'] = NSFC.Xin_Mei_Noodle
    label3['font'] = menufont2

def stall_info_MVRStall():
    label4['text'] = NSFC.Mixed_Veg_Rice
    label4['font'] = menufont2

##------------------------------------------------------------------------------------------------------------------------------------------------------------------
##------------------------------------------------------------------------------------------------------------------------------------------------------------------

#assigning variables
stall_relx = 0.005
stall_rely = 0.005
stall_relwidth = 0.595
stall_relheight = 0.175
ops_relx = 0.61
ops_rely = 0.005
ops_relwidth = 0.385
ops_relheight = 0.18
mbutt_rely = 0.62
tbutt_rely = 0.81
ops_hrs = 'Operating Hours:\n\n Mon-Fri: 0800-2100\n Sat: 0800-1700\n Sun: 0800-1200'
textfont2 = ('courier', 11, "bold")
textfont3 = ('arial', 9)
gray = "gray80"

#Display Western stall----------------------------------------------------------------------------------------------------------------------------------------------
frame1 = tk.Frame(lower_frame, bg = 'white')
frame1.place(relx=0,relwidth=0.59,relheight = 0.23)

#photo
western_menu = tk.PhotoImage(file = 'western_menu.png')
w_m_image = tk.Label(frame1, image = western_menu)
w_m_image.pack(side='bottom',anchor = 'w')

#Stall name
label_western = tk.Label(frame1,font = textfont2,text = 'Western',bg = gray)
label_western.place(relx=stall_relx,rely = stall_rely,relwidth = stall_relwidth,relheight = stall_relheight)

#Ops_hour
label_w_ops = tk.Label(frame1,font = textfont3, text = ops_hrs,bg = gray)
label_w_ops.place(relx=ops_relx,rely=ops_rely,relwidth = ops_relwidth,relheight = 0.6)

#Menu button
w_menu_button = tk.Button(frame1,text ='Stall Information',command=stall_info_Western)
w_menu_button.place(relx = ops_relx,rely=mbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Time button
w_time_button = tk.Button(frame1,text ='Calculate waiting time',command=wait_time_cal)
w_time_button.place(relx = ops_relx,rely=tbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Menu display box
label1 = tk.Label(lower_frame)
label1.place(relx=0.60,relwidth = 0.4,relheight = 0.23)

#Display Chicken Rice stall----------------------------------------------------------------------------------------------------------------------------------------------
frame2 = tk.Frame(lower_frame, bg = 'white')
frame2.place(relx=0,rely=0.25, relwidth=0.59,relheight = 0.23)

#photo
cr_menu = tk.PhotoImage(file = 'c_r.png')
cr_m_image = tk.Label(frame2, image = cr_menu)
cr_m_image.pack(side='bottom',anchor = 'w')

#Stall name
label_cr = tk.Label(frame2,font = textfont2,text = 'Chicken Rice',bg = gray)
label_cr.place(relx=stall_relx,rely = stall_rely,relwidth = stall_relwidth,relheight = stall_relheight)

#Ops_hour
label_cr_ops = tk.Label(frame2,font = textfont3,text = ops_hrs,bg = gray)
label_cr_ops.place(relx=ops_relx,rely=ops_rely,relwidth = ops_relwidth,relheight = 0.6)

#Menu button
cr_menu_button = tk.Button(frame2,text ='Stall Information',command=stall_info_ChickenRice)
cr_menu_button.place(relx = ops_relx,rely=mbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Time button
cr_time_button = tk.Button(frame2,text ='Calculate waiting time',command=wait_time_cal)
cr_time_button.place(relx = ops_relx,rely=tbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Menu display box
label2 = tk.Label(lower_frame)
label2.place(relx=0.60,rely = 0.25, relwidth = 0.4,relheight = 0.23)

#Display Xin Mei Noodle stall----------------------------------------------------------------------------------------------------------------------------------------------
frame3 = tk.Frame(lower_frame,bg = 'white')
frame3.place(relx=0,rely = 0.50,relwidth=0.59,relheight = 0.23)

#photo
noodle_menu = tk.PhotoImage(file = 'noodle.png')
noodle_m_image = tk.Label(frame3, image = noodle_menu)
noodle_m_image.pack(side='bottom',anchor = 'w')

#Stall name
label_noodle = tk.Label(frame3,font = textfont2,text = 'Xin Mei Noodle Stall',bg = gray)
label_noodle.place(relx=stall_relx,rely = stall_rely,relwidth = stall_relwidth,relheight = stall_relheight)

#Ops_hour
label_noodle_ops = tk.Label(frame3,font = textfont3,text = ops_hrs,bg = gray)
label_noodle_ops.place(relx=ops_relx,rely=ops_rely,relwidth = ops_relwidth,relheight = 0.6)

#Menu button
noodle_menu_button = tk.Button(frame3,text ='Stall Information',command=stall_info_XinMeiNoodleStall)
noodle_menu_button.place(relx = ops_relx,rely=mbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Time button
noodle_time_button = tk.Button(frame3,text ='Calculate waiting time',command=wait_time_cal)
noodle_time_button.place(relx = ops_relx,rely=tbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Menu display box
label3 = tk.Label(lower_frame)
label3.place(relx=0.60,rely = 0.50, relwidth = 0.4,relheight = 0.23)

#Display Mixed Veg Rice stall----------------------------------------------------------------------------------------------------------------------------------------------
frame4 = tk.Frame(lower_frame, bg = 'white')
frame4.place(relx=0,rely = 0.75,relwidth=0.59,relheight = 0.23)

#photo
MVR_menu = tk.PhotoImage(file = 'MVR.png')
MVR_m_image = tk.Label(frame4, image = MVR_menu)
MVR_m_image.pack(side='bottom',anchor = 'w')

#Stall name
label_MVR = tk.Label(frame4,font = textfont2,text = 'Mixed Veg Rice Stall',bg = gray)
label_MVR.place(relx=stall_relx,rely = stall_rely,relwidth = stall_relwidth,relheight = stall_relheight)

#Ops_hour
label_MVR_ops = tk.Label(frame4,font = textfont3,text = ops_hrs,bg = gray)
label_MVR_ops.place(relx=ops_relx,rely=ops_rely,relwidth = ops_relwidth,relheight = 0.6)

#Menu button
MVR_menu_button = tk.Button(frame4,text ='Stall Information',command=stall_info_MVRStall)
MVR_menu_button.place(relx = ops_relx,rely=mbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Time button
MVR_time_button = tk.Button(frame4,text ='Calculate waiting time',command=wait_time_cal)
MVR_time_button.place(relx = ops_relx,rely=tbutt_rely, relheight = ops_relheight, relwidth = ops_relwidth)

#Menu display box
label4 = tk.Label(lower_frame)
label4.place(relx=0.60,rely = 0.75, relwidth = 0.4,relheight = 0.23)


now = datetime.datetime.now()
day_num = datetime.datetime.today().weekday()
hour_sel = now.hour
mins_sel = now.minute
label1['text'] = Western(day_num,hour_sel,mins_sel)             #Call Western function --> calls display function --> print menu in string
label1['font'] = menufont
label2['text'] = ChickenRice(day_num,hour_sel,mins_sel)         #Call Chicken Rice function --> calls display function --> print menu in string
label2['font'] = menufont
label3['text'] = XinMeiNoodleStall(day_num,hour_sel,mins_sel)   #Call Xin Mei Noodle function --> calls display function --> print menu in string
label3['font'] = menufont
label4['text'] = MVRStall(day_num,hour_sel,mins_sel)            #Call MVR function --> calls display function --> print menu in string
label4['font'] = menufont
    
root.mainloop()
