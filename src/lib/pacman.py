import subprocess as os

### Install sections
# Available operators:
# -S, -Sy, -Su
def s(a, /):
    os.call(f"sudo pacman -S {a}", shell=True)


def sy(a, /):
    os.call("sudo pacman -Sy {a}", shell=True)


def su(a, /):
    os.call("sudo pacman -Su {a}", shell=True)


### Update sections
# Available operators:
# -Syu, -Syyu
def syu(a, /):
    os.call(f"sudo pacman -Syu {a}", shell=True)


def syyu(a, /):
    os.call(f"sudo pacman -Syyu {a}", shell=True)

### Install sections
# Available operators:
# -R, -Rsn
def r(a, /):
    os.call(f"sudo pacman -R {a}", shell=True)


def rsn(a, /):
    os.call(f"sudo pacman -Rsn {a}", shell=True)


def rs(a, /):
    os.call(f"sudo pacman -Rs {a}", shell=True)

### Miscellaneous options
# Available operators:
# -Ss, -Si, --version
def ss(a, /):
    os.call(f"sudo pacman -Ss {a}", shell=True)


def si(a, /):
    os.call(f"sudo pacman -Si {a}", shell=True)


def version():
    os.call(f"pacman --version", shell=True)
