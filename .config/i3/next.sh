#!/bin/sh

if [ -z "$(pidof spotify)" ]; then
	mpc next
else
	playerctl next
fi
echo $minfo

