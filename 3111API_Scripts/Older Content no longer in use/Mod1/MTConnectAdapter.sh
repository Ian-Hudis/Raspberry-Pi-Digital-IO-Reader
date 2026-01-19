#!/bin/bash

declare -i n=0
declare -i y=1
#declare -i count=10

while (true); do

  n=$((n + y))

  #echo $n

  if [ $n == 10 ]
  then
   sudo python /home/pi/Desktop/httpget.py
   #echo "true"
   n=0
  fi

  sudo python /home/pi/Desktop/xmltest.py &
  sleep 2
done
