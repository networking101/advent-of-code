#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Provide day as argument."
    echo "$0 N"
    exit 0
fi
curl "https://adventofcode.com/2020/day/$1/input" -H 'Cookie: session=53616c7465645f5f6964d5c17bd33a2b90a653f720bd3deadec12145275357fdda36a54f346aa557ad3b1b21e37f06d1;' -o "./$1/input"