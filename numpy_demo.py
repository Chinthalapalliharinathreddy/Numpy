import numpy as np

#arr=np.array([1,2,3,4,5])
#print(arr)

#b=np.array([[1,2],[3,4]])
#print(b)

#a = np.array([[[10, 20],[30, 40]],[[50, 60],[70, 80]]])
#print(a)
#print(a[0,0,0])
#print(a[1,1,0])

#asarray() using nditer()
#a=[10,20,30,40,50]
#arr=np.asarray(a,dtype=float)
#for i in np.nditer(arr):
#   print(i)

#np.frombuffer() Creates an array from binary data
#a=b"Welcome to numpy"
#arr=np.frombuffer(a,dtype='S1',offset=1)
#print(arr)

#fromiter() Creates an array from an iterable object
#n=iter([10,20,30,40,50])
#arr=np.fromiter(n,dtype=int)
#print(arr)

#Zeros() Creates an array filled with zeros
#arr=np.zeros((1,2))
#print(arr)

#Ones() Creates an array filled with ones
#a=np.ones((2,3))
#print(a)

#Empty() Creates an array without initializing its values
#arr=np.empty((2,3))
#print(arr)

#full() Creates an array filled with a specified value
#arr=np.full((2,3),5)
#print(arr)

#arange() Creates an array with a range of values
#arr=np.arange(0,10,2)
#print(arr)

#eye() Creates a 2-D array with ones on the diagonal and zeros elsewhere
#arr=np.eye(3)
#print(arr)

#linspace() Creates an array of evenly spaced values over a specified range
#arr=np.linspace(0,1,5)
#print(arr)

#random.rand() Creates an array of random values between 0 and 1
#arr=np.random.rand(2,3)    
#print(arr)

#random.randint() Creates an array of random integers between a specified range
#arr=np.random.randint(0,10,(2,3))
#print(arr)