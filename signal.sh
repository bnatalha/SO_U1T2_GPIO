#!/bin/bash

cd /sys/class/gpio/gpio67

echo out > direction

for i in `seq 0 10`;
do
    echo 1 > value
    sleep .1
    echo 0 > value
    sleep .1
done
