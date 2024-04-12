# imports
from grid import *
import os
from funcOperations import *

# function types
functions = "\n1. Linear \n2. Quadratic \n3. Polynomic (Under Development) \n4. Square root \n5. Exponential \n6. Logarithmic \n7. Rational (Under Development) \n8. Absolute Value \n9. Trigonometric (Under Development)"
trig = "\n1a. cos \n2a. sin \n3a. tan \n4a. cosec \n5a. sec \n6a. cot"

# get function details
class func():
    
    # get function type
    def determineFunc(self):
        # show user list of function types
        func = wn.textinput("Function", f'Please input function type: {functions}')
        
        # trig case
        if (func == "9"):
            trigFunc = wn.textinput("Trig Function", f'Please choose a trigonometric function: {trig}')
            return trigFunc
        # non trig case   
        return func
    
    # transfer function data
    userFunc = [determineFunc(None)]

    # debug
    def debug(self):
        try: # open file
            cwd = os.getcwd()
            with open("log.txt", 'a') as instance:
                instance.write(f'user function selection: {func.userFunc} \n')
                pass
        except OSError:
            print(f'OSError in {cwd} @ line 31 "func.debug"')
        finally:
            pass
        return None

    # calculations
    def doFunc(self):
        
        # prep
        draw.up()
        draw.goto(-450, -450)
        draw.color('blue')
        draw.width(2.5)
        
        
        # linear
        if func.userFunc[0] == '1':
            
            # get func vals
            m = float(wn.textinput("Function Details", "Please provide m"))
            b = float(wn.textinput("Function Details", "Please provide b"))
            x = draw.xcor()
            
            # move
            for i in range(18000):
                
                # calculate coordinate
                i = algebraicFuncs.linear(0, m, x, b)
                
                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(x) + ' || ' + str(i) + '\n')
                    pass
                
                # draw line
                if i >= 450:
                    draw.up()
                    pass
                else:
                    draw.down()
                    draw.goto(x, i)
                    draw.up()
                
                # move to next line (amount of error)
                x += 0.05
                
                pass
            pass
        
        # quadratic
        if func.userFunc[0] == '2':
            
            # get func vals
            a = float(wn.textinput("Function Details", "Please provide a"))
            h = float(wn.textinput("Function Details", "Please provide h"))
            k = float(wn.textinput("Function Details", "Please input k"))
            x = draw.xcor()
            
            # move
            for i in range(18000):
                
                # calculate coordinate
                i = (algebraicFuncs.quadratic(0, a, x, h, k)) / 45
                
                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(x) + ' || ' + str(i) + '\n')
                    pass
                
                # draw line
                if i >= 450:
                    draw.up()
                    draw.goto(x, 450)
                    pass
                else:
                    draw.down()
                    draw.goto(x, i)
                    draw.up()
                
                # move to next line (amount of error)
                x += 0.05
                
                pass
            pass
        
        # polynomic
        if func.userFunc[0] == '3':
            pass
        
        # square root
        if func.userFunc[0] == '4':
            
            # get func vals
            a = float(wn.textinput("Function Details", "Please provide a"))
            h = float(wn.textinput("Function Details", "Please provide h"))
            k = float(wn.textinput("Function Details", "Please input k"))
            x = draw.xcor()
        
            # move
            for i in range(18000):
                
                # calculate coordinate
                i = (algebraicFuncs.squareRoot(0, a, x, h, k)) * 6.70799
                
                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(x) + ' || ' + str(i) + '\n')
                    pass
                
                # draw line and check for imaginary 
                if debug.isFloat(0, i) == True:
                    # draw line
                    draw.down()
                    draw.goto(x, i)
                    draw.up()
                else:
                    draw.up()
                    draw.goto(x, k)
                    pass
                
                # move to next line (amount of error)
                x += 0.05
                
                pass
            pass
        
        # exponential
        if func.userFunc[0] == '5':
            
            # get func vals
            a = float(wn.textinput("Function Details", "Please provide a"))
            b = float(wn.textinput("Function Details", "Please provide b"))
            h = float(wn.textinput("Function Details", "Please provide h"))
            k = float(wn.textinput("Function Details", "Please input k"))
            x = draw.xcor()
        
            # move
            for i in range(18000):
                
                # calculate coordinate
                i = (algebraicFuncs.exponential(0, a, b, x, h, k))
                
                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(x) + ' || ' + str(i) + '\n')
                    pass
                
                # draw within bounds
                if x > (-450) and i <= (625):
                    # draw line
                    draw.down()
                    draw.goto(x * 45, i * 45)
                    draw.up()
                else:
                    draw.up()
                    draw.goto(x, k)
                    pass
                
                # move to next line (amount of error)
                x += 0.05
                
                pass
            pass
        
        # logarithmic
        if func.userFunc[0] == '6':
            
            # get func vals
            a = float(wn.textinput("Function Details", "Please provide a"))
            b = float(wn.textinput("Function Details", "Please provide b"))
            h = float(wn.textinput("Function Details", "Please provide h"))
            k = float(wn.textinput("Function Details", "Please input k"))
            x = draw.xcor()
        
            # prevent ma error
            if b <= 0:
                b = float(wn.textinput("Function Details", "Please provide b (non-negative greater than zero)"))
            else:
                pass
        
            # move
            for i in range(18000):
                
                # calculate coordinate
                i = (algebraicFuncs.log(0, a, b, x, h, k)) 
                
                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(x) + ' || ' + str(i) + '\n')
                    pass
                
                # draw line and check for imaginary 
                if debug.isFloat(0, i) == True:
                    # draw line
                    draw.down()
                    draw.goto(x * 45, i * 45)
                    draw.up()
                else:
                    pass
                
                    pass
                
                # move to next line (amount of error)
                x += 0.05
                
                pass
            pass
        
        # rational
        if func.userFunc[0] == '7':
            
            # get func vals
            a = float(wn.textinput("Function Details", "Please provide a"))
            b = float(wn.textinput("Function Details", "Please provide b"))
            h = float(wn.textinput("Function Details", "Please provide h"))
            k = float(wn.textinput("Function Details", "Please input k"))
            x = draw.xcor()
        
            # move
            for i in range(18000):
                
                # calculate coordinate
                i = (algebraicFuncs.rational(0, a, b, x, h, k)) * 450
                
                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(x) + ' || ' + str(i) + '\n')
                    pass
                
                # draw within bounds
                if x > -450 and i <= 625:
                    # draw line
                    draw.down()
                    draw.goto(x, i)
                    draw.up()
                else:
                    draw.up()
                    draw.goto(x, k)
                    pass
                
                # move to next line (amount of error)
                x += 0.05
                
                pass
            pass
        
        # absolute value
        if func.userFunc[0] == '8':
            
            # get func vals
            a = float(wn.textinput("Function Details", "Please provide a"))
            h = float(wn.textinput("Function Details", "Please provide h"))
            k = float(wn.textinput("Function Details", "Please input k"))
            x = draw.xcor()
            
           
            #move
            for i in range(18000):

                # calculate coordinate
                i = (algebraicFuncs.absolute(0, a, x, h, k))
                
                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(i) + '\n')
                    pass
                
                # draw line
                if i >= 450:
                    draw.up()
                    draw.goto(x, 450)
                    pass
                else:
                    draw.down()
                    draw.goto(x, i)
                    draw.up()
                
                # move to next line (amount of error)
                x += 0.05
                
                pass
            pass
        
        # sin
        if func.userFunc[0] == '1a':
            
            # get func vals
            a = float(wn.textinput("Function Details", "Please provide a"))
            b = float(wn.textinput("Function Details", "Please provide b"))
            h = float(wn.textinput("Function Details", "Please provide h"))
            k = float(wn.textinput("Function Details", "Please input k"))
            x = draw.xcor()
            
            #move
            for i in range(18000):
                
                # calculate coordinate
                i = (trigonometricFuncs.sine(0, a, b, x, h, k)) * (45)

                # debug
                with open("log.txt", 'a') as instance:
                    instance.write(str(i) + '\n')
                    pass
                
                # draw line
                if i > -450 and i <= 450:
                    draw.down()
                    draw.goto(x *45, i)
                    draw.up()
                else:
                    draw.up()
                    draw.goto(x, 450)
                    pass
                
                # amt error
                x += 0.05
                
                pass
            pass
        
        return