import datetime

with open("register.txt", mode='a') as file:
    file.write('(%s) recorded at:   %s.\n' % 
               ("working", datetime.datetime.now()))