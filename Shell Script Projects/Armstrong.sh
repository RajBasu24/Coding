echo -n "Enter the number:"
read n
num=n
num2=n
s=0
i=0
while [ $n -gt 0 ]
do
	n=$((n/10))
	i=$((i+1))
done
while [ $num -gt 0 ]
do
	d=$((num%10))
	d=$((echo "$d^$i"|bc))
	s=$((s+d))
	num=$((num/10))
done
if [ $s -eq $num2 ]
then
	echo "The number is Armstrong"
else
	echo "The number is not Armstrong"
fi
