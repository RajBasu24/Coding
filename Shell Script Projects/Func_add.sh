add_num()
{
	local num1=$1
	local num2=$2
	local sum=$((num1 + num2))
	echo "The sum is $sum"
}
echo -n "Enter 1st number:"
read num1
echo -n "Enter 2nd number:"
read num2
add_num $num1 $num2
