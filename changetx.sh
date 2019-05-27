#!/bin/bash

tx[0]=3
tx[1]=6
tx[2]=12
tx[3]=24

txv=${tx[$RANDOM % ${#tx[@]}]}
echo $txv > txpower_leader.txt
iwconfig wlan0 txpower $txv
