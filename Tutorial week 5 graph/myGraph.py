from graphics import *   #import the graphics.py module (must be in the same folder this file)


#OPEN THE WINDOW
win = GraphWin("My First Graphics Window", 800, 600)#open a window object called "win" with size and title 
win.setBackground("Mint Cream")# Set the background colour of the window

my_heading = Text(Point(80, 30), 'My Heading') #Define some text.
my_heading.draw(win)                                    #style the heading
my_heading.setTextColor("grey")
my_heading.setSize(15)
my_heading.setStyle("bold")
my_heading.setFace("helvetica")


my_sub_heading = Text(Point(90, 60), 'My Sub heading')  
my_sub_heading.setTextColor("grey")
my_sub_heading.setSize(13)
my_sub_heading.setStyle("bold")
my_sub_heading.setFace("helvetica")
my_sub_heading.draw(win)                                        #Render text to the window

a_Circle = Circle(Point(150,300), 100)                          #Define circle: centre at 150px 300px radius is 100px.
a_Circle.setFill("Lime")
a_Circle.setWidth(0)
a_Circle_label = Text(Point(150,300), "90")
a_Circle_label.setTextColor("white")
a_Circle_label.setSize(20)
a_Circle_label.setStyle("bold")                                            
a_Circle.draw(win)
a_Circle_label.draw(win) 

b_Circle = Circle(Point(400,300), 120)                          #define a second circle
b_Circle.setFill("Lime")
b_Circle.setWidth(0)
b_Circle_label = Text(Point(400,300), "140")
b_Circle_label.setTextColor("white")
b_Circle_label.setSize(20)
b_Circle_label.setStyle("bold")     
b_Circle.draw(win)                                              #Render the circle to to the window
b_Circle_label.draw(win) 

c_Circle = Circle(Point(600,300), 140)                          #define a second circle
c_Circle.setFill("Pink")
c_Circle.setWidth(0)
c_Circle_label = Text(Point(600,300), "170")
c_Circle_label.setTextColor("white")
c_Circle_label.setSize(20)
c_Circle_label.setStyle("bold")      
c_Circle.draw(win)                                              #Render the circle to to the window
c_Circle_label.draw(win)

win.getMouse()
win.close()