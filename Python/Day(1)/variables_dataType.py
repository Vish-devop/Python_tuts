'''
Features of Python: 
1. Dynamic Type lang
2. It uses interpreter not compiler.
    - Compiler : that runs at the end. 
    - Interpretor : your language / code will run line-by-line. 
3. This lang supports : OOPS + Functions + Procedural lang. 
'''

'''
Variables && Data-types :: 

(Variable) : 
-> Keyword 
-> In python, variables are been termed as objects ... ..
-> (use-case) : To store some value in memory.

NOTE: 
- In python, everything is a an object. 


(Data-Type) : 
-> keyword, which tells which type of value a variable is storing. 
-> (4) types: 
    - Numeric Datatype : 
        - (int), (float), (Complex numbers)
    - Sequence Type Data-types: 
        - String, Tuple, list
    - Dictionary
    - Boolean 
    - Set  
'''
# e.g. : 
greeting = "Welcome to first class"  # variable(1): greeting having a value : "Welcome to first class" which is having a data-type as "String" 

day_number = 1  # variable(2): day_number having a valuye : 1, which is having a data-type as inttger. 

'''
# How should I prrint these variables ?? 
# in-order to print, you can use a built-in mnethod (or, function) : print() 

print(): in python, is simillar to System.out.println() in java. 
which means, by-default print() will break the line after execution of anything in python. 
'''

print(greeting) 
print(day_number) 

'''
In python, we don't need to define anything, because  Python is a dynamic type lang..... 

(Type lang):
-> Concept,
-> that tell how a variable should behave at time of execution. 
-> (2) type : 
    -- static type 
        --- where, data-type is been checked at the time of code. 
    -- dynamic type 
        --- where, the data-type gets checked with the variable. 

'''

# How to check the type of the variable ?? 
# For, that we have a function / method : type() 

print(type(greeting), type(day_number))

'''
How to take the input from the user?? 
for that we have a function : input() 
By-default : input() only takes string values.. 
'''
name = input("Please enter your name: ")
# print("Welcome to Python series that will make you anaconda : ", name)

integer = input("Enter any number: ")
print(type(integer))   # output : "5" na- ki : 5 

# Let's do the addition of two numbers: 
n1 = input("Enter the number1: ")  # -> n1 = 1 -> '1'
n2 = input("Enter the number2: ")  # -> n2 = 1 -> "1" 
sum = n1+n2  # -> "1" + "1" = "11"
print("Addition of two numbers: ", sum)
print(type(sum))  