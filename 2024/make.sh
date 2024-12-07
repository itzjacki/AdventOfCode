#!/bin/sh
# Scaffolds Advent of Code directory and opens in vscode

if [ -z "$1" ]; then
    echo "Which day do you want to scaffold?"
    read -r daynumber
else
    daynumber=$1
fi

if [ -d ./"$daynumber" ]; then
  echo "Directory for day already exists."
  exit 1
fi

mkdir "$daynumber"

cp .template/task.py "$daynumber"
mv "$daynumber/task.py" "$daynumber/${daynumber}a.py"

cp .template/task.py "$daynumber"
mv "$daynumber/task.py" "$daynumber/${daynumber}b.py"

touch "$daynumber/input.txt"
touch "$daynumber/test.txt"

read -r -n 1 -p "Do you want to open it in VSCode? [Y/n] " response
if [[ "$response" =~ ^([nN])$ ]]; then
    exit 0
fi

code . -g "/Users/jakobkielland/Documents/Code/hobby/advent-of-code/2024/$daynumber/${daynumber}a.py"
