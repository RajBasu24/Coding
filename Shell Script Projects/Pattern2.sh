echo -n "Enter the no of rows:"
read n
for((i=1; i<=$n; i++))
do
	for((j=1; j<=$((n-i)); j++))
	do
		echo -n -e " "
	done
	for((k=1; k<=$i;k++))
	do
		echo -n -e "*"
	done
	echo -n -e "\n"
done
