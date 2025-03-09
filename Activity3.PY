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