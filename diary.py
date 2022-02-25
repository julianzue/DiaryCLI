import os
import time
from colorama import Fore, init

init()

y = Fore.LIGHTYELLOW_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
c = Fore.LIGHTCYAN_EX
R = Fore.RESET

if not os.path.isdir("Data"):
    os.system("mkdir Data")

def zero(number):
    if number < 10:
        out = "00" + str(number)
    elif number < 100:
        out = "0" + str(number)
    else:
        out  = str(number)

    return out

class Diary():
    def __init__(self):
        x = input(y + "[+] > " + R)

        splitted = x.split("  ")

        if splitted[0] == "add":
            self.add(splitted[1])

        elif splitted[0] == "list":
            self.listfiles("read")

        elif splitted[0] == "read-current" or splitted[0] == "r":
            name = time.strftime("%Y-%m-%d") + ".txt"
            self.readfile(name)

        elif splitted[0] == "exit":
            print("")
            print(r + "[*] |" + R + " Application Closed!")
            print("")
            quit()

        elif splitted[0] == "help":
            self.help()

        elif splitted[0] == "clear":
            os.system("clear")

            self.__init__()

        elif splitted[0] == "edit":
            self.listfiles("edit")

        else:
            print("")
            print(r + "[*] |" + R + " Unknown command!")
            print("")
            self.__init__()

    def add(self, text):
        print("")

        if os.path.isfile("Data/" + time.strftime("%Y-%m-%d") + ".txt"):
            for file in os.scandir("Data"):
                if file.name == time.strftime("%Y-%m-%d") + ".txt":
                    open_file = open("Data/" + file.name, "a")
                    open_file.write(time.strftime("%H:%M:%S") + " | " + text + "\n")
                    print(g + "[*] | " + R + "Successfully written to " + c + time.strftime("%Y-%m-%d") + ".txt" + R)
                    open_file.close()
        else:
            os.system("touch Data/" + time.strftime("%Y-%m-%d") + ".txt")
            print(g + "[*] | " + R + "Created "+ c + time.strftime("%Y-%m-%d") + ".txt" + R)
            self.add(text)

        print("")

        self.__init__()

    def listfiles(self, command):
        count = 0
        files = []

        print("")

        for file in os.scandir("Data"):
            files.append(file.name)

        files.sort()

        for file in files:
            count += 1
            print(zero(count) + " | " + file)

        print("")
            

        x = int(input(y + "[+] | Enter Number: " + R))

        if command == "read":
            self.readfile(files[(x - 1)])
        elif command == "edit":
            self.edit(files[(x - 1)])

    def readfile(self,filename):
        file = open("Data/" + filename, "r")
        count = 0

        print("")
        print(filename)
        print("-"*len(filename))

        for line in file.readlines():
            count += 1
            print(zero(count) + " | " + line.strip("\n"))
        
        print("")
            
        self.__init__()

    def help(self):
        print("")
        print("Help")
        print("----")
        print("")

        print(c + "add  <sentence to add>" + R)
        print("Append Sentence to current file")
        print("")
        print(c + "list" + R)
        print("Lists all data files")
        print("")
        print(c + "read-current" + R + " | " + c + "r" + R)
        print("Read current file")
        print("")
        print(c + "exit" + R)
        print("Closes this Program")
        print("")
        print(c + "help" + R)
        print("Shows this help page")
        print("")
        print(c + "edit" + R)
        print("List files to edit with nano")
        print("")
        print(c + "clear" + R)
        print("Clears the screen")

        print("")

        self.__init__()

    def edit(self, command):
        os.system("gnome-terminal -- nano Data/" + command)
        print("")
        print(g + "[*] | " + R + "Successfully opened " + c + "nano" + R + " with " + c + command + R)
        print("")

        self.__init__()

Diary().__init__()
