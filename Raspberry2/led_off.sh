#!/bin/sh
gpio -g write 2 1
sleep .5
gpio -g write 2 0
