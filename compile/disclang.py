from sys import argv

ok   = '\033[92m'
warn = '\033[93m'
fail = '\033[91m'
wht  = '\033[0m'

if "-h" in argv:
  print(f"""{wht}Disclang compiler

{wht}OK, {warn}WARNING, {fail}FAIL
{wht}python disclang.py [options] [file] [-o outputfile]
""")

