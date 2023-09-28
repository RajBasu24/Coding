echo -n "Enter the number:"
read n
sum=0
while [ $n -gt 0 ]
do
	temp=$((n%10))
	a=$((sum \* 10))
	sum=$((a+temp))
	n=$((n/10))
done
echo "Reverse of the number is $sum"
