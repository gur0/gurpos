s = input()

vowels = ['a', 'e', 'i', 'o', 'u']
alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]

for x in s:
    if x in vowels:
        print("vowel")
    elif x in alphabet:
        print("consonant")
    else:
        break