#!/bin/sh

if [ -z "$(pidof spotify)" ]; then
	mpc toggle
else
	playerctl play-pause
fi
echo $minfo

