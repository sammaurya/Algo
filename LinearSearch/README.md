# Linear Search
Linear search says that start searching from start till you find the element you are looking for or reach end of the list.

Let's say 

    List: [1, 5, 6, 2, 9, 3]
    Size of list (n): 6
    Indexes: 0 to (n - 1) i.e, 0 to 5
    
Time Complexity:

    Best Case: O(1)
            No matter the size of the list, if the element is found at the start of the list (index 0). 
            That is only one comparison is made to get the element.
            
 <p align="center">
<img src="https://github.com/sammaurya/Algo/blob/master/Diagrams/LinearSearchBestCaseComplexity.svg" width="350" title="hover text">
</p>
            
    Worst Case: O(n)
            If the element is not found in the list. That is total comparisons made is equal to the size
            of the list.
            
<p align="center">
<img src="https://github.com/sammaurya/Algo/blob/master/Diagrams/LinearSearchWorstCaseComplexity.svg" width="350" title="hover text">
</p>


## Problems

#### Search the element in the given index range only? (Search In Index Range)


Ans. Accept the start and end index in the linear_search function and run the search loop within range (start, end)

#### Find the minimum element in the list? (Min in list)

Ans. Take first element as the minimum element or the negative infinity value and compare with each element, if the current elemenet is
     smaller than the previous smaller element than assign current element as smaller element and move forward till we reach the end of the list.
     If the list is empty, then simply return None or negative infinity value.
     
#### Find the maximum element in the list? (Max in list)

Ans. Take first element as the maximum element or the positive infinity value and compare with each element, if the current elemenet is
     larger than the previous larger element than assign current element as larger element and move forward till we reach the end of the list.
     If the list is empty, then simply return None or positive infinity value.
     
#### Find the minimum element in the 2D list? (Min in 2D list)

Ans. Take first element as the minimum element or the negative infinity value and compare with each element, if the current elemenet is
     smaller than the previous smaller element than assign current element as smaller element and move forward till we reach the end of the list.
     If the list is empty, then simply return None or negative infinity value.
     Check if the 2D list is not empty and iterate over rows and columns.
     
#### Find the maximum element in the 2D list? (Max in 2D list)

Ans. Take first element as the maximum element or the positive infinity value and compare with each element, if the current elemenet is
     larger than the previous larger element than assign current element as larger element and move forward till we reach the end of the list.
     If the list is empty, then simply return None or positive infinity value.
     Check if the 2D list is not empty and iterate over rows and columns.
