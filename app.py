from Tkinter import *
import ttk

from googletrans import Translator

import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Counter:
	currentScore = int(0)

	def __init__(self):
		print("hello")

	def increaseIt(self):
		Counter.currentScore += 1
	def getCounterScore(self):
		return(Counter.currentScore)

getThisright = Counter()
LANG = raw_input("What language would like learn? (Two letter abbreviations ex. fr, es, du)")

with open("testfiler.txt", "r") as textFile:
    rawWordList = textFile.readlines()
    wordList = [word.rstrip() for word in rawWordList]
#getThisright = 0
def calculate(*args):
    translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])
	#getThisright = 0
	#seenArray = []
    file1 = open("testfiler.txt","r")
    theirGuess = str(inputAnswer.get())
    #seenNumber = 0
    #data = file1.readlines()

    #for i in seenArray:

    #	if(theirGuess == i):
    #		print("You already guessed that - did the scene change?")
    #		seenNumber = 1

    #if(seenNumber == 0):
    #	seenArray.append(theirGuess)
    #print(seenArray)
    data = file1.readlines()
    #print(data[4])
    for thing in data:
        #print(theirGuess)
        #print(thing)
        print(theirGuess)
        var = translator.translate(thing.strip(), src='en', dest=LANG)
        print(translator.translate(thing.strip(), src='en', dest=LANG))
        if (theirGuess in var.text):
            getThisright.increaseIt()
            print(getThisright.getCounterScore())

    #print(getThisright)
    file1.close()
    ttk.Label(mainframe, text=getThisright.getCounterScore()).grid(column=3, row=1, sticky=W)

    
    
root = Tk()
root.title("Examintation")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

inputAnswer = StringVar()
endStatus = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=inputAnswer)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=getThisright.getCounterScore()).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Submit", command=calculate).grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
