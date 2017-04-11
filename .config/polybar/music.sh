#!/bin/sh

if [ -z "$(pidof spotify)" ]; then
	minfo="$(mpc current)"	
else
	minfo="$(spotify-now -i "%artist - %title")"
fi
echo $minfo

