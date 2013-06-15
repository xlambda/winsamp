#-*- coding: utf8 -*-
#!python


from ctypes import *
from ctypes.wintypes import *

def enum_type(module, typenum, param):
  if typenum >> 16:  #integer
    pass
  else:  # string
    pass
  windll.kernel32.EnumResourceNamesA(module, cast(typenum, LPSTR), enum_name, 0)
  return 1

def enum_name(module, typenum, name, param):
  windll.kernel32.EnumResourceLanguagesA(module, cast(typenum, LPSTR), cast(name, LPSTR), enum_lang, 0)
  return 1

def enum_lang(module, typenum, name, lang, param):
  print typenum, name, hex(lang)
  """
  if typenum != 6:
    return 1
  buff = create_string_buffer(1000)
  readnum = windll.user32.LoadStringA(module, name, buff, 1000)
  if readnum == 0:
    print WinError()
    return 1
  print buff.value
"""
  if typenum != 3:
    return 1
  #hicon = windll.user32.LoadIconA(module, name)
  #hicon = windll.user32.LoadImageA(module, name, 0, 0, 0, 0)
  hicon = windll.kernel32.FindResourceA(module, name, typenum)
  if not hicon:
    print WinError()
    return 1
  print 'hicon: ', hicon
  hicon = windll.kernel32.FindResourceExA(module, typenum, name, lang)
  if not hicon:
    print WinError()
    return 1
  print 'hicon: ', hicon
  return 1

def go(filepath):
  global enum_type, enum_name, enum_lang
  functype = WINFUNCTYPE(BOOL, HMODULE, WORD, LONG)
  enum_type = functype(enum_type)
  funcname = WINFUNCTYPE(BOOL, HMODULE, WORD, WORD, LONG)
  enum_name = funcname(enum_name)
  funclang = WINFUNCTYPE(BOOL, HMODULE, WORD, WORD, WORD, LONG)
  enum_lang = funclang(enum_lang)
  #exe = windll.kernel32.LoadLibraryA(filepath)
  n = windll.shell32.ExtractIconExA(filepath, -1, None, None, 10)
  print n
  n = windll.user32.PrivateExtractIconsA(
filepath, 0, 16, 16, None, None, 10, 0)
  print n
  exe = windll.kernel32.LoadLibraryExA(filepath, None, 2)
  #exe2 = windll.kernel32.GetModuleHandleA(filepath)
  '''
  for i in range(0,1000):
    h = windll.user32.LoadIconA(exe, i)
    if h:
      print i, h
  h = windll.user32.LoadIconA(exe, 32512)
  if h:
    print i, h
  '''
  windll.kernel32.EnumResourceTypesA(exe, enum_type, 0)



if __name__ == "__main__":
  import sys
  go(sys.argv[1])
