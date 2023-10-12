swap_num()
{
	local num1=$1
	local num2=$2
	echo "Before swapping:"
	echo "$num1 $num2"
	echo "After swapping:"
	num1=$((num1 + num2))
	num2=$((num1 - num2))
	num1=$((num1 - num2))
	echo "$num1 $num2"
}
echo -n "Enter 1st number:"
read num1
echo -n "Enter 2nd number:"
read num2
swap_num $num1 $num2
