'''
1. Strings : 
    - A data-type 
    - Collection of your characters 
    - Immutable types 

2. Operations on Strings : 
    - Concatenation 
    - Slicing 

3. Strings Methods 
    - After sometime.. because if we will see right now, your mind will be fried like a fish fry (but I am vegeterian) 
'''


'''
What is a mutable and immutable data-type?? 
(immutable data-type) : 
-> aise datatypes that can't be updated / changed but they can be accessed. 
-> e.g: String, tuple 

(mutable data-types) : 
-> those data-types that can be changed and updated also in real-time.
-> list, dictionary  

'''

'''
 SLICING in strings: 
    -> to filter the strings.
    -> Sytanx : String_name[start: stop : skip] 
        -- by-dafault things: 
            - Start : 0
            - stop (end) : length of string
            - skip : 0 

    -> negative slicing : 

NOTE:  
    -> to find the length of a string we use a keyword : len() 
    -> the counting inside a string usually starts from 0 to length-1. 
'''
# eg: 
string = "HEllo, are you sleepy , do you want to lay over your bed and sleep like a small baby .. "

# total_length_of_string = len(string) 
# print(total_length_of_string)
# start_of_string = 0

# part1 = string[start_of_string : 5] 
# part2 = string[7: 21]
# part3 = string[24:total_length_of_string] # len(string) : total length of string   string[24:88]

# print("part1: ",part1)
# # print("part2: ",part2)
# print("part3: ",part3)

# negative indexing - slicing : 
# negative indexing : (shortcut) whenver it's written something like this: string[7:-1] : you can re-write this as : string[7:len(string)-1]
# eg: 
part4=string[7:-4] # string[7:len(string)-1]
part5=string[7:len(string)-4]
# print(part5)


# skipping : 
# Problem statement : I only want the characters/words which are placed at even position. 
part6=string[0:len(string): 2]
print(part6)