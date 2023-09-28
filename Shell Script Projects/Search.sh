echo -n "Enter the no of elements:"
read n
echo "Enter the elements:"
for((i=0; i<n; i++))
do
	read a[$i]
done
echo -n "Enter the number to be searched:"
read key
temp=0
a=0
for i in ${a[@]}
do
	((a++))
	if [ $i -eq $key ]
	then
		temp=1
		a=$a
		break
	fi
done
if [ $temp -eq 1 ]
then
	echo "$key is found in position $a"
else
	echo "$key is not found"
fi
