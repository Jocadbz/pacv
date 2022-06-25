module pacman

import os

pub fn install() {
   pkg := os.args[2..]
   mut cmd := 'sudo pacman -S '
   for x in pkg {
      cmd += '$x '
    }
    os.system(cmd)
}

pub fn remove() {
   pkg := os.args[2..]
   mut cmd := 'sudo pacman -R '
   for x in pkg {
      cmd += '$x '
    }
    os.system(cmd)
}

pub fn upgrade() {
   pkg := os.args[2..]
   mut cmd := 'sudo pacman -Syu '
   for x in pkg {
      cmd += '$x '
    }
    os.system(cmd)
}

pub fn search() {
   pkg := os.args[2]
   os.system("sudo pacman -Ss $pkg")
}

pub fn info() {
   pkg := os.args[2..]
   mut cmd := 'sudo pacman -Si '
   for x in pkg {
      cmd += '$x '
    }
    os.system(cmd)
}

pub fn refresh() {
   pkg := os.args[2..]
   mut cmd := 'sudo pacman -Syyu '
   for x in pkg {
      cmd += '$x '
    }
    os.system(cmd)
}