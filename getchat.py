# Code written by Austin Foulks, 8/29/2023

import privatedata
import socket
from emoji import demojize
import re

CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")

sock = socket.socket()

def StartConnection():
    # Connect socket to Twitch
    sock.connect((privatedata.server, privatedata.port))

    # Authenticate and connect to channel over socket
    sock.send("PASS {}\r\n".format(privatedata.token).encode("utf-8"))
    sock.send("NICK {}\r\n".format(privatedata.nickname).encode("utf-8"))
    sock.send("JOIN {}\r\n".format(privatedata.channel).encode("utf-8"))
    
def ConnectionCheck(msg):
    # Respond to Twitch checking if the bot is still active
    if msg == "PING :tmi.twitch.tv\r\n":
        sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    
def GetMessage():
    try:
        # Hangs until something is received
        msg = sock.recv(2048).decode("utf-8")
        print(msg)
        
    except socket.error:
        return
    
    ConnectionCheck(msg)
    
    if len(msg) > 0:
        demojize(msg)
    
    # Avoid AttributeError and TypeError
    if msg:
        # Use regex to separate string
        username = re.search(r"\w+", msg).group(0)
        message = CHAT_MSG.sub("", msg)
        print(username + ": " + message)

        # Force lowercase for less comparisons
        message = message.lower()
        
        # Remove invisible characters that mess with string comparison
        mapping = dict.fromkeys(range(32))
        clean_message = message.translate(mapping)

        return clean_message
    
def CloseSocket():
    sock.close()