echo "Enter two numbers"
read x
read y
echo "Choose the option:"
echo "1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division, 5 for Modulus, 6 for Exponent"
read z
if [ $z -eq 1 ]
then
	s=$(( $x + $y ))
	echo "Addition of $x and $y is $s"
elif [ $z -eq 2 ]
then
	s=$(( $x - $y ))
	echo "Subtraction of $x and $y is $s"
elif [ $z -eq 3 ]
then
	s=$(( $x * $y ))
	echo "Multiplication of $x and $y is $s"
elif [ $z -eq 4 ]
then
	s=$(( $x / $y ))
	echo "Division of $x and $y is $s"
elif [ $z -eq 5 ]
then
	s=$(( $x % $y ))
	echo "Modulus of $x and $y is $s"
elif [ $z -eq 6 ]
then
	s=$(( $x ** $y ))
	echo "Exponent of $x and $y is $s"
else
	echo "You have entered wrong input"
fi
