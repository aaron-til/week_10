# -*- coding: utf-8 -*-

# Created by Aaron Tilson
# Create an application that refances a txt document to create an address book


basedir = "C:\\dev\\addbook\\"

print("Welcom to your digital address book:\n")

project = input("Please enter the name of your address book\n")
file = project + ".txt"

if (os.path.isdir(basedir)):
    print("Your directory has been found")
else:
    print("Your directory  does not exist, I will make it for you\n")
    os.mkdir(basedir)

while name != "done":
    print("enter done if done entering information")
    name = input("Please enter the person's name:\n")
    address = input("Please enter the person's address:\n")
    phone = input("please enter teh person's phone number:\n")

log_entrery = name + "," + address + "," + phone

completePath = basedir + file

with open (completePath, "a") as fileHandle:
    fileHandle.write(log_entrery + "\n")

print("Your address book has been updated with the following information:/n")

with open (completePath, "r") as readHandle:
    for line = readHandle.read:
        print(line.strip())
