with open('Codingal.txt','w')as file:
    file.write("Hi! I am penguin of 1 yr")
    file.close()

with open('Codingal.txt','r')as file:
  data= file.readlines()
print("Words in this file are....")
for line in data:
    word= line.split()
    print(word)
    file.close()
    new_file = open('New_File.txt', 'x')
new_file.close()

import os
print("Checking if My file exists or not....")
if os.path.exists("My_file.txt"):
    os.remove("My_file.txt")
else:
    print("The file does not exist")

My_file = open("My_file.txt", "w")
My_file.write("Hi! I am penguin of 1 yr")
My_file.close()

os.remove('Codingal.txt')
outputFile = open('UpdatedFile.txt' , 'w')
InputFile = open('Repeated.txt','r')

lines_seen_so_far = set()
print("Eliminating duplicate lines....")
for line in InputFile:

        if line not in lines_seen_so_far:
                outputFile.write(line)

                lines_seen_so_far.add(line)

InputFile.close()
outputFile.close()