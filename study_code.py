# -*- coding: utf-8 -*-
"""
@author: William
"""
# =============================================================================
# class Solution:
#     def twosum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i,j]
#                 
#         raise ValueError('No Solution!')
# 
# ans = Solution()
# a = ans.twosum([3,2,4],5)
# =============================================================================

# =============================================================================
# class Solution:
#     def numJewelsInStones(self, J, S):
#         total = 0
#         for i in range(len(J)):
#             total = total + S.count(J[i])
#             
#         return total
#             
# ans = Solution()
# a = ans.numJewelsInStones('z','ZZ')
# 
# def conv(x):
#     return ord(x)
# 
# a = 'aA'
# table = list(a)
# data = list(map(conv,table))
# num = len(a)
# b = 'babAAb'
# num = b.count('A')
# =============================================================================

# =============================================================================
# class Solution:
#     def toLowerCase(self, str):
#         """
#         :type str: str
#         :rtype: str
#         """
#         def conv(x):
#             if x >= 65 and x <= 90:
#                 return x + 32
#             else:
#                 return x
#         
#         a = list(map(ord,str))
#         b = list(map(conv,a))
#         
#         return ''.join(map(chr,b))
# =============================================================================

# =============================================================================
# from math import floor
# 
# table = [[1,1,0],[1,0,1],[0,0,0]]
# for row in table:
#     for i in range(floor((len(row)+1)/2)):
#         row[i], row[~i] = row[~i]^1, row[i]^1
# =============================================================================

# =============================================================================
# a = [1,3,5,8,6,7]
# a.sort(key = lambda x: x%2)
# =============================================================================

# =============================================================================
# a = [1,8,5,6,2,4,3,7]
# ans = [None]*len(a)
# even = 0
# odd = 1
# for i in range(len(a)):
#     if a[i]%2 == 0:
#         ans[even]=a[i]
#         even+=2
#     
#     if a[i]%2 == 1:
#         ans[odd]=a[i]
#         odd+=2
# 
# print(id(a[0]))
# print(id(ans[1]))
# ans[1]+=1
# print(id(a[0]))
# print(id(ans[1]))
# =============================================================================

# =============================================================================
# left=1
# right=28
# ans = []
# for i in range(left,right+1):
#     flag = 0
#     for j in str(i):
#         if j == '0' or i%int(j) != 0:
#             flag = 1
#             break
#     if flag == 0:
#         ans.append(i)
# =============================================================================

# =============================================================================
# a=[0,1,3,1]
# ans=a.index(max(a))
# =============================================================================

# =============================================================================
# from collections import Counter
# a = [5,1,5,2,5,3,5,4]
# count = Counter(a).most_common(1)
# print(count[0][0])
# =============================================================================

# =============================================================================
# x = 1
# y = 4
# ans = bin(x^y).count('1')
# =============================================================================

# =============================================================================
# a=[[1,2,3],[4,5,6],[7,8,9]]
# ans = []
# for i  in range(len(a[0])):
#     temp = []
#     for j in range(len(a)):
#         temp.append(a[j][i])
#     ans.append(temp)
# =============================================================================

# =============================================================================
# a = "ABCDEFGHIJKLM"
# print(a[::-1])
# print(a[0:10:2])
# print(a[-5::-2])
# =============================================================================

# =============================================================================
# a = 5
# b = '1'*len(bin(a)[2::])
# bb = int(b,base=2)-a
# print(bb)
# =============================================================================

# =============================================================================
# x,*y,z='abcdefg'
# group = {}
# a = True
# S = [[1,2,3],[4,1,2],[5,4,1]]
# for r,row in enumerate(S):
#     for c,val in enumerate(row):
#         if (r-c) not in group:
#             group[r-c]=val
#         elif group[r-c] != val:
#             a=False
# print(a)
# g = {} #empty set
# g[0]=S[0]
# =============================================================================

# =============================================================================
# from collections import Counter
# A = 'apple apple'
# B = "banana"
# ans = []
# c = A.split(' ') + B.split(' ')
# d = Counter(c)
# for i in c:
#     if d[i] == 1:
#         ans.append(i)
# =============================================================================

# =============================================================================
# a=[1,4,3,2]
# a.sort()
# sum = 0
# for i in range(int(len(a)/2)):
#     sum += a[2*i]
# =============================================================================

# =============================================================================
# morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
#          "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# words = ["gin", "zen", "gig", "msg"]
# group = {}
# i = 0
# for word in words:
#     code = []
#     for c in word:
#         code.append(morse[ord(c) - ord('a')])
#     morse_code = ''.join(code)
#     if morse_code not in group:
#         group[morse_code] = i
#         i += 1
# =============================================================================

a = "Let's take LeetCode contest"
aa = a.split(' ')
rev = []
for i in aa:
    rev.append(i[::-1])
ans = ' '.join(rev)
