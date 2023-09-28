echo "Enter a number:"
read x
if [ `expr $x % 2` -eq 0 ]
	then
		echo "$x is even"
	else
		echo "$x is odd"
fi
