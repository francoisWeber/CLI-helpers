# pics
function heic2jpeg {
    for i in *.heic; do 
        convert -quality 100 "$i" "${i%.heic}.jpg"
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

    for i in *.MOV; do 
        ffmpeg -i "$i" "${i%.mov}.mp4"
        rm "$i"
    done
}

# Python
export PATH="$PATH:~/Library/Python/3.8/bin"

# Various softs
eval "$(thefuck --alias)"


# Add my tools to path
export PATH="$PATH:~/Code/CLI-helpers/pics-handling"

# Source other local bash_profil-like file
# include .bashrc if it exists
if [ -f $HOME/.local_bash_profile ]; then
    . $HOME/.local_bash_profile
fi

# # Git autocomplete
if [ -f /opt/local/etc/profile.d/bash_completion.sh ]; then
  . /opt/local/etc/profile.d/bash_completion.sh
fi


# Autocompletion for ZSH
autoload -Uz compinit && compinit

# Z
. /opt/homebrew/etc/profile.d/z.sh
