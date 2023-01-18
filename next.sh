#!/bin/bash

mkdir $1
echo "# Problem $1" > $1/README.md
echo "#!/usr/bin/python3" > $1/$1.py
chmod +x $1/$1.py