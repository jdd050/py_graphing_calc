import matplotlib.pyplot as plt
import re, sympy

class Main:
    def __init__(self, equation):
        # define equation strings
        self.equation = re.sub(r" ", r"", equation)
        return None
    
    # retrieve vWin size
    def getDomain(self):
        # get canvas
        window = plt.get_current_fig_manager()
        vWinCanvas = window.canvas
        # get dimensions
        dimensions = vWinCanvas.get_width_height()
        xCoorIter = -dimensions[0]
        # create xCoord list
        self.domain = []
        while xCoorIter <= dimensions[0]:
            self.domain.append(xCoorIter)
            xCoorIter += 0.05
        return self.domain
    
    # translate operators
    def translateOps(self):
        # nested multiplication w/ coeff
        nestedMatches = re.findall(r"\d+" + r"[a-zA-Z]", self.equation)
        print(nestedMatches, " nested")
        for match in nestedMatches:
            nestedMatchStr = f"{match[0:len(match) - 1]}*{match[-1]}"
            self.equation = re.sub(match, nestedMatchStr, self.equation)
        
        # distributive property number
        distMatches = re.findall(r"\d+\(", self.equation)
        print(distMatches, " distributive num")
        for match in distMatches:
            distMatchStr = f"{match[0:len(match) - 1]}*{match[-1]}"
            self.equation = re.sub(re.escape(match), distMatchStr, self.equation)

        # distributive property variable
        distMatches = re.findall(r"[a-zA-Z]+\(", self.equation)
        print(distMatches, " distributive var")
        for match in distMatches:
            distMatchStr = f"{match[0:len(match) - 1]}*{match[-1]}"
            self.equation = re.sub(re.escape(match), distMatchStr, self.equation)
        
        # pow
        powMatches = re.findall(r"\^" + r"\d+", self.equation)
        print(powMatches, " pow")
        for match in powMatches:
            powMatchStr = f"**{match[-1]}"
            self.equation = re.sub(re.escape(match), powMatchStr, self.equation)
            
        # factorial
        factorialMatches = re.findall(r"\d+\!", self.equation)
        print(factorialMatches, " factorial")
        for match in factorialMatches:
            cleanFactorial = re.sub("!", "", match)
            # calculate any operations and convert to int
            clearOp = eval(cleanFactorial)
            if clearOp < 2_147_383_647: # prevent overflow
                try:
                    calcFactorial = float(sympy.factorial(clearOp))
                except ValueError:
                    print("Factorial omitted due to ValueError. Likely caused by complex result.")
                
                # replace factorial with calculated value
                self.equation = re.sub(match, str(calcFactorial), self.equation)
                    
        return self.equation

    # translate common functions
    def translateFuncs(self):
        # log
        sympy.log()
        return

    # find variable letter for eval() global declaration
    def findVar(self):
        for char in self.equation:
            if char.isalpha() == True:
                self.eqVar = char
                break
            else:
                self.eqVar = self.equation

    # calculate values given f(x)
    def evalFunction(self):
        # create dictionary of values and find var char
        Main.findVar(self)
        self.funcValues = {}
        # calculate func value and add to dict
        for coord in self.domain:
            value = eval(self.equation, {}, {self.eqVar: coord}) 
            self.funcValues[coord] = value
            
        return self.funcValues 

# get equation
equation = input("Enter equation:\n")
while equation == "":
    equation = input("Enter equation:\n")
    pass

main = Main(equation) # class instance

# clean entire string
i = 0
while i < 2:
  cleanedEq = main.translateOps()
  i += 1
# func calls
domain = main.getDomain()
funcValues = main.evalFunction()

# graph function
plt.plot(funcValues.keys(), funcValues.values())
plt.show()