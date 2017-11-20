# The following lines were added by compinstall

zstyle ':completion:*' completer _complete _ignored _correct _approximate
zstyle ':completion:*' format 'Completando %d'
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' matcher-list '' 'm:{[:lower:][:upper:]}={[:upper:][:lower:]}' 'r:|[._-]=** r:|=**' 'l:|=* r:|=*'
zstyle :compinstall filename '/home/ayatsfer/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.zsh/hist
HISTSIZE=25
SAVEHIST=100
# End of lines configured by zsh-newuser-install
PS1='%F{yellow}%B%n%b %F{blue}%v%3~ %F{magenta}»%f '
RPS1='%F{white}%t%f'
alias cdc='cd ~-'
alias ls='ls --color=auto'
LS_COLORS=$LS_COLORS:'ow=1;34:'; export LS_COLORS
alias tree='tree -C'
alias raspi='ssh ayatsfer@10.10.0.136'
alias upm='cd ~/d/UPM/INFORMATICA'
function mkfortran {
  echo "program $1\nimplicit none\n\nend program $1" >> $1.f95
}
function gf {
  gfortran $1.f95 -o $1.o
  ./$1.o
}
