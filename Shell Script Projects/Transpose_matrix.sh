echo -n "Enter the no of rows:"
read a
echo -n "Enter the no of columns:"
read b
echo "Enter the elements of the matrix:"
for((i=0; i<a; i++))
do
        for((j=0; j<b; j++))
        do
                echo -n "Enter element ($i,$j)"
                read arr[$i$j]
        done
done
for((i=0; i<a; i++))
do
	for((j=0; j<b; j++))
	do
		index=$((i*b+j))
		echo -n "${arr[key]} "
	done
	echo
done
for((i=0; i<a; i++))
do
	for((j=i+1; j<b; j++))
	do
		key1=$((a*i + j))
		key2=$((a*j + i))
		temp=${arr[key1]}
		arr[key1]=${arr[key2]}
		arr[key2]=$temp
	done
done
echo "Transpose of the matrix is:"
for((i=0; i<a; i++))
do
	for((j=0; j<b; j++))
	do
		key=$((i*b+j))
		echo -n "${arr[key]} "
	done
	echo
done
