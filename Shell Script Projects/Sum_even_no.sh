echo -n "Enter the no of elements:"
read n
echo "Enter the elements:"
for((i=0; i<n; i++))
do
        read a[$i]
done
temp=0
for((i=0; i<n; i++))
do
        if [ $((a[i]%2)) -eq 0 ]
        then
                temp=$((temp+a[i]))
        fi
done
echo "Sum of even numbers is $temp"
