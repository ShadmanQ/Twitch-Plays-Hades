import socket
import pyautogui
import pydirectinput
SERVER = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:kbqp5v0mq0i0yhthpdjokam7e42hwq"
BOT = "HadesBot"
CHANNEL = "silverlungs"
OWNER = "silverlungs"

irc = socket.socket()

irc.connect((SERVER,PORT))
irc.send(("PASS " + PASS + " \n" + 
        "NICK "+ BOT + " \n" +
        "JOIN #"+CHANNEL+"\n").encode())

def joinchat():
    Loading = True
    while Loading:
        readbuffer_join = irc.recv(1024).decode()
        line = readbuffer_join
        print(line)
        Loading = loadingComplete(line)


def loadingComplete(line):
        if ("End of /NAMES list" in line):
                print("Bot has joined")
                sendMessage(irc, "Hi everyone! Good luck escaping Hell.")
                return False
        else:
                print("Bot hasn't joined yet")
                return True

def sendMessage(irc, message):
        messageTemp = "PRIVMSG #"+ CHANNEL+" : " + message
        irc.send((messageTemp + "\n").encode())
joinchat()

def test(thing):
        if thing == "w":
                pydirectinput.press("w")
        if thing == "a":
                pydirectinput.press("a")
        if thing == "s":
                pydirectinput.press("d")
        if thing == "d":
                pydirectinput.press("d")
        if thing == "e":
                pydirectinput.press("e")
        if thing == "i":
                pydirectinput.press("i")
        if thing == "j":
                pydirectinput.press("j")
        if thing == "k":
                pydirectinput.press("k")
        if thing == "l":
                pydirectinput.press("l")
        

while True:
        try:
                readbuffer_msg = irc.recv(1024).decode()
        except:
                readbuffer_msg=""
        
        for line in readbuffer_msg.split("\r\n"):
                if line == "":
                        continue
                if "PING" in line:
                        msg = "PONG tmi.twitch.tb\r\n".encode()
                        irc.send(msg)
                        print(msg)
                        continue

                else:
                        print(line)
                        command = line.split(":")[2]
                        print(command)
                        test(command)