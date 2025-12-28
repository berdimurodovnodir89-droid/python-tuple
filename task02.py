students = [
("Ali", ["Fizika", "Matematika"]),
 ("Laylo", ["Ingliz tili"]), 
 ("Jasur", ["Matematika", "Informatika"])
 ]

subject = input('subject :')

count = 0
for student in students :
    if subject in students[1]:
     count  += 1

print(count)