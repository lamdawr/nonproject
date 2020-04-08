#### Factorial of a number #####

def factorial_num(num):
    return num if (num <=1) else (num*factorial_num((num-1)))

print(factorial_num(5))

#### Sort list of strings by the length of string #####

List1 = ['sun','mon','tues','wed','thurs','fri','sun','mon','tues','sun','mon','tues','sun','mon','tues']

List1.sort(key = lambda s:len(s))

print(List1)


#### Sort list of strings by their last char ####

List1 = ['sun','mon','tues','wed','thurs','fri','sun','mon','tues','sun','mon','tues','sun','mon','tues']

List1.sort(key = lambda x:x[-1])

print(List1)

