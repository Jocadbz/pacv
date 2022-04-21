#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import sys
# from ast import Break

help = """
    Pacy : An wrapper for pacman

    Options:
    install -> Install the desired package
    upgrade -> Do an complete upgrade
    remove  -> remove the desired program
    clean   -> clean the system and remove orphaned packages
    search  -> Search for an package
    info    -> Display info of an package
    version -> Version of Pacy that is installed
       """


def VERSION():
    print("Pacy version: 2.0.0")
    os.system("pacman --version")


def INSTALL():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    subprocess.call(f'sudo pacman -S {new}', shell=True)


def UPGRADE():
    args = sys.argv
    args = args[2:]
    if len(args) == 0:
      subprocess.call("sudo pacman -Syu", shell=True)
      sys.exit
    else:
       pkgs = sys.argv[2:]
       res = str(pkgs)[1:-1]
       new = res.replace(',', '')
       subprocess.call(f'sudo pacman -Syu {new}', shell=True)
       sys.exit


def REMOVE():
   pkgs = sys.argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   subprocess.call(f"sudo pacman -Rs {new}", shell=True)


def REMOVEORPHANS():
   subprocess.call("sudo pacman -Rs $(pacman -Qqdt)", shell=True)


def SEARCH():
   pkgs = sys.argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   subprocess.call(f'sudo pacman -Ss {new}', shell=True)


def INFO():
   pkgs = sys.argv[2:]
   res = str(pkgs)[1:-1]
   new = res.replace(',', '')
   subprocess.call(f'sudo pacman -Si {new}')


def DO_WORK():
   """ Function to handle command line usage"""
   args = sys.argv
   args = args[1:]  # First element of args is the file name

   if len(args) == 0:
      print('Wrong usage. Run with --help flag to see current commands.')
   else:
      for a in args:
         if a == '--help':
            print(help)
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
         elif a == 'version' or a == 'vs':
             VERSION()
             break
         else:
            print('Unrecognised argument.')
            print('Try running with --help flag to see current commands')


if __name__ == '__main__':
    DO_WORK()
