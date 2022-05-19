import time
# every day i rewrite again, 100 lines ar- gone to waste~
"""heres how it works:
for every line in <file>.readlines():
if empty or in note catcher skip
if import do import
if init write to a table for inits
if main write to a table for mains"""
file=open('example.dss')
count=0
count2=0
m_init=[]
m_main=[]
blank=[]
mode=0
def panic(msg):
  global count
  print("Error!")
  print(f"At line {count}")
  print(msg)
  time.sleep(5)
  quit()
for i in file.readlines():
  count+=1
  if i == "\n":
    continue
  if count2 > 0:
    count2 -= 1
    continue
  if i.startswith('::'):
    continue
  if i.startswith(':k'):
    a=i.split(":k",1)[1]
    count2=int(a)
    continue
  if i.startswith('--'):
    if i.startswith('import',2):
      mode=1
      continue
    if i.startswith('init',2):
      mode=2
      continue
    if i.startswith('main',2):
      mode=3
      continue
    panic("Invalid mode, must be; import, init, or main")
  # finally
  if mode == 1:
    if i.startswith(">>"):
      try:
        exec(f"import lib."+i.split(">>",1)[1])
      except:
        panic("Invalid import\nCreate a 'lib' folder or incorrect import name")
    continue
  if mode == 2:
    try:
      exec(f'm_init.append(lib.'+i.split('-',1)[0]+f'.main("{i}"))'.replace('\n',""))
    except:
      panic("")
    #      m_init.append('')
    continue
    #m_init.append()
  if mode == 3:
    try:
      exec(f'm_main.append(lib.'+i.split('-',1)[0]+f'.main("{i}"))'.replace('\n',""))
    except:
      panic("")
    continue
