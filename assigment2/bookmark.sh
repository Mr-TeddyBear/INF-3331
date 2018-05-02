#!/bin/bash
if [ $# -gt 2 ]; then
    echo "Too many imput arguments maximum 2 is allowed"
    return
fi

if [ $# -eq 0 ]; then
  while read -r bookmarkname; do
    name=`echo $bookmarkname | cut -d \| -f 1`
    location=`echo $bookmarkname | cut -d \| -f 2`
    export $name="$location"
  done < "$HOME/.bookmarks"
  return
fi

case $1 in
    "-a")
        #code to add current directory
        #to bookmarks
        pwd=`pwd`
        echo "$2|$pwd" >> ~/.bookmarks
        ;;
    "-r")
        #remove given bookmark and accosiated
        #directory
        sed -i "/^$2/d" ~/.bookmarks
        unset $2
        ;;

    *)
        echo "Invalid input arguments"
        return
        ;;
esac
