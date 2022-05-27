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
            
            ![image](https://user-images.githubusercontent.com/31203196/170693725-daf55f9b-d07d-4244-854b-15bdfaf440ae.png)

            
    Worst Case: O(n)
            If the element is not found in the list. That is total comparisons made is equal to the size
            of the list.
            
