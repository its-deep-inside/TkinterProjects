import random
import string
import pyperclip
from tkinter import *

root = Tk()
root.title("Password Generator")
root.geometry("400x400")
root.resizable(False, False)

# password generation function
def GeneratePassword(**kargs):
    try:
        key = ""
        temp = []

        if(kargs['uppercase']):
            temp.extend(list(string.ascii_uppercase))   
        if(kargs['lowercase']):
            temp.extend(list(string.ascii_lowercase))   
        if(kargs['number']):
            temp.extend(list(string.digits))   
        if(kargs['symbol']):
            temp.extend(list(string.punctuation))   

        if kargs['length'] < 1:
            kargs['length'] = 1

        for _ in range(kargs['length']):
            key += random.choice(temp)

        passwordKey.set(key)
    except ValueError and IndexError:
        pass

# function to copy password
def CopyToClipBoard(*args):
    pyperclip.copy(passwordKey.get())


# creating heading
Label(root, text="Password Generator", font="Consolas 18 underline").grid(row=0, column=0, pady=20, columnspan=3)

# creating input
# password
passwordKey = StringVar()
passwordGen = Entry(root, textvariable=passwordKey, justify=CENTER, font="Consolas 16")
passwordGen.insert(0, "Generated Password")
passwordGen.config(state="readonly")
passwordGen.grid(row=1, column=0, columnspan=2, padx=(30, 5), pady=(20, 0), sticky=NSEW)

# copy button
copyBtn = Button(root, text="COPY", font="Consolas 16", command=CopyToClipBoard)
copyBtn.grid(row=1, column=2, padx=(5, 30), pady=(20, 0), sticky=NSEW)

# password length
Label(root, text="Password Length", font="Consolas 14").grid(row=2, column=0, padx=30, pady=(20, 0), sticky=W)
passLen = IntVar()
passLenE = Spinbox(root, from_=8, to_=32, textvariable=passLen, font="Consolas 14", width=6)
passLenE.grid(row=2, column=1, columnspan=2, padx=30, pady=(20, 0), sticky=E)

# password uppercase
Label(root, text="UpperCase", font="Consolas 14").grid(row=3, column=0, padx=30, sticky=W)
upperCase = BooleanVar()
upperCaseR = Checkbutton(root, variable=upperCase)
upperCaseR.grid(row=3, column=1, columnspan=2, padx=30, sticky=E)
upperCaseR.select()

# password lowercase
Label(root, text="LowerCase", font="Consolas 14").grid(row=4, column=0, padx=30, sticky=W)
lowerCase = BooleanVar()
lowerCaseR = Checkbutton(root, variable=lowerCase)
lowerCaseR.grid(row=4, column=1, columnspan=2, padx=30, sticky=E)
lowerCaseR.select()

# password numbers
Label(root, text="Numbers", font="Consolas 14").grid(row=5, column=0, padx=30, sticky=W)
numbers = BooleanVar()
numbersR = Checkbutton(root, variable=numbers)
numbersR.grid(row=5, column=1, columnspan=2, padx=30, sticky=E)
numbersR.select()

# password symbols
Label(root, text="Symbols", font="Consolas 14").grid(row=6, column=0, padx=30, sticky=W)
symbols = BooleanVar()
symbolsR = Checkbutton(root, variable=symbols)
symbolsR.grid(row=6, column=1, columnspan=2, padx=30, sticky=E)
symbolsR.select()

# password generation btn
generateBtn = Button(root, text="Generate", font="Consolas 14", command=lambda: GeneratePassword(uppercase=upperCase.get(), lowercase=lowerCase.get(), number=numbers.get(), symbol=symbols.get(), length=passLen.get()))
generateBtn.grid(row=7, column=0, columnspan=3, padx=30, pady=(20, 0), sticky=NSEW)

root.columnconfigure(0, weight=1)
root.mainloop()