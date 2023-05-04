#User function Template for python3
import heapq
class Solution:
    #Heapify function to maintain heap property.
    def leftchild(self,current):
        return (current * 2) + 1
    def rightchild(self,current):
        return (current * 2) + 2
    def swap(self,arr,c,n):
        arr[c],arr[n] = arr[n],arr[c]
    def heapify(self,arr, n, current):
        if self.leftchild(current) < n:
            l = self.leftchild(current)
            r = self.rightchild(current)
            smallest = current
            
            if arr[l] > arr[smallest]:
                smallest = l
                
            if r < n and arr[r] > arr[smallest]:
                smallest = r
            if smallest != current:
                self.swap(arr,current,smallest)
                self.heapify(arr, n, smallest)

        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        lp = n // 2 - 1
        for i in range(lp,-1,-1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,len(arr))
        #heapq.heapify(arr)
        n = len(arr)
        while n:
            self.swap(arr,0,n-1)
            n -= 1
            self.heapify(arr,n,0)
            
  
        
        
