def code(string,mode,key):
  out = ""
  if mode == 0:
    #
    for x in string:
      out += chr(ord(x)+key)
    for x in "QZL":
      out += chr(ord(x)+key)
  elif mode == 1:
    #
    length = len(string)
    ckey = string[length-3:length+1]
    print("read key is:",ckey)
    tkey = ""
    y = 0
    while y < 500 and tkey != "QZL":
      tkey = ""
      for x in ckey:
        tkey += chr(ord(x)-y)
      y += 1
    key = y - 1
    #
    print(key)
    for x in string:
      out += chr(ord(x)-key)
    out = out[0:length-3]
  return out