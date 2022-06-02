# Pacy
An wrapper for pacman

### What this does?

It is basically an wrapper for pacman package manager. it makes syntax more simple.

### Functions

#### Installing packages
```bash
pacy i <package> # -> same as "pacman -S"
```
#### Updating the system
```bash
pacy u [optional package] # -> same as "pacman -Syu"
```

#### Printing package info
```bash
pacy info <package> # -> same as "pacman -Si"
```

#### Removing orphan packages
```bash
pacy c # -> same as "pacman -Rs $(pacman -Qqdt)"
```

#### Removing packages
```bash
pacy r <package> # -> same as "pacman -Rs"
```

#### Searching packages
```bash
pacy s <package> # -> same as "pacman -Ss"
```

### How to install ?
You can use the ```jocadbz-arch-repo```, a repo I made for my projects.
Instructions at https://jocadbz.github.io/arch-repo/

If you don't want to mess around with repos, just move the binary to ```/usr/bin/```
