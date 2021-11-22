message = input(">")
words = message.split(' ')
emoji = {
    ":)" : "😁",
    ":;" : "😎"
}
output = ""
for word in words:
    output += emoji.get(word , word) + " "

print(output)

#Argument in programming is the value that we supply to a function call function greet_user("Dragos") unde dragos este argumentul
#parameters are the holes or placeholders that we defind in our function for receving information ex def greet_user(name) the parameter is name