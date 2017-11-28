import numpy as np
import timeit
import csv

# A=np.array([
# [90,49,10,15],
# [10,11,12,14],
# [11,15,20,14]
# ])

# cal = A.sum(axis=1)
# print(cal)
#-------------------------------------------------------------------------------
# def calculate_profit(day):
#   return float(day['Revenue']) - float(day['Cost'])
#
#
# def parser():
#     with open('/Users/thomasgrimes/Desktop/PythonDataScienceHandbook-master/revenue.csv') as csvfile:
#         reader = csv.DictReader(csvfile)
#         # print(reader)
#         #
#         for row in reader:
#             print(row)
        #
        # for day in reader:
        #     print('%10s: %10.2f' % (day['Date'], calculate_profit(day)))
# parser()
#------------------------------------------------------------------------------_

# np_2d = np.array([[1, 1.5, 1.75, 0.75, 1.25],[50, 55, 62, 47, 84]])
# print(np_2d.shape) #Telling us how many rows and how many columns in the 2D array above(rows,columns)
# np_2d.reshape(10,1)
#------------------------------------------------------------------------------_

# a = list(range(6))
#
#
# n = np.array(a)
# n3 = np.random.randint(10, size=(3,4,5))
# print(n.shape)
#------------------------------------------------------------------------------_
#------------------------------------------------------------------------------_
#------------------------------------------------------------------------------_

#Excercises
# a = np.array([1,2,3,4,5,6,7,8,9,10])
# v1 = np.zeros(10)

# Create a null vector of size 10
# print(v1)

# How to find the memory size of any array
# print(a.itemsize)#Number of bytes used
# print(a.size)#Number of elements in an array
# print(help(np.itemsize))

# Create a null vector of size 10 but the fifth value which is 1
# v1[4] = 1
# print(v1)

# Create a vector with values ranging from 10 to 49
# 1st arg: (START #), 2nd arg: (STOP #), 3rd arg: incrementer)
# x = np.arange(10,50,1)
# print(x)

# Reverse a vector (first element becomes last)
#print(a[::-1])

# Create a 3x3 matrix with values ranging from 0 to 8
# x = np.arange(0,9).reshape(3,3)
# print(x)

# Find indices of non-zero elements from [1,2,0,0,4,0]
# d = [0,1,2,3,0,1,2,3,0,1,2,3]
# print(np.nonzero(d))

# Create a 3x3x3 array with random values
# x = np.random.rand(3,3)
# print(x)

# Create a 10x10 array with random values and find the minimum and maximum values
# Keep in mind the np MIN is different than the regular one dimensional
# built in MIN function
# x = np.random.rand(10,10)*100
# print(x)
# print(np.min(x))
# print(np.max(x))

# Create a random vector of size 30 and find the mean value
# x = np.arange(31)
# print(np.mean(x))

# Create a 2d array with 1 on the border and 0 inside
# x = np.ones((5,5))
# x[1:-1,1:-1] = 0
# print(x)

x = np.arange(31)











#------------------------------------------------------------------------------_
