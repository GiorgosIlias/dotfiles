#!/bin/sh

if [ -z "$(pidof spotify)" ]; then
	mpc prev
else
	playerctl previous
fi
echo $minfo

