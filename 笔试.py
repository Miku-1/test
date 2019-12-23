# 朴素字符串匹配算法(暴力匹配)
# string_s = 'china'
# string_p = 'ina'
# def NaiveStringSearch(string_s,string_p):
#     i, j = 0, 0
#     while i < len(string_s) and j < len(string_p):
#         # 如果相等 判断下一位
#         if string_s[i] == string_p[j]:
#             i += 1
#             j += 1
#         # 匹配失败,移到串s中的下一个位置
#         else:
#             i = i -j + 1
#             j = 0
#     # 如果匹配到字符串,输出串S中的下标位置,不存在 则输出Error
#     if j == len(string_p):
#         return i-j
#     else:
#         return "Error"
# print(NaiveStringSearch(string_s,string_p))

# KMP算法 next数组求法
# def get_next(string):
#     j = 0
#     next = [0]
#     k = 0
#     for i in range(1,len(string)):
#         while k > 0 and string[k] != string[i]:
#             k = next[ k-1 ]
#         if string[k] == string[i]:
#             k += 1
#         next.append(k)
#     return next
# name = get_next('ABCDABCD')
# print(name)

# 罗马数字转阿拉伯数字
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         a = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
#         b = 0
#         for i in range(len(s)-1):  #这里遍历字符串的时候选择了遍历每个字符的下标，为了防止下标超出就遍历到len(s)-1
#             if a[s[i]] >= a[s[i+1]]:  #如果前大于后则正常相加
#                 b += a[s[i]]
#             else:
#                 b -= a[s[i]]	#如果前大于后就减去当前值
#
#         b += a[s[len(s)-1]]
#         return b

#二进制数字中最大连续1的个数
# num = int(input())
# def get_max_consecutive_num(num):
#     bin_num = bin(num)
#     string = str(bin_num)[2:]
#     print(string)
#     ones_list = string.split("0")
#     # print(ones_list)
#     return len(max(ones_list))
# print(get_max_consecutive_num(num))

# 先排序 再与原来的数字作比较,
# 若某位不同 记录原数字组数字为m
# 记录排序后当前数字为n
# 找到原数字组中最低位次值为n的数字与m交换
# def get_max_swapnum(num):
#     num_list = list(str(num))
#     sort_num_list = sorted(num_list,reverse=True)
#     print(sort_num_list)
#     for i in range(len(num_list)):
#         if num_list[i] != sort_num_list[i]:
#             num_list[str(num).rfind(sort_num_list[i])] = num_list[i]
#             num_list[i] = sort_num_list[i]
#             break
#     return int("".join(num_list))
# print(get_max_swapnum(139820))
# 思路
# 偶数直接向右移位运算
# 奇数时分两种情况
#     1,01结尾时取n-1
#     2,11结尾时取n+1
# 11结尾中3为特殊情况,做特殊处理  n+1路线为3→4→2→1,n-1路线为3→2→1  所以直接加2
# n = int(input())
# def get_swap_count(n):
#     count = 0
#     while n !=1:
#         # 通过与运算区分奇偶数
#         if n&1 == 0:
#             n >>= 1
#             count += 1
#         else:
#             #判断是否01结尾
#             if n&2 == 0:
#                 n -= 1
#                 count += 1
#             else:
#                 if n == 3:
#                     count += 2
#                     break
#                 else:
#                     n += 1
#                 count += 1
#     return count
# print(get_swap_count(n))


# class node(object):
#     def __init__(self,value = None,left=None,right=None):
#         self.value =value
#         self.left = left
#         self.right =right
#
# def get_tree(str1,str2):
#     # str1后序,str2中序
#     root = node(str1[-1])
#     Index = str2.index(root.value)
#
#     leftstr2 = str2[:Index]
#     maxindex = -1
#     for i in leftstr2:
#         tmpindex = str1.index(i)
#         if maxindex < tmpindex:
#             maxindex = tmpindex
#     if len(leftstr2) == 1:
#         root.left = node(leftstr2)
#     elif len(leftstr2) == 0:
#         root.left = None
#     else:
#         root.left = get_tree(str1[:maxindex+1],leftstr2)
#     rightstr2 = str2[Index+1:]
#     if len(rightstr2) == 1:
#         root.right = node(rightstr2)
#     elif len(rightstr2) == 0:
#         root.right = None
#     else:
#         root.right = get_tree(str1[maxindex+1:-1],rightstr2)
#     return root
#
# def pre(root):
#     if root != None:
#         print(root.value)
#         pre(root.left)
#         pre(root.right)
#
# if __name__ == '__main__':
#     # str2 = input()
#     str2 = "DBHEAGCF"
#     # str1 = input()
#     str1 = "DHEBGFCA"
#     root = get_tree(str1,str2)
#     pre(root)
#   Start_to_lear$n_so#mething
#   n_so Start_to_lear mething
# import time
# def func(f):
#     def wrap():
#         time1 = time.time()
#         f()
#         time2 = time.time()
#         print("执行时间",time2-time1)
#     return wrap
# @func
# def func2():
#     time.sleep(1)
#     print(12345)
# func2()

dict = {"a":1,"b":2,"c":3}
arr = sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(arr)