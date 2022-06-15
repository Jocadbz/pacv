#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import lib.pacman as pacman

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
    print("Pacy version: 4.0.0")
    pacman.version()


def INSTALL():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    pacman.s(new)


def UPGRADE():
    args = sys.argv
    args = args[2:]
    if len(args) == 0:
        pacman.syu("")
        sys.exit(0)
    else:
        pkgs = sys.argv[2:]
        res = str(pkgs)[1:-1]
        new = res.replace(',', '')
        pacman.syu(new)
        sys.exit(0)


def REMOVE():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    pacman.rs(new)


def remove_orphans():
    pacman.rs("$(pacman -Qqdt)")


def SEARCH():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    pacman.ss(new)


def INFO():
    pkgs = sys.argv[2:]
    res = str(pkgs)[1:-1]
    new = res.replace(',', '')
    pacman.si(new)


def REFRESH():
    pacman.syyu()


abbreviationsDict = {"i": INSTALL, "u": UPGRADE, "r": REMOVE,
                     "c": remove_orphans, "s": SEARCH, "vs": VERSION,
                     "info": INFO, "refresh": REFRESH}


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
                    else:
                        # install = INSTALL + () = INSTALL() and eval it.
                        eval(f"{arguments.upper()}()")
                        break
                except NameError:
                    print('Unrecognized argument.')
                    print("Running with --help flag to see current commands")
                    break


if __name__ == '__main__':
    DO_WORK()
