global sys
sys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6, 8]


def print_style():
    display = '''
                      {}
            -------------------------
                     {}|{}
         --------------------------------
                  {}|{}|{}|{}
     --------------------------------------
              {}|{}|{}|{}|{}|{}|{}|{}
      ----------------------------------------
    '''
    print(display.format(*sys))
from ctypes import cdll
lib=cdll.LoadLibrary('./libgeek.so')
class Geek(object):
    def __init__(self):
        self.obj=Geek_new()
    def myfun(self):
        lib.Geek_myfun(self.obj)
f=Geek()
f.myfun()