#!/bin/bash
if [ $# == "0" ]; then
    echo "You did not specify a TZ, printing your standard TZ"
    date
    exit
fi

case $1 in
    "no")
        export TZ="CET"
        ;;
    "sk")
        export TZ="Asia/Seoul"
        ;;
    "us")
        export TZ="America/New_York"
        ;;
    *)
        echo "Invalid input argument"
        exit
esac
while [ 1 == 1 ]; do
clear; date; sleep 1
done