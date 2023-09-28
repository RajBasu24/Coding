echo -n "Enter the number:"
read n
temp=$n
sum=0
while [ $n -gt 0 ]
do
	num=$((n%10))
	f=$((sum\*10))
	sum=$((f+num))
	n=$((n/10))
done
if [ $temp -eq $sum ]
then
	echo "$temp is Palindrome number"
else
	echo "$temp is not Palindrome number"
fi
