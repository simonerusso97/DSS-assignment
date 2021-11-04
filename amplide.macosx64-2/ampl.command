#!/bin/bash
cd "`dirname "$0"`"
xattr -rc .
clear
echo 'wd:' `pwd`
./ampl -v
