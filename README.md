# Pacy
An wrapper for pacman

### What this does?

It is basically an wrapper for pacman package manager. it makes syntax more simple.

### Functions

#### Installing packages
```bash
pacy [i or install] <package> # -> same as "pacman -S"
```
#### Updating the system
```bash
pacy [u or upgrade] [optional package] # -> same as "pacman -Syu"
```

#### Printing package info
```bash
pacy info <package> # -> same as "pacman -Si"
```

#### Removing orphan packages
```bash
pacy [c or clean] # -> same as "pacman -Rs $(pacman -Qqdt)"
```

#### Removing packages
```bash
pacy [r or remove] <package> # -> same as "pacman -Rs"
```

#### Searching packages
```bash
pacy [s or search] <package> # -> same as "pacman -Ss"
```

### How to install ?
Just move the binary to ```bin```. And you are good to go.

It is pretty basic right now, but i am working on this.

### Know limitations

Unfortunately, the operations don't support more than one package. that means you can't install several packages
in an row, you need to install one per time.
