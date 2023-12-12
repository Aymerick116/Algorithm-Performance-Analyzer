# Algorithm-Performance-Analyzer
Design and Analysis of Algorithms Programing Project
Aymerick Osse

1. Problem Definition:
•	The problem at hand is the Selection Problem. Given an array A [1…n] of n elements, the objective is to find the i-th order statistic, where  1 <=i<= n. The i-th order statistic represents the i-th smallest element in the array.

•	The input size for this problem is determined by the array A [1…n], where n is the number of elements in the array. The project specifies that the algorithms will be analyzed for various values of n ranging from 1,000 to 10,000 in increments of 1,000. 

•	The Selection Problem has practical applications in various real-world scenarios. For instance, consider a situation where you have a dataset representing the performance scores of students in a class. Finding the i-th order statistic could help identify the i-th highest-scoring student. This kind of analysis is valuable in fields such as data science, finance (identifying top performers in a stock portfolio), or any domain where ranking or order statistics are crucial for decision-making.


2. Algorithms and RT analysis. Write the pseudocode for each algorithm and RT
analysis.

Insertion Sort
•	Pseudocode
insertion_sort(arr)
for i = 1 to n - 1
key = arr[i]
j = i - 1
while j >= 0 and key < arr[j]
arr[j + 1] = arr[j]
j = j - 1
arr[j + 1] = key
•	Pseudocode ALG1
ALG1(A,n,i)
   Insertion-sort(arr)
   Print A[i-1]
•	Runtime Analysis:
o	Time complexity(theoretical): O(n^2) - Quadratic time - Worst-case time complexity.
o	Space complexity: O(1) – Constant time



Merge Sort
•	Pseudocode
merge_sort(arr, p, r):
  if p < r
    q = (p + r) / 2
    merge_sort(arr, p, q)
    merge_sort(arr, q + 1, r)
    merge(arr, p, q, r)

merge(arr, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  left_half = [arr[p + i] for i in range(n1)]
  right_half = [arr[q + 1 + j] for j in range(n2)]
  i = j = 0
  k = p
  while i < n1 and (j >= n2 or left_half[i] <= right_half[j])
    arr[k] = left_half[i]
    i = i + 1
    k = k + 1
  while j < n2
    arr[k] = right_half[j]
    j = j + 1
    k = k + 1
•	Pseudocode ALG2
  ALG2(A,n,i)
   	Merge-sort(A,n,i)
   	Print A[i-1]


•	Runtime Analysis:
o	Time complexity(theoretical): O(n log n)
o	Space complexity: O(n) 


Randomized-select
•	Pseudocode
randomized_select(arr, p, r, i)
  if p = r
    return arr[p]
  q = randomized_partition(arr, p, r)
  k = q - p + 1
  if i = k
    return arr[q]
  else if i < k
    return randomized_select(arr, p, q - 1, i)
  else
    return randomized_select(arr, q + 1, r, i - k)

randomized_partition(arr, p, r)
  i = random.randint(p, r)
  swap(arr[r], arr[i])
  return partition(arr, p, r)

partition(arr, p, r)
  x = arr[r]
  i = p - 1
  for j = p to r - 1
    if arr[j] <= x
      i = i + 1
      swap(arr[i], arr[j])
  swap(arr[i + 1], arr[r])
  return i + 1

•	Pseudocode ALG3
   ALG3(arr, n, i):
    	result = randomized_select(arr, n - 1, i)
    	print (result)


•	Runtime Analysis:
o	Time complexity(theoretical): O(n)
o	Space complexity: O( log n) 















3. Experimental Results. Include the 3 tables and 4 graphs.

Table for ALG1
 



Table for ALG2
 




Table for ALG3
 
























Empirical Runtimes of the 3 Algorithms
 







Empirical vs Predicted Runtimes ALG1  

Empirical vs Predicted Runtimes ALG2  
Empirical vs Predicted Runtimes ALG3  






















4. Conclusions

What conclusions can you draw from your experiments? Are the
theoretical and empirical results consistent?

In conclusion, the empirical experiments conducted on the algorithms (ALG1, ALG2, and ALG3) for solving the Selection Problem align closely with their respective theoretical analyses. ALG1, implementing Insertion Sort, exhibits a quadratic growth in empirical runtimes, consistent with its expected quadratic time complexity. ALG2, employing Merge Sort, demonstrates an empirical runtime growth in line with its linearithmic theoretical complexity. Similarly, ALG3, utilizing Randomized Select, displays linear growth in empirical runtimes, supporting its anticipated linear time complexity. The ratios between empirical and theoretical runtimes are relatively small, suggesting that the algorithms' performances closely adhere to their expected complexities. These findings underscore the reliability of theoretical predictions in assessing algorithmic efficiency and provide confidence in the accurate implementation and analysis of the algorithms for the Selection Problem.










