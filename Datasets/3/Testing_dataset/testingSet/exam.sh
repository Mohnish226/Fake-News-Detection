#!/bin/bash

OP="./teamEval.csv"

# Real

p_real="/media/sf_Hackathon/Articles/testingSet/real"

printf "True value,Program prediction,Memory,Time\n" > $OP

for i in $(ls -v $p_real)
do cat $p_real/$i | tr -cd '\11\12\15\40-\176' > ./tempTestFile
echo $p_real/$i
#cat ./testFile
#sleep 5
/usr/bin/time -f  ",%M,%e" -ao $OP bash -c 'printf "Real,"; if ./classifier.sh ./tempTestFile > /dev/null; then printf "Real"; else printf "Fake"; fi' >> $OP
done

# Fake

p_fake="/media/sf_Hackathon/Articles/testingSet/fake"

for i in $(ls -v $p_fake)
do cat $p_fake/$i | tr -cd '\11\12\15\40-\176'  > ./tempTestFile
echo $p_fake/$i
/usr/bin/time -f  ",%M,%e" -ao $OP bash -c 'printf "Fake,"; if ./classifier.sh ./tempTestFile >/dev/null; then printf "Real"; else printf "Fake"; fi' >> $OP
done

#/usr/bin/time -f ", %M, %e\n" $1 $2 >/dev/null
