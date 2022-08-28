def main(i):
  a=i.split('[',1)[1]
  b=a.split('[',1)[1]
  a=a.split(']',1)[0]
  b=b.split(']',1)[0]
  return f"  if c == '{a}':\n    await l.channel.send('{b}')"