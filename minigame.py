import turtle
from turtle import *
window = turtle.Screen()
window.title("ping pong")
window.setup(width=800, height=600)
window.tracer(0) # set delay for update drawongs
window.bgcolor(.1,.1,.1)

#setup game object ======
#ball
ball=turtle.Turtle()
ball.speed(0) #drawing speed (fastest)
ball.shape("square")
ball.color("white")
shapesize(stretch_len=1, stretch_wid=1) #تحديد حجم الكرة الجم الستوندار 20 ضرب 20 فكي درت واحد كاني ضربت عشرين في واحد
ball.goto(x=0, y=0) #start position
ball.penup() # باش كي تتحرك ماتخليش موراها اثر
ball_dx, ball_dy = 1, 1
ball_speed= .5
#center line
center_line= turtle.Turtle()
center_line.speed(0) #drawing speed (fastest)
center_line.shape("square")
center_line.color("white")
center_line.shapesize(stretch_len=.1, stretch_wid=25)
center_line.penup()
center_line.goto(0, 0) #start position
#player 1
player_1= turtle.Turtle()
player_1.speed(0)
player_1.shape("square")
player_1.color("blue")
player_1.shapesize(stretch_len=1, stretch_wid=5)
player_1.penup()
player_1.goto(-350, 0)
#player 2
player_2= turtle.Turtle()
player_2.speed(0)
player_2.shape("square")
player_2.color("red")
player_2.shapesize(stretch_len=1, stretch_wid=5)
player_2.penup()
player_2.goto(350, 0)
#score text
score=turtle.Turtle()
score.speed(0)
score.color("green")
score.shapesize(stretch_len=1, stretch_wid=5)
score.penup()
score.goto(0, 260)
score.write("player_1:0, player_2:0", align="center", font=("courier",14,"normal"))
score.hideturtle()# باش تبان غير النتيجة ومايمان فيها ختى شكل لا سهم لا مربع
p1_score, p2_score= 0, 0 # باش نحسب نقاط كل لاعب


#player mnt======
player_speed= 20 # مقدار حركة المضارب
def p1_move_up():
    player_1.sety(player_1.ycor()+player_speed) #هذي باش نحرك اللاعب الاول على محور التراتيب فنقولو خذ موقع اللاعب الاول وزيدلو عشرين بكسل للاعلى
def p1_move_down():
    player_1.sety(player_1.ycor()-player_speed)

def p2_move_up():
    player_2.sety(player_2.ycor()+player_speed) #هذي باش نحرك اللاعب الاول على محور التراتيب فنقولو خذ موقع اللاعب الاول وزيدلو عشرين بكسل للاعلى
def p2_move_down():
    player_2.sety(player_2.ycor()-player_speed)

#GET USERS INPUTS ( key bindines)
window.listen() # تولي الشاشة تستجيب لاوامر اللاعبين
window.onkeypress(p1_move_up, "z") # lazam fr w minscul
window.onkeypress(p1_move_down,"s")   
window.onkeypress(p1_move_up,"Z")
window.onkeypress(p1_move_down,"S")

window.onkeypress(p2_move_up, "Up") # رمز السهم تاع الفوق
window.onkeypress(p2_move_down,"Down")   

#game loop ==============
while True:
    window.update()
    #ball mvt
    ball.setx(ball.xcor()+(ball_dx*ball_speed)) # موضع الكرة الجديد هو موضع الكرة القديم زائد مدار التغير اللي عينتو مسبقا مضروب في سرعة الكرة اللي عينتو ايضا سابقا
    ball.sety(ball.ycor()+(ball_dy*ball_speed))
    
    # BALL AND BORDER COLLISION
    if (ball.ycor()>290): # 290 =>300(top border)- 10(half ball size)
        ball.sety(290)# خلي الكرة في بلاصتها
        ball_dy*=-1 # اعكس او اقلب مسار الكرة
    if (ball.ycor()<-290): # 290 =>300(top border)- 10(half ball size)
        ball.sety(-290)# خلي الكرة في بلاصتها
        ball_dy*=-1 
    #ball and player collision
    #with player 1    
    if ball.xcor()<-340 and ball.xcor()> -350 and ball.ycor()>(player_1.ycor()-60) and ball.ycor()<(player_1.ycor()+60):
        ball.setx(-340)
        ball_dx*=-1
    #WITH PLAYER 2
    if ball.xcor()>340 and ball.xcor()< 350 and ball.ycor()>(player_2.ycor()-60) and ball.ycor()<(player_2.ycor()+60):
        ball.setx(340)
        ball_dx*=-1
    #score handling
    if (ball.xcor()>390):
        ball.goto(0, 0)
        ball_dx *= -1 #تبدا جولة جديدة و الكرة في اتجاه جديد 
        score.clear()
        p1_score+=1
        score.write(f"player_1:{p1_score}, player_2:{p2_score}", align="center", font=("courier",14,"normal"))  # al f tasmahli ndir variable da5al al string w da5al al {} al variable
        
    if (ball.xcor()<-390):
        ball.goto(0, 0)
        ball_dx *= -1  
        score.clear()
        p2_score+=1
        score.write(f"player_1:{p1_score}, player_2:{p2_score}", align="center", font=("courier",14,"normal"))
          