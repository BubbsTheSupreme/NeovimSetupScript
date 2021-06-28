import os
from sys import argv

if argv[1] == '--deb' or argv[1] == '-d':
	os.system('sudo apt install neovim')
elif argv[1] == '--arch' or argv[1] == '-a':
	os.system('sudo pacman -Syu neovim')

os.system('mkdir ~/.config/nvim')
os.system('touch ~/.config/nvim/init.vim')
os.system('curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim')
os.system('mkdir ~/.config/nvim/vim-plug/plugins.vim')
os.system('touch ~/.config/nvim/vim-plug/plugins.vim')

plugins = '''
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
endif

call plug#begin('~/.config/nvim/autoload/plugged')
    Plug 'sheerun/vim-polyglot'
    Plug 'scrooloose/NERDTree'
    Plug 'jiangmiao/auto-pairs'
call plug#end()
'''

with open('~/.config/nvim/vim-plug/plugins.vim', 'w+') as f:\
	f.write(plugins)

config = '''
source $HOME/.config/nvim/vim-plug/plugins.vim
set number
set showmatch
set autoindent
set shiftwidth=4
set smartindent
set smarttab
set softtabstop=4
set tabstop=4
'''

with open('~/.config/nvim/init.vim', 'w+') as f:
	f.write(config)

# This is a script to automate the process of setting
# up neovim that chrisatmachine created (along with my vim config settings)
# link to original setup is here
#https://www.chrisatmachine.com/Neovim/01-vim-plug/