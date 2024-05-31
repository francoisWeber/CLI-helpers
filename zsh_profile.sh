# ZSH stuff
source $(brew --prefix)/share/zsh-autosuggestions/zsh-autosuggestions.zsh
plugins=( 
    git
    z
    copypath
)

export DEFAULT_USER=$USER

prompt_aws(){}


# Z
. /opt/homebrew/etc/profile.d/z.sh

# Functions
source $HOME/code/CLI-helpers/functions.sh

# Fuck
eval "$(thefuck --alias)"

# Pyenv
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"