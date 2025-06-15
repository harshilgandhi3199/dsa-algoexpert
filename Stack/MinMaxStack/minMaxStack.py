# Write a MinMaxStack class for a Min Max Stack. The class should support:
# • Pushing and popping values on and off the stack.
# • Peeking at the value at the top of the stack.
# • Getting both the minimum and the maximum values in the stack at any given point in time.
# All class methods, when considered independently, should run in constant time and with constant space.

class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []
        
    def peek(self):
        # Write your code here.
        # len() method runs in O(1) time
        return self.stack[len(self.stack) - 1]

    def pop(self):
        # Write your code here.
        # pop() mehtod runs in O(1) time
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number): 
        # Write your code here.
        newMinMax = {'min': number, 'max': number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax['min'] = min(lastMinMax['min'], number)
            newMinMax['max'] = max(lastMinMax['max'], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
    
    def getMin(self):
        # Write your code here.
        return self.minMaxStack[len(self.minMaxStack) - 1]['min']

    def getMax(self):
        # Write your code here.
        return self.minMaxStack[len(self.minMaxStack) - 1]['max']
