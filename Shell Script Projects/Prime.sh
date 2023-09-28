echo -n "Enter the number:"
read n
flag=0
for((i=2; i<n; i++))
do
	a=$((n%i))
	if [ $a -eq 0 ]
	then
		flag=$((flag+1))
	fi
done
if [ $flag -eq 0 ]
then
	echo "$n is Prime"
else
	echo "$n is not Prime"
fi
