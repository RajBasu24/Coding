echo "Enter two numbers:"
read x
read y
if [ $x -gt $y ]
then
	echo "$x is greater than $y"
else	
	echo "$y is greatar than $x"
fi
