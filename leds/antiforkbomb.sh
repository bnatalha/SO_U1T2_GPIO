#!/bin/bash
# Set the field seperator to a newline
#IFS="
#"

for line in $(ps -Ao comm= | uniq -c | awk '$1 > 30 {print $2}');do 
 echo "Command "$line" is creating too much processes";
 # Parar processo
 #pkill -c $line --signal SIGSTOP
 # Matar processo
 pkill -c $line --signal SIGKILL
done
#sleep 0.5


