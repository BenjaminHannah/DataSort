UPPER_list = []
LOWER_list = []
DIGIT_list = []

UPPER_length = 0
LOWER_length = 0
DIGIT_length = 0

f = open("data.txt")
chars = []
for line in f:
    chars.extend(line)

for i in chars:
    i = ord(i)
    if i >= 65 and i <= 91:
        UPPER_list.append(i)
    elif i >= 97 and i <= 123:
        LOWER_list.append(i)
    elif i >= 48 and i <= 58:
        DIGIT_list.append(i)

for i in UPPER_list:
    UPPER_length = UPPER_length + 1
    
print "Upper =",UPPER_length

for i in LOWER_list:
    LOWER_length = LOWER_length + 1
    
print "Lower =",LOWER_length

for i in DIGIT_list:
    DIGIT_length = DIGIT_length + 1
    
print "Digit =",DIGIT_length


