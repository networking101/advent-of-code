#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Provide day as argument."
    echo "$0 N"
    exit 0
fi
curl "https://adventofcode.com/2016/day/$1/input" -H 'Cookie: session=53616c7465645f5f34db99e7553fdd2e7a5ff592d6f2c8eda080a0d3a96c5bfc27bab97552eb4b5a42eff0ed91e22de45e130bbdcfc34a30775c41a2d3b873a5;' -o "./$1/input"
