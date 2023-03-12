from tkinter import *
from tkinter import messagebox
import pymysql
from PIL import Image,ImageTk



conn = pymysql.connect(host="localhost", user="root", passwd="",database="testing")

myCursor=conn.cursor()

root2=Tk()
#root2.configure(background="black")
content=''
i=0
bat1=[]
def retrieve():
    global content
    content=name.get("1.0", "end-1c")

def bat_name_list():
    global i
    try:
        if i<6:
            retrieve()
            bat1.append(content)
            print(bat1)
            i=i+1
            name.delete(0.0,END)
    except Exception:
            print("")
    
label11=Label(root2,text="Enter name of batsmen")
label11.pack()
label11.config(width=30)
label11.config(font=("Courier",20))
name = Text(root2,height=1,width=30)
name.pack()

button_sub=Button(root2,text="SUBMIT",command=bat_name_list)
button_sub.config(height=2, width=10)
button_sub.pack(padx=5, pady=20,side=BOTTOM)
root2.mainloop()

root=Tk()

img=ImageTk.PhotoImage(Image.open("kohli.jpg"))
panel=Label(root,image=img)
panel.pack(side="left")

img2=ImageTk.PhotoImage(Image.open("starc.jpg"))
panel2=Label(root,image=img2)
panel2.pack(side="right")


score=0
wicket=0
ball_runs=[]
balls=0
overs=0
bat1_score=0
bat2_score=0
strike=0
bat1_ball=0
bat2_ball=0
bat1_sr=0
bat2_sr=0
run_rate=0
total_balls=0
n=1   



#FUNCTIONS

def curr_rr():
    global n

def bat1_strike():
    global bat1_score
    global bat1_ball
    global bat1_sr
    bat1_sr=((bat1_score/bat1_ball)*100)
    bat1_sr=str(round(bat1_sr,2))
    batsman1_sr.config(text=bat1_sr)

def bat2_strike():
    global bat2_score
    global bat2_ball
    global bat2_sr
    bat2_sr=(bat2_score/bat2_ball)*100
    bat2_sr=str(round(bat2_sr,2))
    batsman2_sr.config(text=bat2_sr)
    
def bat1_ball_count():
    global bat1_ball
    bat1_ball+=1
    batsman1_balls.config(text=bat1_ball)

def bat2_ball_count():
    global bat2_ball
    bat2_ball+=1
    batsman2_balls.config(text=bat2_ball)
        
def over_count_even():
    global balls
    global overs
    global bat1_score
    global bat2_score
    global strike
    global total_balls
    balls+=1
    total_balls+=1
    
    if(balls==6):
        overs+=1
        try:
            if(overs==5):
                root11=Tk()
                disp_txt=Label(root11,text="Innings over, Next Team please")
                disp_txt.pack()
                disp_txt.config(height=5,width=30)
                disp_txt.config(font=("Courier",20))
                root11.mainloop()
        except Exception as e:
                print("")
        balls=0
        if(strike%2==0):
            #bat1_score+=1
            batsman1.config(text="")
            batsman1_score.config(text=bat1_score)
            batsman2.config(text="*")
        else:
            #bat2_score+=1
            batsman2.config(text="")
            batsman2_score.config(text=bat2_score)
            batsman1.config(text="*")
        strike+=1
        
        
        
        
    label_over.config(text=overs)
    label_ball.config(text=balls)
    

def over_count_odd():
    global balls
    global overs
    global bat1_score
    global bat2_score
    global strike
    global total_balls
    balls+=1
    total_balls+=1
    
    if(balls==6):
        overs+=1
        try:
            if(overs==5):
                root10=Tk()
                disp_txt=Label(root10,text="Innings over, Next Team please")
                disp_txt.pack()
                disp_txt.config(height=5,width=30)
                disp_txt.config(font=("Courier",20))
                root10.mainloop()
        except Exception as e:
            print("")
        balls=0
        if(strike%2==0):
            #bat1_score+=1
            batsman1.config(text="*")
            batsman1_score.config(text=bat1_score)
            batsman2.config(text="")
        else:
            #bat2_score+=1
            batsman2.config(text="*")
            batsman2_score.config(text=bat2_score)
            batsman1.config(text="")
        strike+=1
        
    label_over.config(text=overs)
    label_ball.config(text=balls)
    

    

def dot_ball():
    global score
    global bat1_score
    global bat2_score
    #score+=1
    if(strike%2==0):
        #bat1_score+=2
        bat1_ball_count()
        bat1_strike()
        #batsman1.config(text="Batsman1:")
        batsman1_score.config(text=bat1_score)
        #batsman2.config(text="Batsman2*:")
    else:
        #bat2_score+=2
        bat2_ball_count()
        bat2_strike()
        #batsman2.config(text="Batsman2:")
        batsman2_score.config(text=bat2_score)
        #batsman1.config(text="Batsman1*:")
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append(0)
    label3.config(text=ball_runs)
    over_count_even()
    curr_rr()
    
def one_run():
    global score
    global bat1_score
    global bat2_score
    global strike
    score+=1
    if(strike%2==0):
        bat1_score+=1
        bat1_ball_count()
        bat1_strike()
        batsman1.config(text="")
        batsman1_score.config(text=bat1_score)
        batsman2.config(text="*")
    else:
        bat2_score+=1
        bat2_ball_count()
        bat2_strike()
        batsman2.config(text="")
        batsman2_score.config(text=bat2_score)
        batsman1.config(text="*")
    
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append(1)
    label3.config(text=ball_runs)
    over_count_odd()
    curr_rr()
    strike+=1

def two_run():
    global score
    global bat1_score
    global bat2_score
    score+=2
    if(strike%2==0):
        bat1_score+=2
        bat1_ball_count()
        bat1_strike()
        #batsman1.config(text="Batsman1:")
        batsman1_score.config(text=bat1_score)
        #batsman2.config(text="Batsman2*:")
    else:
        bat2_score+=2
        bat2_ball_count()
        bat2_strike()
        #batsman2.config(text="Batsman2:")
        batsman2_score.config(text=bat2_score)
        #batsman1.config(text="Batsman1*:")
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append(2)
    label3.config(text=ball_runs)
    over_count_even()
    curr_rr()

def three_run():
    global score
    global bat1_score
    global bat2_score
    global strike
    score+=3
    if(strike%2==0):
        bat1_score+=3
        bat1_ball_count()
        bat1_strike()
        batsman1.config(text="")
        batsman1_score.config(text=bat1_score)
        batsman2.config(text="*")
    else:
        bat2_score+=3
        bat2_ball_count()
        bat2_strike()
        batsman2.config(text="")
        batsman2_score.config(text=bat2_score)
        batsman1.config(text="*")
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append(3)
    label3.config(text=ball_runs)
    over_count_odd()
    strike+=1

def four_run():
    global score
    global bat1_score
    global bat2_score
    global strike
    score+=4
    if(strike%2==0):
        bat1_score+=4
        bat1_ball_count()
        bat1_strike()
        #batsman1.config(text="Batsman1:")
        batsman1_score.config(text=bat1_score)
        #batsman2.config(text="Batsman2*:")
    else:
        bat2_score+=4
        bat2_ball_count()
        bat2_strike()
        #batsman2.config(text="Batsman2:")
        batsman2_score.config(text=bat2_score)
        #batsman1.config(text="Batsman1*:")
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append(4)
    label3.config(text=ball_runs)
    over_count_even()

def five_run():
    global score
    global bat1_score
    global bat2_score
    global strike
    score+=5
    if(strike%2==0):
        bat1_score+=5
        bat1_ball_count()
        bat1_strike()
        batsman1.config(text="")
        batsman1_score.config(text=bat1_score)
        batsman2.config(text="*")
    else:
        bat2_score+=5
        bat2_ball_count()
        bat2_strike()
        batsman2.config(text="")
        batsman2_score.config(text=bat2_score)
        batsman1.config(text="*")
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append(5)
    label3.config(text=ball_runs)
    over_count_odd()
    strike+=1

def six_run():
    global score
    global bat1_score
    global bat2_score
    global strike
    score+=6
    if(strike%2==0):
        bat1_score+=6
        bat1_ball_count()
        bat1_strike()
        #batsman1.config(text="Batsman1:")
        batsman1_score.config(text=bat1_score)
        #batsman2.config(text="Batsman2*:")
    else:
        bat2_score+=6
        bat2_ball_count()
        bat2_strike()
        #batsman2.config(text="Batsman2:")
        batsman2_score.config(text=bat2_score)
        #batsman1.config(text="Batsman1*:")
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append(6)
    label3.config(text=ball_runs)
    over_count_even()

def wickets():
    global wicket
    global bat1_score
    global bat2_score
    global bat1_ball
    global bat2_ball
    global bat1_sr
    global bat2_sr
    try:
        wicket+=1
        next_bat()
        if(strike%2==0):
            #bat1_score+=6
            bat1_ball_count()
            bat1_strike()
            myCursor.execute("insert into batsman_score(name,runs,balls) values(%s,%s,%s);",(bat1[n-1],bat1_score,bat1_ball))
            conn.commit()
            bat1_score=0
            bat1_ball=0
            bat1_sr=0
            #batsman1.config(text="Batsman1:")
            batsman1_score.config(text=bat1_score)
            batsman1_balls.config(text=bat1_ball)
            batsman1_sr.config(text=bat1_sr)
            batsmanName1.config(text=bat1[n])
            #batsman2.config(text="Batsman2*:")
        else:
            #bat2_score+=6
            bat2_ball_count()
            bat2_strike()
            myCursor.execute("insert into batsman_score(name,runs,balls) values(%s,%s,%s);",(bat1[n],bat2_score,bat2_ball))
            conn.commit()
            bat2_score=0
            bat2_ball=0
            bat2_sr=0
            #batsman2.config(text="Batsman2:")
            batsman2_score.config(text=bat2_score)
            batsman2_balls.config(text=bat2_ball)
            batsman2_sr.config(text=bat2_sr)
            batsmanName2.config(text=bat1[n])
            #batsman1.config(text="Batsman1*:")

        
        label2.config(text=wicket)
        ball_runs.append("W")
        if(wicket==len(bat1[n])):
            print("All out")
        label3.config(text=ball_runs)
        over_count_even()
    except Exception as e:
        print("Next team please!")
        root6=Tk()
        disp_txt=Label(root6,text="All Out, Next Team please")
        disp_txt.pack()
        disp_txt.config(height=5,width=30)
        disp_txt.config(font=("Courier",20))
        root6.mainloop()
    

def wide():
    global score
    score+=1
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append("Wd")
    label3.config(text=ball_runs)
    #over_count()

def no_ball():
    global score
    score+=1
    label1.config(text=score)
    label1.config(font=("Courier",20))
    ball_runs.append("Nb")
    label3.config(text=ball_runs)
    #over_count()

def insert_db():
    global score
    global wicket
    myCursor.execute("insert into inn_scores(score,wickets) values(%s,%s);",(score,wicket))
    conn.commit()
    root5=Tk()
    disp_score=Label(root5,text="Final Score :"+str(score)+"/"+str(wicket))
    disp_score.pack()
    disp_score.config(width=30)
    disp_score.config(font=("Courier",20))
    disp_target=Label(root5,text="Target :"+str(score+1))
    disp_target.pack()
    disp_target.config(width=30)
    disp_target.config(font=("Courier",20))
    disp_rr=Label(root5,text="Required RunRate :"+str(float(score//5)))
    disp_rr.pack()
    disp_rr.config(width=30)
    disp_rr.config(font=("Courier",20))
    #disp_highest=Label(root5,text="Top scorer")
    #disp_highest.pack()
    #top_batsman=myCursor.execute("select MAX(runs) from batsman_scores;")
    #disp_high_score=Label(root5,text=str(top_batsman))
    #disp_high_score.pack()
    root5.mainloop()

def next_bat():
    global n
    n=n+1

def retrieve_score():
    myCursor.execute("SELECT score from inn_scores")
    lis = myCursor.fetchall()
    
    print(lis[len(lis)-1])
    root8=Tk()
    prev_lbl=Label(root8,text="PREVIOUS INNINGS SCORE :")
    prev_lbl.pack()
    prev_lbl.config(width=30)
    prev_lbl.config(font=("Courier",20))
    prev_score=Label(root8,text="Runs :"+str(lis[len(lis)-1]))
    prev_score.pack()
    prev_score.config(width=20)
    prev_score.config(font=("Courier",20))
    root8.mainloop()


#print("SCORE",end='')

topFrame=Frame(root)
topFrame.pack()

bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

rightFrame=Frame(root)
rightFrame.pack(side=RIGHT)


#LABELS
labelsc=Label(topFrame,text="SCORECARD",fg="red")
labelsc.config(width=20)
labelsc.config(font=("Courier",40))
labelsc.pack()


#SCORE LABEL
labelss=Label(topFrame,text="Score:",fg="red")
labelss.config(width=10)
labelss.config(font=("Courier",20))
labelss.pack(side=LEFT)
label1=Label(topFrame,text="0",fg="red")
label1.config(width=10)
label1.config(font=("Courier",20))
label1.pack(side=LEFT)
label_slash=Label(topFrame,text="|",fg="red")
label_slash.config(width=2)
label_slash.config(font=("Courier",20))
label_slash.pack(side=LEFT)
label2=Label(topFrame,text="0",fg="red")
label2.config(width=5)
label2.config(font=("Courier",20))
label2.pack(side=LEFT)

label3=Label(rightFrame,text="")
label3.pack(side=LEFT)

#OVERS LABEL

label4=Label(topFrame,text="OVERS:",fg="red")
label4.config(width=10)
label4.config(font=("Courier",20))
label4.pack(side=LEFT)
label_over=Label(topFrame,text="0",fg="red")
label_over.config(width=5)
label_over.config(font=("Courier",20))
label_over.pack(side=LEFT)
label_dot=Label(topFrame,text=".",fg="red")
label_dot.config(width=3)
label_dot.config(font=("Courier",20))
label_dot.pack(side=LEFT)
label_ball=Label(topFrame,text="0",fg="red")
label_ball.config(width=5)
label_ball.config(font=("Courier",20))
label_ball.pack(side=LEFT)


#RUN RATE LABELS
#label_nrr=Label(topFrame,text="RUN RATE:")
#label_nrr.pack(side=LEFT)
#label_runrate=Label(topFrame,text="0")
#label_runrate.pack(side=LEFT)

#BATSMEN LABELS
bat_lbl=Label(bottomFrame, text="BATSMEN",fg="red")
bat_lbl.config(width=10)
bat_lbl.config(font=("Courier",30))
bat_lbl.pack()
#BATSMEN LABELS
batsmanName1=Label(bottomFrame,text=bat1[n-1],fg="blue")
batsmanName1.config(width=20)
batsmanName1.config(font=("Courier",20))
batsmanName1.pack()
batsman1=Label(bottomFrame,text="*",fg="red")
batsman1.config(width=5)
batsman1.config(font=("Courier",20))
batsman1.pack()
batsman1core=Label(bottomFrame,text="Score: ").pack()
batsman1_score=Label(bottomFrame,text="0")
batsman1_score.pack()
batsman1ball=Label(bottomFrame,text="Balls: ").pack()
batsman1_balls=Label(bottomFrame,text="0")
batsman1_balls.pack()
batsman1sr=Label(bottomFrame,text="StrikeRate: ").pack()
batsman1_sr=Label(bottomFrame,text="0")
batsman1_sr.pack()

batsmanName2=Label(bottomFrame,text=bat1[n],fg="blue")
batsmanName2.config(width=20)
batsmanName2.config(font=("Courier",20))
batsmanName2.pack()
batsman2=Label(bottomFrame,text="",fg="red")
batsman2.pack()
batsman2.config(width=5)
batsman2.config(font=("Courier",20))
batsman2core=Label(bottomFrame,text="Score: ").pack()
batsman2_score=Label(bottomFrame,text="0")
batsman2_score.pack()
batsman1ball=Label(bottomFrame,text="Balls: ").pack()
batsman2_balls=Label(bottomFrame,text="0")
batsman2_balls.pack()
batsman2sr=Label(bottomFrame,text="SrtikeRate: ").pack()
batsman2_sr=Label(bottomFrame,text="0")
batsman2_sr.pack()



#label1.grid(row=2,column=2)


#BUTTONS

button_dot=Button(bottomFrame,text="DOT ",command=dot_ball)
button_dot.config(height=2, width=5)
button_dot.pack(padx=5, pady=20,side=LEFT)
button1=Button(bottomFrame,text="1 run",command=one_run)
button1.config(height=2, width=5)
button1.pack(padx=5, pady=20,side=LEFT)
button2=Button(bottomFrame,text="2 run",command=two_run)
button2.config(height=2, width=5)
button2.pack(padx=5, pady=20,side=LEFT)
button3=Button(bottomFrame,text="3 run",command=three_run)
button3.config(height=2, width=5)
button3.pack(padx=5, pady=20,side=LEFT)
button4=Button(bottomFrame,text="4 run",command=four_run)
button4.config(height=2, width=5)
button4.pack(padx=5, pady=20,side=LEFT)
button5=Button(bottomFrame,text="5 run",command=five_run)
button5.config(height=2, width=5)
button5.pack(padx=5, pady=20,side=LEFT)
button6=Button(bottomFrame,text="6 run",command=six_run)
button6.config(height=2, width=5)
button6.pack(padx=5, pady=20,side=LEFT)
button_wicket=Button(bottomFrame,text="wicket",command=wickets)
button_wicket.config(height=2, width=5)
button_wicket.pack(padx=5, pady=20,side=LEFT)
button_wide=Button(bottomFrame,text="wide",command=wide)
button_wide.config(height=2, width=5)
button_wide.pack(padx=5, pady=20,side=LEFT)
button_noball=Button(bottomFrame,text="no ball",command=no_ball)
button_noball.config(height=2, width=5)
button_noball.pack(padx=5, pady=20,side=LEFT)
button_sub=Button(bottomFrame,text="Submit",command=insert_db)
button_sub.config(height=2, width=5)
button_sub.pack(padx=5, pady=20,side=LEFT)
button_sub=Button(bottomFrame,text="RETR",command=retrieve_score)
button_sub.config(height=2, width=5)
button_sub.pack(padx=5, pady=20,side=LEFT)

#button1.grid(row=3,column=0)
#button2.grid(row=3,column=1)

frame=Frame(root,height=200,width=300)
#root.geometry('300x200+250+250')


root.mainloop()


conn.close()


