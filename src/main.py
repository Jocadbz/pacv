#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import os
import sys

# from ast import Break

help_pacy = """
    Pacy : An wrapper for pacman

    Options:
    i [package]    -> Install the desired package
    u <package>    -> Do an complete upgrade
    r [package]    -> remove the desired program
    c              -> clean the system and remove orphaned packages
    s [package]    -> Search for an package
    info [package] -> Display info of an package
    vs             -> Version of Pacy and Pacman
       """


def VERSION():
    print("Pacy version: 3.0.0")
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
        sys.exit(0)
    else:
        pkgs = sys.argv[2:]
        res = str(pkgs)[1:-1]
        new = res.replace(',', '')
        subprocess.call(f'sudo pacman -Syu {new}', shell=True)
        sys.exit(0)


def REMOVE():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    subprocess.call(f"sudo pacman -Rs {new}", shell=True)


def remove_orphans():
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


abbreviationsDict = {"i": INSTALL, "u": UPGRADE, "r": REMOVE, "c": remove_orphans,
                     "s": SEARCH, "vs": VERSION, "info": INFO}


def DO_WORK():
    """ Function to handle command line usage"""
    args = sys.argv
    args = args[1:]  # First element of args is the file name

    if len(args) == 0:
        print('Wrong usage. Run with --help flag to see current commands.')
    else:
        for arguments in args:
            if arguments == '--help':
                print(help_pacy)
                break
            else:
                try:
                    if arguments in abbreviationsDict.keys():
                        # get your function based on key in abbreviationsDict
                        required_function = abbreviationsDict[arguments]
                        required_function()  # Execute this function.
                        break
                    # Since the user input a command that can't be used as the name of a function.
                    else:
                        # install = INSTALL + () = INSTALL() and eval it.
                        eval(f"{arguments.upper()}()")
                        break
                # (NameError) will be thrown in case you use a command which is not present.
                except NameError:
                    print('Unrecognized argument.')
                    print("Try running with --help flag to see current commands")
                    break


if __name__ == '__main__':
    DO_WORK()
