# install Brew
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# # install python
# brew install python
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3 get-pip.py
# rm get-pip.py


# brew some stuff
brew install thefuck wget z htop stats bash-completion


# Git
## Autocomplete
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash >> ~/.git-completion.bash

## global alias
git config --global alias.lg 'log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit'
git config --global alias.amend 'commit --amend --no-edit'
git config --global alias.co checkout
git config --global alias.sha 'rev-parse HEAD'
git config --global alias.last 'log -1 HEAD'
git config --global alias.pushfwk 'push --force-with-lease'

git config --global core.editor "nano"

## Echo some stuff into ~/.bash_profile
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
echo "source $DIR/.bash_profile" >> ~/.bash_profile
echo "source $DIR/.alias" >> ~/.bash_profile