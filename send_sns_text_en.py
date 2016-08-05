#!/usr/bin/python
# -*- coding: utf-8 -*-

# Program written in Python 3.5.2 (v3.5.2:4def2a2901a5, Ago 04 2016, 17:30:00)
# Written by José Ricardo

from twilio import rest
import webbrowser
import time


def msgSNS():

    title = '''
Share SNS with Twilio using Python ^ - ^

You need a Twilio account !!!

Access in: https://www.twilio.com/try-twilio
    '''

    print("")
    print(title)
    print("")


def ChoiceWeb():
    correct = False

    while (correct == False):
        i = 3
        choice = input("Do you want to access the website now? Y ou N ----->  ")
        print("")

        if (choice == "y") | (choice == "Y"):
            while (i >= 1):
                print("Accessed in: ", i)
                time.sleep(1)
                i = i - 1

            print("")
            print("Opening now!!!")
            time.sleep(1)
            webbrowser.open("https://www.twilio.com/try-twilio")
            correct = True
        else:
            if (choice == "n") | (choice == "N"):
                print("")
                print("OK we will continue!!!")
                correct = True
            else:
                print("")
                print("Enter only the characters: y or Y, n or N")
                correct = False


def ChoiceNew():
    newMsg = False

    while (newMsg == False):

        print("")
        account_sid = input("Enter your SID Twilio: ")
        print("")
        auth_token = input("Enter your Token Twilio: ")
        print("")
        msgTXT = input("Type your message: ")
        print("")
        toTXT = input("Who is your message, use a phone number? ex: +12555555 ")
        print("")
        fromTXT = input("What is your Twilio phone number? ex: +12555555 ")

        client = rest.TwilioRestClient(account_sid, auth_token)
        message = client.messages.create(
            body= msgTXT,  # Replace with your message
            to= toTXT,  # Replace with your phone number
            from_= fromTXT)  # Replace with your Twilio number

        print("")
        print("Your SID Twilio is: ")
        print(message.sid)

        print("")
        print("Your message: ")
        print(message.body)

        print("")
        print("You sent to: ")
        print(message.to)

        print("")
        print("Who sent: ")
        print(message.from_)

        print("")
        print("")
        print("End of message ^-^")

        print("")
        print("")

        correct2 = False

        while (correct2 == False):
            N_msg = input("Do you want to send another message? ------> Y ou N    ")

            if (N_msg == "y") | (N_msg == "Y"):
                correct2 = True
                newMsg = False
            else:
                if (N_msg == "n") | (N_msg == "N"):
                    print("")
                    print("End of program ^-^")
                    print("")
                    input("Press any key to end . . .")
                    newMsg = True
                    correct2 = True
                else:
                    print("")
                    print("Enter only the characters: y or Y, n or N")
                    print("")
                    correct2 = False


msgSNS()
ChoiceWeb()
ChoiceNew()