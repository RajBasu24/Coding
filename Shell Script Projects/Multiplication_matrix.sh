echo -n "Enter the no of rows:"
read a
echo -n "Enter the no of columns:"
read b
echo "Enter the elements of 1st matrix:"
for((i=0; i<a; i++))
do
        for((j=0; j<b; j++))
        do
                echo -n "Enter element ($i,$j)"
                read arr1[$i$j]
        done
done
echo "Enter the elements of 2nd matrix:"
for((i=0; i<a; i++))
do
        for((j=0; j<b; j++))
        do
                echo -n "Enter element ($i,$j)"
                read arr2[$i$j]
        done
done
for((i=0; i<a; i++))
do
        for((j=0; j<b; j++))
        do
                arr3[$i$j]=`expr ${arr1[$i$j]} \* ${arr2[$i$j]}`
        done
done
echo "Matrix after multiplication is:"
for((i=0; i<a; i++))
do
        for((j=0; j<b; j++))
        do
                echo -n "${arr3[$i$j]} "
        done
        echo ""
done
