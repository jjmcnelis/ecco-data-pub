#!/bin/bash
for f in /home/jack/data/tests/20200902_v3/*.nc; do 
    echo $f;
    name="$(basename -- $f)";
    ncdump -h $f > ${name}.cdl;
    echo;
done