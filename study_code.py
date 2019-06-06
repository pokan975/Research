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

# =============================================================================
# a = "Let's take LeetCode contest"
# aa = a.split(' ')
# rev = []
# for i in aa:
#     rev.append(i[::-1])
# ans = ' '.join(rev)
# =============================================================================

# =============================================================================
# emails = ["test.email+alex@leetcode.com","testemail+david@lee.tcode.com","test.e.mail+bob.cathy@leetcode.com"]
# addr = set()
# for i in emails:
#     local, domain = i.split('@')
#     if '+' in local:
#         local = local[:local.index('+')]
#     addr.add(local.replace('.','')+'@'+domain)
# print(len(addr))
# 
# aa = {'google','facebook','apple'}
# print(aa)
# aa.add('google')
# print(aa)
# =============================================================================

# =============================================================================
# moves = "UD"
# print(moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'))
# =============================================================================

# =============================================================================
# grid = [[1,1,1],[1,0,1],[1,1,1]]
# x = 0
# y = [0]*len(grid[0])
# z = len(grid)**2
# for i in grid:
#     x = x + max(i)
#     z = z - i.count(0)
#     for j in range(len(i)):
#         if y[j] < i[j]:
#             y[j] = i[j]
# print(x+z+sum(y))
# =============================================================================

# =============================================================================
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 
# class Solution:
#     def mergeTrees(self, t1, t2):
#         """
#         :type t1: TreeNode
#         :type t2: TreeNode
#         :rtype: TreeNode
#         """
#         if t1 == None:
#             return t2
#         if t2 == None:
#             return t1
#         
#         t1.val = t1.val+t2.val
#         t1.left = self.mergeTrees(t1.left,t2.left)
#         t1.right = self.mergeTrees(t1.right,t2.right)
#         
#         return t1
# =============================================================================
    
# =============================================================================
# class Solution:
#     def searchBST(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode
#         """
#         if not root: # equals (if root == None)
#             return None
#         if root.val == val:
#             return root
#         
#         return self.searchBST(root.left, val) or self.searchBST(root.right, val)
# =============================================================================

# =============================================================================
# ops = ["5","2","C","D","+"]
# ans = []
# for i in ops:
#     if i is "D":
#         ans.append(ans[-1]*2)
#     elif i is "C":
#         ans.pop(-1)
#     elif i is "+":
#         ans.append(ans[-1]+ans[-2])
#     else:
#         ans.append(int(i))
# print(sum(ans))
# =============================================================================

# =============================================================================
# grid = [[1,0]]
# row_N = len(grid[0])
# col_N = len(grid)
# block = 0
# side = 0
# for i in grid:
#     block += sum(i)
# if row_N > 1:
#     for col in range(col_N):
#         for row in range(1,row_N):
#             side = side + (grid[col][row-1] and grid[col][row])
# 
# if col_N > 1:
#     for row in range(row_N):
#         for col in range(1,col_N):
#             side = side + (grid[col-1][row] and grid[col][row])
# print(block*4-side*2)
# =============================================================================

# =============================================================================
# N = 8
# ans = 0
# bin_str = bin(N)
# a = len(bin_str)
# k = bin_str.index('1')
# last_k = a-1-(bin_str[::-1].index('1'))
# while k != last_k:
#     kk = bin_str[k+1::].index('1')
#     if kk+1 > ans:
#         ans = kk+1
#     k = k + kk + 1
# class Solution:
#     def binaryGap(self, N):
#         A = [i for i in range(32) if (N >> i) & 1]
#         if len(A) < 2: 
#             return 0
#         return max(A[i+1] - A[i] for i in range(len(A) - 1))
# =============================================================================

# =============================================================================
# class Solution:
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int], only 1 num is unique, find that
#         :rtype: int
#         nums=[4,1,2,1,2] -> return 4
#         """
#         from functools import reduce
#         return reduce(lambda x, y: x ^ y, nums)
# def singleNumber(self, nums):
#         standard = 0
#         for i, v in enumerate(nums):
#             standard = v ^ standard
#         return standard
# =============================================================================

# =============================================================================
# n = 7
# bit = bin(n)
# print(all(bit[i] != bit[i+1] for i in range(len(bit)-1)))
# =============================================================================

# =============================================================================
# nums = [[1,2], [3,4]]
# r, c = 2, 2
# total = [i for sub in nums for i in sub]
# ans = []
# for ii in range(r):
#     ans.append(total[ii*c:(ii+1)*c:])
# 
# if len(nums)*len(nums[0]) == r*c:
#     ans = [[nums[(y*c+x)//len(nums[0])][(y*c+x)%len(nums[0])] for x in range(c)] for y in range(r)]
# else: 
#     ans = nums
# =============================================================================

# =============================================================================
# candies = [1,2,2,2,3,3,4,4,4,5,5,5,5,5,5,5]
# sister = min(len(set(candies)), int(len(candies)/2))
# =============================================================================

# =============================================================================
# A=[1,2,2,3]
# ans = (all(A[i] >= A[i+1] for i in range(len(A)-1))) or (all(A[i] <= A[i+1] for i in range(len(A)-1)))
# =============================================================================

# =============================================================================
# S = "a-bC-dEf-ghIj"
# letters = [c for c in S if c.isalpha()]
# ans = []
# for i in S:
#     if i.isalpha():
#         ans.append(letters.pop())
#     else:
#         ans.append(i)
# ReverseOnlyLetters = ''.join(ans)
# =============================================================================

# =============================================================================
# class Solution:
#     def addDigits(self, num):
# #        :type num: int
# #        :rtype: int
#         from functools import reduce
#         if num < 10:
#             return num
#         else:
#             added = reduce(lambda x,y: x+y,[int(i) for i in str(num)])
#             return self.addDigits(added)
# =============================================================================

# =============================================================================
# nums = [1,1,0,1,1,1]
# cur_len = 0
# lens = [0]
# for i in nums:
#     if i:
#         cur_len+= 1
#     else:
#         if cur_len:
#             lens.append(cur_len)
#             cur_len = 0
# if cur_len:
#     lens.append(cur_len)
# ans = max(lens)
# =============================================================================

# =============================================================================
# L, R = 6, 10
# ans = 0
# prime_bits = {2,3,5,7,11,13,17,19}
# for i in range(L,R+1):
#     binary = bin(i)
#     if binary.counter("1") in prime_bits:
#         ans+=1
# print("Number of prime set bits = ",ans)
# =============================================================================

# =============================================================================
# nums = [0,0,1]
# i = 0
# for counter in range(len(nums)):
#     if nums[i] is 0:
#         temp = nums.pop(i)
#         nums.append(temp)
#     else:
#         i+=1
# =============================================================================

# =============================================================================
# def Solution(self, word):
# #    :type word: str
# #    :rtype: bool
#     from functools import reduce
#     ASCII = [ord(i) for i in word]
#     bool_list = list(map(lambda x: 65 <= x <= 90, ASCII))
# 
#     if len(bool_list) is 1:
#         return True
#         
#     if bool_list[0] is True:
#         bool_set = set(bool_list[1:])
#         if len(bool_set) is 1:
#             return True
#         else:
#             return False
#     else:
#         bool_rest = reduce(lambda x, y: x or y, bool_list[1:])
#         if bool_rest is False:
#             return True
#         else:
#             return False
# 
# def detectCapitalUse(self, word):
#     return word.lower()==word or word.upper()==word or (word[0].upper()==word[0] and word[1:].lower() == word[1:])
# =============================================================================

# =============================================================================
# # K points that are nearest to origin 
# points = [[3,3],[5,-1],[-2,4]]
# K = 2
# points.sort(key = lambda coord: coord[0]**2 + coord[1]**2)
# ans = points[:K]
# =============================================================================

# =============================================================================
# N = 2
# a,b = 0,1
# for _ in range(N):
#     a, b = b, a+b
# Fibonacci_num = a
# =============================================================================

# =============================================================================
# nums = [9,6,4,2,3,5,7,0,1]
# a = list(set(nums)) #把一個list用set()轉成set會自動做排序
# =============================================================================

# =============================================================================
# def summ(x: int, y: int) -> bool:
#     return x + y
# 
# nums = [1,2,3,1,2,3]
# k = 3
# dic = {}
# ans = False
# 
# for i in range(len(nums)):
#     current = nums[i]
#     if current in dic and i-dic[current] <= k: #{val : index}
#         ans = True
#     else:
#         dic[current] = i
# 
# print(summ(2, 3))
# =============================================================================

# =============================================================================
# import re
# 
# s1 = "This is a test\n"
# s2 = "\n"
# s3 = "allee@asu.edu\n"
# s4 = "\n"
# string = [s1,s2,s3,s4]
# 
# f = open("test.txt", "w")
# 
# for line in string:
#     f.write(line)
#     match = re.search(r"^T[\S]+\s", line)
#     if match:
#         line = "insert\n"
#         f.write(line)
# 
# f.close()
# =============================================================================

# =============================================================================
# import re
# num = list(range(1,11))
# total = len(num)
# invalid = 0
# invalid1 = {'0','1','8'}
# invalid2 = {'3','4','7'}
# 
# for i in num:
#     number = str(i)
#     digi_list = re.findall(r'\d', number)
#     digits = set(digi_list)
#     if digits.issubset(invalid1):
#         invalid += 1
#     if not digits.isdisjoint(invalid2):
#         invalid += 1
# =============================================================================

string = "(()())(())(()(()))"
res = []
balance = 0
i = 0

for j in range(len(string)):
    if string[j] == "(":
        balance += 1
    elif string[j] == ")":
        balance -= 1
    if balance == 0:
        res.append(string[i+1:j])
        i = j+1
ans = "".join(res)

# =============================================================================
# string = "   -42"
# 
# i, ans = 0, 0
# num = ""
# 
# strlist = string.split(" ")
# if (strlist[0][0] == "-" or strlist[0][0].isdigit()):
#     num = num + strlist[0]
# =============================================================================

# =============================================================================
# ROMAN = [
#     (1000, "M"),
#     ( 900, "CM"),
#     ( 500, "D"),
#     ( 400, "CD"),
#     ( 100, "C"),
#     (  90, "XC"),
#     (  50, "L"),
#     (  40, "XL"),
#     (  10, "X"),
#     (   9, "IX"),
#     (   5, "V"),
#     (   4, "IV"),
#     (   1, "I"),
# ]
# 
# number = 19
# result = ""
# for (arabic, roman) in ROMAN:
#     (factor, number) = divmod(number, arabic)
#     result += roman * factor
# =============================================================================

# =============================================================================
# stones = [2,2]
# stones.sort()
# 
# while(len(stones) > 1):
#     if len(stones) >= 2:
#         remain = abs(stones.pop() - stones.pop())
#         if remain != 0:
#             stones.append(remain)
#             stones.sort()
#     else:
#         break
# =============================================================================

# =============================================================================
# n = 10
# from math import sqrt
# prime = [1]*n
# prime[0] = 0
# prime[1] = 0
# 
# upper = int(sqrt(n))
# 
# for i in range(2,upper+1):
#     if not prime[i]:
#         continue
#     for j in range(i**2,n,i):
#         prime[j] = 0
# 
# count = sum(prime)
# =============================================================================

# =============================================================================
# grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# 
# v = len(grid)
# h = len(grid[0])
# 
# skylineV = [0]*v
# skylineH = [0]*h
# 
# for i in range(v):
#     skylineV[i] = max(grid[i])
#     
#     for j in range(h):
#         skylineH[j] = max(skylineH[j], grid[i][j])
# 
# count = 0
# for i in range(v):
#     for j in range(h):
#         inc = min(skylineV[i], skylineH[j]) - grid[i][j]
#         count += inc
# =============================================================================

# =============================================================================
# nums = [2, 2, 3, 1]
# nums = set(nums)
# if len(nums) > 2:
#     nums.remove(max(nums))
#     nums.remove(max(nums))
# ans = max(nums)
# =============================================================================

from collections import Counter
words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"

patlen = Counter(pattern)

i = 0
while(i<len(words)):
    if len(Counter(words[i])) != len(patlen):
        words.remove(words[i])
    else:
        i += 1
        
outtab = "".join(patlen)
ans = []
for word in words:
    intab = "".join(Counter(word))
    transtab = word.maketrans(intab, outtab)
    if word.translate(transtab) == pattern:
        ans.append(word)
