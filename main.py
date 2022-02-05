#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from ast import Break
from sys import argv

def INSTALL():
    pkgs = argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    os.system(f'sudo pacman -S {new}')

def UPGRADE():
    n = len(sys.argv)
    args = sys.argv
    args = args[2:]
    if len(args) == 0:
      os.system("sudo pacman -Syu")
      sys.exit
    else:
       pkgs = argv[2:]
       res = str(pkgs)[1:-1]
       new = res.replace(',', '')
       os.system(f'sudo pacman -Syu {new}')
       sys.exit
             
def REMOVE():
   pkgs = argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   os.system(f"sudo pacman -Rs {new}")

def REMOVEORPHANS():
   os.system(f"sudo pacman -Rs $(pacman -Qqdt)")

def SEARCH():
   pkgs = argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   os.system(f'sudo pacman -Ss {new}')

def INFO():
   pkgs = argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   os.system(f'sudo pacman -Si {new}')

def DO_WORK():
   """ Function to handle command line usage"""
   args = sys.argv
   args = args[1:] # First element of args is the file name

   if len(args) == 0:
      print('Wrong usage. Run with --help flag to see current commands.')
   else:
      for a in args:
         if a == '--help':
            print('pacy : An wrapper for pacman')
            print('Options:')
            print(' install -> Install the desired package')
            print(' upgrade -> Do an complete upgrade')
            print(' remove  -> remove the desired program')
            print(' clean   -> clean the system and remove orphaned packages')
            print(' search  -> Search for an package')
            print(' info    -> Display info of an package')
         elif a == 'install' or a == 'i':
            INSTALL()
            break
         elif a == 'upgrade' or a == 'u':
            UPGRADE()
            break
         elif a == 'remove' or a == 'r':
            REMOVE()
            break
         elif a == "clean" or a == "c":
            REMOVEORPHANS()
            break
         elif a == 'search' or a == 's':
            SEARCH()
            break
         elif a == 'info':
            INFO()
            break
         else:
            print('Unrecognised argument.')
            print('Try running with --help flag to see current commands')

if __name__ == '__main__': 
    DO_WORK()
