import time
"""
if you are here from replit look at example.dss!


"""
def error(message):
  print(message)
############ BUILTINS
"""
send args as table (eg, <command>[arg1][arg2][arg...)
"""
class chat_reply:
  def chat(args):
    pass
  def reply(args):
    pass
class activity:
  def activity(args):
    a=len(args)
    if a > 2:
      error("More than 2 arguements in activity command!")
#############
def scanlib(name):
  file=open(name)
  f=file.readline()
  a,b=cmd_scan(f)
def cmd_scan(i):
  pass