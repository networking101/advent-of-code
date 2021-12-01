#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Provide day as argument."
    echo "$0 N"
    exit 0
fi
curl "https://adventofcode.com/2021/day/$1/input" -H 'Cookie: session=53616c7465645f5fa0c7d6dc806aeda466ed062c948200fca643fa39d43e7c4bb20af533d44fe640b48b570b50d0755e;' -o "./$1/input"