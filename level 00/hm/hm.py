from turtle import *
#გავაკეთოთ სახლი
width(8)
speed(10)
color("gray")
bgcolor("cyan")
begin_fill()
forward(200)

right(90)
forward(200)
right(90)
forward(200)

right(90)
forward(200)

right(90)
forward(200)
end_fill()
#გადაიტანეთ პასტა კარების დასახატად
penup()
goto(125,-200)
pendown()

# დავხატოთ კარები
color("white")
begin_fill()

left(90)
forward(110)
left(90)
forward(50)
left(90)
forward(110)
end_fill()

#გადავიტანოთ სახურავზე
color("black")
penup()
goto(0,0)
pendown()

#დავხატოთ სახურავი
begin_fill()
left(140)
forward(170)
right(105)
forward(158)
end_fill()

#გადავიტანოთ ბალახზე

color("black")
width(100)
penup()
goto(-500,-425)
left(80)
forward(89)
right(190)
pendown()

exitonclick()