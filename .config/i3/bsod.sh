#!/usr/bin/env bash

bsod="$HOME/.config/i3/bsod.png"

(( $# )) && { icon=$1; }

i3lock -i "$bsod" -p win
