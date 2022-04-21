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
Just move the binary to ```bin```. And you are good to go.
