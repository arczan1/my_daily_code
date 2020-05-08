#!/bin/bash

if [ $# -eq 2 ]; then
	a=$1
	b=$2
	while ! [ $b -eq 0 ]; do
		tmp=$b
		b=$(( $a % $b ))
		a=$tmp	
	done
	echo "GDB($1, $2) = $a"
else
cat << EOF
Usage:
	greatest_common_divisor.sh NUMBER1 NUMBER1
EOF
fi
