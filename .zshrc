alias raspi='ssh pi@192.168.1.40'
alias ls='ls --color=auto'
alias xres='xrdb ~/.Xresources'
alias monstercat='streamlink -Q -p mpv twitch.tv/monstercat best'
alias mfm='monstercat & disown'
alias apaga='sudo shutdown now'
alias gksu='gksu-polkit'

export VISUAL=vim
export EDITOR="$VISUAL"

PS1='%F{yellow}%B%n%b %F{blue}%v%3~ %F{magenta}»%f '
RPS1='%F{white}%t%f'
