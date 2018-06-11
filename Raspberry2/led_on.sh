#!/bin/sh
gpio -g write 3 1
sleep .5
gpio -g write 3 0
