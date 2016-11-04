export EDITOR=vim

export NRF5_SDK=/media/data/Releases/nRF5x/nRF5_SDK_12.1.0_0d23e2a

# If I ever set the path here, check for /etc/profile in /etc/zsh/profile

# Make sure path only keeps unique values
typeset -U path
# Add RubyGems to path (for homesick, etc)
path+=("$(ruby -e 'print Gem.user_dir')/bin")

export PATH
