from collections import OrderedDict

freq = {} 
letters = {}
#The plain text below to be decrypted
plain = 'PBFPVYFBQXZTYFPBFEQJHDXXQVAPTPQJKTOYQWIPBVWLXTOXBTFXQWAXBVCXQWAXFQJVWLEQNTOZQGGQLFXQWAKVWLXQWAEBIPBFXQVXGTVJVWLBTPQWAEBFPBFHCVLXBQUFEVWLXGDPEQVPQGVPPBFTIXPFHXZHVFAGFOTHFEFBQUFTDHZBQPOTHXTYFTODXQHFTDPTOGHFQPBQWAQJJTODXQHFOQPWTBDHHIXQVAPBFZQHCFWPFHPBFIPBQWKFABVYYDZBOTHPBQPQJTQOTOGHFQAPBFEQJHDXXQVAVXEBQPEFZBVFOJIWFFACFCCFHQWAUVWFLQHGFXVAFXQHFUFHILTTAVWAFFAWTEVOITDHFHFQAITIXPFHXAFQHEFZQWGFLVWPTOFFA'

for i in plain: #counting all the letters in their frequency
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1

for x in plain: #counting all the letters
    if x in letters: 
        letters[x] += 1
    else: 
        letters[x] = 1

ordered = OrderedDict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

print("The plaintext :")
print(plain)
print()
print ("Count of all characters in the plaintext sorted by decending frequency :")
print(' '.join("{}:{}".format(k, v) for k, v in ordered.items()))
print()
print("The goal here is to use a key to unravel the original message by using the find and replace function.")
print("Note: please remember to not replace a letter twice.")
print()
letters = {}
letter_list = []
replace_list = []
for x in plain: 
    if x in letters: 
        letters[x] += 1
    else: 
        letters[x] = 1

while True:
    print ("Count of all characters in the plaintext sorted by decending frequency :")
    print(' '.join("{}:{}".format(k, v) for k, v in ordered.items()))
    print()
    print(plain.upper())
    print()
    print("Letter you have looked for  " + str(letter_list).upper())
    print("What you replaced them with " + str(replace_list).upper())
    print()

    find = input("Enter letter to find: ")
    while find.upper() in letter_list or find.lower() in letter_list :
        find = input("You already looked for " + find.upper() + "! Enter letter to find: ")
    
    letter_list.append(find)
    
    replace = input("Enter letter to replace: ")
    replace_list.append(replace)
    print()
    find = find.upper()
    replace = replace.upper()

    plain = plain.replace(find, replace.lower())
    
    print(plain.upper())
    print()
    if input("Do You Want To Continue? [y/n]") == "y":
        print()
        continue
    else:
        print()
        print("The final message: \n")
        print(plain.upper())
        print()
        print("The key so far:")
        print(str(replace_list).upper())
        print(str(letter_list).upper())
        break