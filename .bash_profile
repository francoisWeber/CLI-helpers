# General alias
alias ll="ls -lhFG"
alias copypath="~/Code/helpers/copypath/copypath.py"

# Python
alias python=python3
export PATH="$PATH:~/Library/Python/3.8/bin"

# The Fuck
eval "$(thefuck --alias)"


# Source other local bash_profil-like file
# include .bashrc if it exists
if [ -f $HOME/.bash_profile_local ]; then
    . $HOME/.bash_profile_local
fi

# Prompt
function _update_ps1() {
    PS1=$(powerline-shell $?)
}

if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
fi
