fact_num()
{
	local num=$1
	local fact=1
	for((i=1; i<=num; i++))
	do
		fact=$((fact*i))
	done
	echo "Factorial of the number is $fact"
}
echo -n "Enter a number:"
read num
fact_num $num
