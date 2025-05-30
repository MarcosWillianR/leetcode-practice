# Design Dynamic Array (Resizable Array)
# https://neetcode.io/problems/dynamicArray

# Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

# Your DynamicArray class should support the following operations:

class DynamicArray:
    # -> DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
    def __init__(self, capacity: int):
      if capacity <= 0:
         raise ValueError("Capacity must be greater than 0.")
      
      self._capacity = capacity
      self._size = 0
      self._data = [None] * capacity

    def get(self, i: int) -> int:
       # -> int get(int i) will return the element at index i. Assume that index i is valid.
       return self._data[i]


    def set(self, i: int, n: int) -> None:
       # -> void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
       self._data[i] = n


    def pushback(self, n: int) -> None:
       # -> void pushback(int n) will push the element n to the end of the array.
       # If we call void pushback(int n) but the array is full, we should resize the array first.
      if self._size >= self._capacity:
        self.resize()
       
      self._data[self._size] = n
      self._size += 1


    def popback(self) -> int:
       # -> int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
       self._size -= 1
       return self._data.pop()
 

    def resize(self) -> None:
      # -> void resize() will double the capacity of the array.
      self._capacity *= 2
      new_data = [None] * self._capacity
      for i in range(len(self._data)):
         new_data[i] = self._data[i]
      self._data = new_data

    def getSize(self) -> int:
        # int getSize() will return the number of elements in the array.
        return self._size
    
    def getCapacity(self) -> int:
       # int getCapacity() will return the capacity of the array.
       return self._capacity


dyn_arr = DynamicArray(4)

dyn_arr.pushback(1)
dyn_arr.set(0, 0)
dyn_arr.pushback(2)
dyn_arr.get(0)
dyn_arr.get(1)
dyn_arr.getCapacity()
dyn_arr.popback()



# This test dont pass:
# ["Array", 4, "pushback", 1, "set", 0, 0, "pushback", 2, "get", 0, "get", 1, "getCapacity", "popback"]