
import os
#heres a explanation,
#So first it attempts to open a file and if that fails it quits existing. Then it creates a table wich is where all the data is gonna be, you can see it like this
# ['import discord', clie...]
# In the 3rd step of the process the file is scanned line by line for ":> ;> token and even ::" it will parse these commands into something readable by discord then append them to the table
#in the 4th and final step of the process, it takes a output file and parses the table into the file, and writes to it. 
"""I wrote the above notes before knowing the triple quote existed

coming back on this im now working on Disclang2 wich is basicly just a rewrite with more functionality and the potential to be an actual language (if you put enough time into making it, its still designed around making discord bots)
"""



#OKAY, 5TH REWRITE LETS GOOOOOO
#Finally, its done, though im not done.

try:
    print('If you are coming from the community tab click show files and look at example.dss and example.py')
    file = open(input("File? "), "r")
except:
    print("Failed!")
    quit()
#this time im gonna append it all to a table
table = [
'import discord', 
'client = discord.Client()', 
'@client.event',
'async def on_message(l):', 
'  c = l.content.lower()'
]

l = file.readlines()
importstable = []
for line in l:
    currentlinea=line
    for i in importstable:
      exec(f"import {i}")
      exec(f"oiuy = {i}.readline({currentlinea})")
      table.append(oiuy)
    line = str(line)
    #note
    if line.startswith("::"):
        k = line.split("::", 1)[1]
        table.append(f"#Note, {k}")
    if line.startswith(":{}"):
      k = line.split("{")[1]
      k = k.split("}")[0]
      print("Using " + k)
      importstable.append(k)
    #message
    if line.startswith(":>"):
        #split to 2 vars
        line = line.replace(" ", "")
        line = line.replace("%20", " ")
        a = line.split(":>")[1]
        a = a.split(">>>")[0]
        b = line.split(">>>")[1]
        #print(a + " IMAGINE " + b)
        table.append(f"  if c == '{a}':")
        table.append(f"    l.channel.send('{b}')")

    #reply
    if line.startswith(";>"):
        #split to 2 vars
        line = line.replace(" ", "")
        line = line.replace("%20", " ")
        a = line.split(";>")[1]
        a = a.split(">>>")[0]
        b = line.split(">>>")[1]
        table.append(f"  if c == '{a}':")
        table.append(f"    l.reply('{b}')")
        #print(a + " IMAGINE " + b)
    if line.startswith("token"):
      a = line.split("token ")[1]
      table.append(f"client.run('{a}')")
      

#WHEN PARSING TABLE DO NOT FORGET TO REMOVE \n
#finally I can do the table
print()

try:
    outt = input("Output: ")
    file = open(outt, "x")
except:
    print("Failed!")
    quit()
for i in table:
    i = i.replace("\n", "")
    file.write(i)
    file.write(os.linesep)
file.close()

#interpret?
#for i in table:
#  exec(i)
#yeah nope, 
print("Done!")
