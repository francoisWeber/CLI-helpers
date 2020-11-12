# install Brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# install python
brew install python
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
rm get-pip.py

# brew some stuff
brew install thefuck wget z htop github-markdown-toc

# pip install some stuff
pip install click powerline-shell

# install fonts for powerline-shell
cd /tmp
git clone https://github.com/powerline/fonts.git --depth=1
cd fonts
./install.sh
cd ..
rm -rf fonts

# Git
## Autocomplete
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash

## global alias
git config --global alias.lg 'log --graph --pretty=format:"%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit'
git config --global alias.co checkout
git config --global alias.sha 'rev-parse HEAD'
git config --global core.editor "nano"
