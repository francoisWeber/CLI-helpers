# General alias
alias ll="ls -lhFG"
alias copypath="~/Code/CLI-helpers/copypath/copypath.py"
alias meteo='curl http://wttr.in/'
alias octal='stat -f %A'

# pics
alias pics-dirs='mkdir RAW Vidéos && mv *.NEF RAW && mv *.mov Vidéos'
function heic2jpeg {
    for i in *.heic; do 
        convert -quality 98 "$i" "${i%.heic}.jpg"
    done
    jhead -ft *.jpg
}

function any2jpeg {
    # argument : extension you want to turn into JPG
    for i in *."$1"; do 
        convert -quality 98 -define "$1":exif-properties=true "$i" "${i%.$1}.jpg"
        rm "$i"
    done
}

function mov2mp4 {
    for i in *.mov; do 
        ffmpeg -i "$i" "${i%.mov}.mp4"
        rm "$i"
    done
}

# Python
alias python=python3
export PATH="$PATH:~/Library/Python/3.8/bin"

# Various softs
eval "$(thefuck --alias)"
source /usr/local/etc/profile.d/z.sh

# Add my tools to path
export PATH="$PATH:~/Code/CLI-helpers/pics-handling"

# Source other local bash_profil-like file
# include .bashrc if it exists
if [ -f $HOME/.local_bash_profile ]; then
    . $HOME/.local_bash_profile
fi

# Git autocomplete
if [ -f ~/.git-completion.bash ]; then
  . ~/.git-completion.bash
fi

# Prompt
function _update_ps1() {
    PS1=$(powerline-shell $?)
}

if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
fi

