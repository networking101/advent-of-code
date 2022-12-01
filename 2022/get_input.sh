#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Provide day as argument."
    echo "$0 N"
    exit 0
fi
curl "https://adventofcode.com/2022/day/$1/input" -H 'Cookie: session=53616c7465645f5f27b71a9da74083adf20ad70f04d0a53619e672bb882bcccf758f36507a0b9802fa96f03200ede643713f426dd51a9340a1f522971f475301;' -o "./$1/input"
