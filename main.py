#GOTO https://replit.com/@WellSilver/Disclang
#https://replit.com/@WellSilver/Disclang
#https://replit.com/@WellSilver/Disclang
#https://replit.com/@WellSilver/Disclang
#https://replit.com/@WellSilver/Disclang
#https://replit.com/@WellSilver/Disclang
#https://replit.com/@WellSilver/Disclang


#message.author.mention


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#here we get our file
out = input("File\n")
try:
  file = open(out)
except:
  print("Error!")
  quit()

#declare everything we need
lines = file.readlines()
count = 0
table = [
"import discord",
"client = discord.Client()",
"@client.event",
"async def on_message(l):"
"  c = l.content.lower()"
]

#finally we can start parsing it
for line in lines:
  #if note
  if count >= 1:
    table.append("# Note, " + line)
    continue
  try:
    if line.startswith(":k"):
      a = line.split(":k")[1]      
      a = int(str(a))
    if line.startswith("::"):
      table.append("# Note, " + line.split("::")[1])
      continue
    if line.startswith(":>"):
      print(line)
    if line.startswith(";>")
    #thisfunctiondoesntexistsoitwillgiveanerror()
  except:
    print("Oops")
    print("Error with '" + line.replace("\n", "") + "'")
    quit()

print()
print("How would you like to run?")
print("1, via interpreter or 2, export to .py file")
awdaw = str(input("1/2  "))
if awdaw == "1":
  print("naw")
