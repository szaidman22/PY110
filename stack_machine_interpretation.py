'''
n: Place an integer value, n, in the register. Do not modify the stack.
PUSH : Push the current register value onto the stack. Leave the value in the register.
ADD : Pop a value from the stack and add it to the register value, storing the result in the register.
SUB : Pop a value from the stack and subtract it from the register value, storing the result in the register.
MULT : Pop a value from the stack and multiply it by the register value, storing the result in the register.
DIV : Pop a value from the stack and divide the register value by the popped stack value, storing the integer result back in the register.
REMAINDER : Pop a value from the stack and divide the register value by the popped stack value, storing the integer remainder of the division back in the register.
POP : Remove the topmost item from the stack and place it in the register.
PRINT : Print the register value.
'''
'''
minilang('5 PUSH 3 MULT PRINT')
# 15
'''



def minilang(command_string):

    stack = []
    register = 0

    commands = ['PUSH', 'ADD', 'SUB',
                'MULT', 'DIV', 'REMAINDER',
                'POP', 'PRINT']
    
    command_list = command_string.split(' ')

    if len([word for word in command_list if word.upper() not in commands]) == 1:
        register = command_list[0]
    
    print(register)

minilang('4 PUSH 3')