#!/bin/sh

for q in $(ls -d */); do
    cd $q
    # pwd
    rm -f *.ps 
    rm -f *.raw  
    rm -f *.log
    rm -f *.net
    rm -f *.txt
    rm -f .spiceinit
    rm -f -r ./tmp
    echo y | rm -f *.sch~ 
    cd ..
done

