set directory=$HOME/.vim/swap//
set backupdir=$HOME/.vim/backup//
map <F5> :w <CR> :!gfortran % -o %<.o && ./%<.o <CR>

let fortran_free_source=1
let fortran_do_enddo=1
filetype plugin indent on
syntax on

set nu
set ruler

set showcmd

set smarttab
set expandtab
set smartindent
set autoindent
set tabstop=2
set shiftwidth=2

set bs=2

set incsearch
set ignorecase
set smartcase
