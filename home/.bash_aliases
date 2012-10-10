# sudo shortcuts
alias svim='sudo vim'
alias srb='sudo reboot'
alias spo='sudo poweroff'

alias h="history|grep "     # search terminal history
alias f="find . |grep "     # find files in the current directory
alias p="ps aux |grep "     # search running processes
alias o="xdg-open "       # open as if you had double-clicked

#TODO change this to socat
alias listen="nc -luvvn "   # listen on udp port using netcat

# prompt strings
alias ps1_short="PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '"
alias ps1_long="PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '"
