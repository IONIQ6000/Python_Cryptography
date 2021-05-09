# This code covers question 3 on assignment 1
Xstream = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # The X,Y,Z streams provided from the assignment
Ystream = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
Zstream = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
print("The original contents of X,Y,Z from Question 3 \n ")
print("X = (x0,x1,...,x18) = ", *Xstream, sep="", )
print("Y = (y0, y1,..., y21) = ", *Ystream, sep="", )
print("Z = (z0, z1,..., z22) = ", *Zstream, sep="", )
finalbits = []
bitclock = 0  # The variable that determines how many times the code will run.
maj = []


def majvote(bit_list):  # This function determines the majority of the X8, Y10 and Z10 values for stepping the streams
    index, center = 0, 1

    for i in range(1, len(bit_list)):
        if bit_list[index] == bit_list[i]:
            center += 1
        else:
            center -= 1
            if center == 0:
                index = i
                center = 1

    return bit_list[index]


while bitclock <= 64:
    maj.extend((Xstream[8], Ystream[10], Zstream[10]))
    supermaj = (majvote(maj))
    maj = []

    if Xstream[8] == supermaj:
        Xstream.insert(0, (Xstream[13] ^ Xstream[16] ^ Xstream[17] ^ Xstream[18]))

    if Ystream[10] == supermaj:
        Ystream.insert(0, (Ystream[20] ^ Ystream[21]))

    if Zstream[10] == supermaj:
        Zstream.insert(0, (Zstream[7] ^ Zstream[20] ^ Zstream[21] ^ Zstream[22]))

    if len(Xstream) > 19:
        Xstream.pop()
    if len(Ystream) > 22:
        Ystream.pop()
    if len(Zstream) > 23:
        Zstream.pop()

    finalbits.append(
        Xstream[18] ^ Ystream[21] ^ Zstream[22])
    bitclock += 1

print()
print()
print(f"The next {str(bitclock - 1)} keystream bits and the contents of X,Y,Z after {str(bitclock - 1)} steps\n ")
print("Keystream bits = ", *finalbits, sep="", )
print()
print("X = (x0,x1,...,x18) = ", *Xstream, sep="", )
print("Y = (y0, y1,..., y21) = ", *Ystream, sep="", )
print("Z = (z0, z1,..., z22) = ", *Zstream, sep="", )
