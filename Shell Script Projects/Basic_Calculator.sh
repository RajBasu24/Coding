echo -n "Enter 1st number:"
read a
echo -n "Enter 2nd number:"
read b
while [ 1 ]
do
	echo -e "Enter 1 for Addition\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 for Modulus\nEnter 6 for Exit"
	echo -n "Enter your choice:"
	read ch
	case "$ch" in
		1) c=$((a+b));;
		2) c=$((a-b));;
		3) c=$((a*b));;
		4) c=$((a/b));;
		5) c=$((a%b));;
		6) exit 0;;
		*) echo "Enter correct choice"
		exit 0;;
	esac
	echo "Result is $c"
done
