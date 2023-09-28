echo -n "Enter the number:"
read n
sum=0
while [ $n -gt 0 ]
do
	temp=$((n%10))
	sum=$((sum+temp))
	n=$((n/10))
done
echo "Sum of the digits is $sum"
