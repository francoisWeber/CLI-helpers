# General alias
alias ll="ls -lhFG"
alias copypath="~/Code/CLI-helpers/copypath/copypath.py"

# Git
git config --global alias.lg 'log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit'
git config --global alias.co checkout

# Python
alias python=python3
export PATH="$PATH:~/Library/Python/3.8/bin"

# Various softs
eval "$(thefuck --alias)"
source /usr/local/etc/profile.d/z.sh

# Source other local bash_profil-like file
# include .bashrc if it exists
if [ -f $HOME/.local_bash_profile ]; then
    . $HOME/.local_bash_profile
fi

# Prompt
function _update_ps1() {
    PS1=$(powerline-shell $?)
}

if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
fi

