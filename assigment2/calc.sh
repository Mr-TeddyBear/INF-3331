#!/bin/bash
if [ $# == "0" ]; then
    echo "Please provide commandline input"
    exit
fi
case $1 in
    "S")
        shift;
        sum=0
        for i in "$@"; do
            ((sum+=$i))
        done
        echo "$sum"
        ;;
    "P")
        shift;
        product=1
        for i in "$@"; do
            ((product*=$i))
        done
        echo "$product"
        ;;
    "M")
        shift;
        max=$2
        for i in "$@"; do
            if [ $max -lt $i ]; then
                max=$i
            fi
        done
        echo "$max"
        ;;
    "m")
        shift;
        min=$1
        for i in "$@"; do
            if [ $min -gt $i ]; then
                min=$i
            fi
        done
        echo "$min"
        ;;
    esac