#!/bin/bash

FRUIT=$1

if [ $FRUIT == APPLE ]; then
	echo "Select APPLE"
elif [ $FRUIT == BANANA ]; then
        echo "Select BANANAE"
elif [ $FRUIT == ORANGE ]; then
        echo "Select ORANGEE"
else
        echo "Select Others"
fi
