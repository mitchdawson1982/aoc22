#!/bin/bash

if [ $# -eq 0 ];
then
  echo "$0: 🔙 - Missing argument, include day number as argument."
  exit 1
elif [ $# -gt 1 ];
then
  echo "$0: ⬆ - Too many arguments."
  exit 1
else
  echo "📁 - Creating python directory for Day $1."
  mkdir ../day$1
  echo "🐑 - Cloning contents."
  cp main.py ../day$1
  cp input.txt ../day$1
  echo "✅ - Complete."
fi
