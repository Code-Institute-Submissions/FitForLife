#!/bin/bash
source ./shell_scripts/environment.sh

DOY=$(date +%j)
echo "Backing up existing code: $$DOY"
tar -zcf ~/backup/fflsnapshot_${DOY}.tar.gz  /home/developer/VDjangoDevelopment/FitForLife
echo "Pulling latest code from origin master"
git pull

 