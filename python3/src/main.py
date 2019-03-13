from subprocess import Popen, PIPE
from bot import Bot
import time
import random
import json
import re

fr  = open("stdout.txt", "w+")
fw  = open("stdout.txt", "w+")
err = open("stderr.txt", "w+")
in_write = open("stdin.txt", "w+")

p = Popen(["npm", "start"], stdout = fw, stderr = err)

out = ""
while 1:
    if p.poll() != None:
        break
    out += fr.read()

    if "</END>" not in out:
        time.sleep(0.1)
        continue

    print(out)
    
    data = out[:out.rfind("</END>")]
    data = data[data.rfind("<START>")+len("<START>"):].strip()
    try:
        game_state = json.loads(data)
        out = out[out.rfind("</END>")+len("</END>"):]

        choice = Bot.do_action(game_state)
        in_write.write(choice + "\n")
        in_write.flush()
        print("Sent: " + choice)
    except:
        pass 

print("terminated")