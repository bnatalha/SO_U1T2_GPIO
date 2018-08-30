#!/bin/bash

RED_LED=gpio68
GREEN_LED=gpio69

cd /sys/class/gpio/$RED_LED

echo out > direction

#for i in `seq 0 10`;
#do
#    echo 1 > value
#    sleep .1
#    echo 0 > value
#    sleep .1
#done

grep 'cpu ' /proc/stat | 
awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'

echo $usage

