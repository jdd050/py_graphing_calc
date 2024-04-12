# imports
import turtle as trtl

# turtle object
draw = trtl.Turtle()
draw.speed('fastest')
trtl.tracer(0,0)

# window object
wn = trtl.Screen()
wn.setup(900, 900)
wn.bgcolor('lightYellow')

# globals
global windowLength
global windowHeight
windowLength = trtl.window_width()
windowHeight = trtl.window_height()

# coordinate plane domain
class cp():
    
     # draw axes
    def drawAxes(self):
        
        # y-axis
        draw.seth(90)
        draw.up()
        draw.width(3)
        draw.goto(0, (-windowHeight / 2)) # go to bottom-center
        draw.down()
        draw.forward(windowHeight) # go to opposite end, drawing the axis
        draw.up()
        
        # x-axis
        draw.seth(0)
        draw.goto((-windowLength / 2), 0) # go to middle-left
        draw.down()
        draw.forward(windowLength) # go to opposite end, drawing the axis
        draw.up()
        
        return
    
    # draw grid
    def drawGrid(self):
        
        # prep for x-lines
        draw.width(1)
        draw.goto(-450, -450)
        draw.seth(90)
        draw.down()
        
        # draw x-lines
        i = 0
        while i < 20:
            
            draw.seth(90)
            draw.forward(windowLength) # step 1
            draw.seth(0) # step 2
            draw.up()
            
            draw.forward(45) # step 3
            draw.seth(270) # step 4
            
            draw.down()
            draw.forward(windowHeight) # step 5
            
            i += 1
            pass
        
        # prep for y-lines
        draw.up()
        draw.goto(-450, 450)
        draw.down()
        
        # draw y-lines
        j = 0
        while j < 20:
            
            draw.seth(0)
            draw.forward(windowLength) # step 1
            draw.seth(270) # step 2
            draw.up()
            
            draw.forward(45) # step 3
            draw.seth(180) # step 4
            
            draw.down()
            draw.forward(windowHeight) # step 5
            
            j += 1
            pass
        return
    pass