#!/bin/bash

for host in $(cat bt3_for_bt4.txt); do
    naabu -host $host -pf top-1000-most-popular-tcp-ports-nmap-sorted.csv -o bt4.csv
done
