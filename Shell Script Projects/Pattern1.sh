echo -n "Enter the no of rows:"
read n
for ((i=1; i<=$n; i++))
do
	for((j=1; j<=$i; j++))
	do
		echo -n -e "*"
	done
	echo -e -n "\n"
done
