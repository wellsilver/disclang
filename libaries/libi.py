def main(i):
  print("Libi has no command and is used by other libaries")
  return ''

def getargs(i,amount):
  try:
    a=i.split("-",1)[1]
  except:
    print("Failed- invalid command")
  kk = []
  # I dont know if below counts as a algorithm, though I dont know what algorithms are lol
  for bb in range(int(amount)):
    kk.append(a.split('[',1)[1].split(']',1)[0])
    a=a.split(']',1)[1]
  return kk
