# simple example from Arch wiki:
autoload -Uz compinit promptinit
compinit
promptinit

# add the local fpath (e.g., for autocompletion)
fpath=($ZDOTDIR/fpath $fpath)
