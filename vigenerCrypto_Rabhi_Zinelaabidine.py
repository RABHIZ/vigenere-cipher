# Rabhi_Zinelaabidine_code
from tkinter import *
from tkinter import messagebox
import re

vg = Tk()
vg.geometry("900x600")
vg.title("Vigenére Cryptosystem_Rabhi_Zinelaabidine_G02")
vg.resizable(width="false", height="false")
vg.config(bg="lightgrey",relief='solid',borderwidth=2)
alphabets = "abcdefghijklmnopqrstuvwxyz"

# les Fonction
def Encrypt(p, k):  #The encryption process requires the key and the Plaintext
    c = ""
    kpos = []
    k=k.lower()
    for x in k:
        kpos.append(alphabets.find(x))
    i = 0
    for x in p:

            if i == len(kpos):
                i = 0
            if not alphabets.find(x) == -1:   # If it x is found in the list alphabet
                pos = alphabets.find(x) + kpos[i]
                if pos > 25:
                    pos = pos - 26

                c += alphabets[pos]
                i += 1
            else:
                c += x
    return c

def Decrypt(key, message):

    p = []
    keyIndex = 0
    key = key.lower()

    for symbol in message:
        num = alphabets.find(symbol.lower())
        if num != -1:
            num -= alphabets.find(key[keyIndex])
            num %= len(alphabets)
            if symbol.islower():
                p.append(alphabets[num])
            elif symbol.islower():
                p.append(alphabets[num].lower())

            keyIndex += 1
            if keyIndex == len(key):
                keyIndex = 0
        else:
            p.append(symbol)

    return ''.join(p)


def cryptanalysis():
    ciphertext = entry4.get("1.0", "end-1c")
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()
    for word in words:
        word = word.strip()  # Remove the newline at the end.
        decryptedText = Decrypt(word, ciphertext)
        if Is_English(decryptedText, wordPercentage=40):
            entry2.delete("1.0", "end")
            entry3.delete("1.0", "end")
            entry2.insert(END, decryptedText)
            entry3.insert(END, str(word))


Upperalphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabets_AND_SPACE = Upperalphabets + Upperalphabets.lower() + ' \t\n'

def AddDictionary():
    DictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in DictionaryFile.read().split('\n'):
        englishWords[word] = None
    DictionaryFile.close()
    return englishWords

ENGLISH_WORDS = AddDictionary()

def GetEnglishCount(message):
    message = message.upper()
    message = Remove_Non_Alphabets(message)
    PossibleWords = message.split()

    if PossibleWords == []:
        return 0.0 # No words at all, so return 0.0.

    matches = 0
    for word in PossibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(PossibleWords)

def Remove_Non_Alphabets(message):
    AlphabetsOnly = []
    for symbol in message:
        if symbol in alphabets_AND_SPACE:
            AlphabetsOnly.append(symbol)
    return ''.join(AlphabetsOnly)

def Is_English(message, wordPercentage=20, letterPercentage=85):

    wordsMatch = GetEnglishCount(message) * 100 >= wordPercentage
    numalphabets = len(Remove_Non_Alphabets(message))
    messagealphabetsPercentage = float(numalphabets) / len(message) * 100
    alphabetsMatch = messagealphabetsPercentage >= letterPercentage
    return wordsMatch and alphabetsMatch


def Take_input():   # Function that allows me to enter Plaintext and the key
    INPUT = entry2.get("1.0", "end-1c")
    d=INPUT
    INPUT=INPUT.replace(" ","")
    INPUT = INPUT.lower()
    INPUT2 = entry3.get("1.0", "end-1c")
    INPUT2 = INPUT2.replace(" ", "")
    if not INPUT2.isalpha():
            messagebox.showerror('Only alphabets', 'Only alphabets are allowed in the key!')
    else:
            entry4.delete("1.0", "end")
            c = Encrypt(INPUT, INPUT2)
            indexes = [x.start() for x in re.finditer(' ', d)]     #Add white spaces in the plaintext
            for i in indexes:
                c = c[:i] + " " + c[i:]
            entry4.insert(END, c)

def Take_input1():   # Function that allows me to enter Ciphertext and the key
    INPUT = entry4.get("1.0", "end-1c")
    d = INPUT
    INPUT = INPUT.replace(" ", "")
    INPUT = INPUT.lower()
    INPUT2 = entry3.get("1.0", "end-1c")
    INPUT2 = INPUT2.replace(" ", "")
    if not INPUT2.isalpha():
            messagebox.showerror('Only alphabets', 'Only alphabets are allowed in the key!')
    else:
            entry2.delete("1.0", "end")
            c = Decrypt(INPUT2, INPUT)
            indexes = [x.start() for x in re.finditer(' ', d)]  #Add white spaces in the ciphertext
            for i in indexes:
                c = c[:i] + " " + c[i:]

            entry2.insert(END, c)

# Began Interface Graphics
# position label && Text Box
l1 = Label(text="Vigenére\n Cryptosystem", font=("serif", 14), fg="red", bg="lightgrey")
l1.pack()
l1.place(x=10, y=10)

l2 = Label(text="Plaintext", font=("serif", 14), bg="lightgrey")
l2.pack()
l2.place(x=210, y=12)
entry2 = Text(vg, font=("serif", 14), relief='solid')
entry2.pack()
entry2.place(width=500, height=200, x=300, y=11)

l3 = Label(text="key", font=("serif", 14), bg="lightgrey")
l3.pack()
l3.place(x=255, y=270)
entry3 = Text(vg, font=("serif", 14), relief='solid')
entry3.pack()
entry3.place(width=150, height=30, x=300, y=270)

l4 = Label(text="Ciphertext", font=("serif", 14), bg="lightgrey")
l4.pack()
l4.place(x=201, y=350)
entry4 = Text(vg, font=("serif", 14), relief='solid')
entry4.pack()
entry4.place(width=500, height=200, x=300, y=350)

# button

b1 = Button(vg, text="Encrypt", font=("serif", 14), bg="orange", command=lambda: Take_input(),relief='raised', borderwidth=5)
b1.pack()
b1.place(x=150, y=100)

b2 = Button(vg, text="Decrypt", font=("serif", 14), bg="orange", command=lambda: Take_input1(),relief='raised', borderwidth=5)
b2.pack()
b2.place(x=150, y=450)

b3 = Button(vg, text="Cryptanalysis", font=("serif", 14), bg="orange", command=lambda: cryptanalysis(), relief='raised', borderwidth=5)
b3.pack()
b3.place(x=150, y=500)
#End Button
# End_Interface Graphics//

vg.mainloop()