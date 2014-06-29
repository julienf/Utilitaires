#! /bin/bash

for i in /home/julien/github/*; do
  for j in $i/.git/objects/*; do
    gitdir=`basename $j`;
    if [[ $gitdir == [0-9][0-9] ]]; then
      echo "In $i there is : $gitdir";
      for k in $j/*; do
	echo "Nb of objects : `ls -1 $j | wc -l`";
	echo "Hash: $gitdir`basename $k`";
	if [[ $k == [0-9]* ]]; then
	  echo "KING OF THE WORLD";
	fi;
	done;
    fi;
  done;
done;
