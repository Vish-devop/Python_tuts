'''
Type-Casting : 
-> Changing the type of your variable (type -> data-type) 
-> Types: 
    --> Implicit : 
        -->> (automatic conversion) : that a machine do itself. 
    --> Explicit : 
        -->> (manual conversion) : a user / programmer is trying to change / forcing to change the data-type of a variable. 

-> (very-very-very-important) : 
    -> There is a precision (the order in which data-type would be type-casted )
        --> Everytime, a small data-type can be typecasted to big one, but vice-versa will create problem and is not suggested to do. 
        --> Problem : 
            -- hr ek data-type ka size hota hain :: 
            e.g. -> float to int : 
                    -->> size of flaot : 4 bits 
                    -->> size of int : 2 bits 
                    so your outupt would be of size 2 bits only. 
                        -- means, it will only print the value which is excedding the size after 2 bits. (2+2). 
'''
#e.g. -> I need to convert string into integer. 
number1 = input("Enter the number: ")
integer_num = int(number1)  #dataType(variable_name) 
float_num = float(number1)
print(type(integer_num))
print(type(float_num)) 

