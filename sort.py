Insertion/Bubble sort
Merge sort
Heap/binary sort
Quick sort

QUICKSORT.A; p; r/
1 ifp < r
2 q D PARTITION.A; p; r/
3 QUICKSORT.A; p; q  1/
4 QUICKSORT.A; q C 1; r/

PARTITION.A; p; r/
1 x D AOEr
2 i D p  1
3 for j D p to r  1
4 if AOEj   x
5 i D i C 1
6 exchange AOEi with AOEj 
7 exchange AOEi C 1 with AOEr
8 return i C 1