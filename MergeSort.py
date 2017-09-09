#!/usr/bin/env python

def merge(a, b):
   z = []
   x, y = (0, 0)
   while x < len(a) and y < len(b):
      if a[x] < b[y]:
         z.append(a[x])
         x = x + 1
      else:
         z.append(b[y])
         y = y + 1

   if x < len(a):
      z = z + a[x:]

   if y < len(b):
      z = z + b[y:]

   return z

def mergesort(a):
   n = len(a)
   return a if n == 1 else merge(mergesort(a[:n/2]), mergesort(a[n/2:]))
