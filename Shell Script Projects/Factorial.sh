echo -n "Enter the number:"
read n
i=1
f=1
while [ $i -le $n ]
do
	f=$((f*i))
	((i++))
done
echo "Factorial is $f"
