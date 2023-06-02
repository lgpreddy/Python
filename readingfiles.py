# from sys import argv
#
# script, UserName = argv
#
# print(f"Hello {UserName}, How are you?. I am {script} file")
# print()
#
# prompt = "?;  "
#
# print("Can I ask you a few questions? ")
# print()
#
# Answer = input(prompt)
#
# print(f"Where do you live, {UserName}?")
#
# lives = input(prompt)
#
# print(f"What do you do, {UserName}?")
# job = input(prompt)
#
# print()
# print(f"I live in {lives}, and I am a {job} developer")
# print()
# print()
#
# print(f"""Hey what's up {UserName}?.
# I am Happy where I am.
# I am from {lives}.
# I use {job}.""")


# from sys import argv
#
# script, filename = argv
# txt = open(filename)
#
# print(f"Here's your file {filename}:", "w")
# print()
# print(txt.read())
# print()
#
#
#
# print()

#Here we are importing args 

from sys import argv

#Here unpacking the args and assigning 

script, filename = argv

#format string to display the message
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.") 
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")
print("I'm going to write these lines in the file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print("And finally, we close it")
target.close()



