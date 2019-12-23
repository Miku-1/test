# # class Node(object):
# #     def __init__(self,value):
# #         self.value = value
# #         self.pnext = None
# #
# # class ChainTale(object):
# #     def __init__(self):
# #         self._head = None
# #     # 头插法
# #     def add(self,value):
# #         node = Node(value)
# #         node.pnext = self._head
# #         self._head = node
# #     # 尾插法
# #     def append(self,value):
# #         cur = self._head
# #         if cur is None:
# #             self.add(value)
# #         else:
# #             node = Node(value)
# #             while cur.pnext:
# #                 cur = cur.pnext
# #             cur.pnext = node
# #     # 链表是否为空
# #     def is_empty(self):
# #         if self._head:
# #             return False
# #         else:
# #             return True
# #     # 链表长度
# #     def length(self):
# #         cur = self._head
# #         count = 0
# #         while cur.pnext:
# #             cur = cur.pnext
# #             count += 1
# #         return count
# #
# #
# #     # 指定位置插入元素
# #     # location为要插入元素的位置(索引从0开始)
# #     def insert(self,location,value):
# #         if location == 0:
# #             self.add(value)
# #         elif location >= self.length:
# #             self.append(value)
# #         else:
# #             cur = self._head
# #             for i in range(location - 1):
# #                 cur = cur.pnext
# #             node = Node(value)
# #             node.pnext = cur.pnext
# #             cur.pnext = node
# #     # 遍历
# #     def show(self):
# #         if self._head is None:
# #             return 'empty list'
# #         else:
# #             cur = self._head
# #             while cur:
# #                 print(cur.value,end = '\t')
# #                 cur = cur.pnext
# #             print()
# #     # 删除节点
# #     def delete(self,location):
# #         if self.is_empty:
# #             return 'null'
# #         elif location == 1:
# #             self._head = self._head.pnext
# #         cur = self._head
# #         for i in range(location - 1):
# #             cur = cur.pnext
# #         cur.pnext =cur.pnext.pnext
# #     def revese_table(self):
# #         # if self.length()< 2:
# #         #     return '数据过少'
# #         # cur = self._head
# #         # pre = None
# #         # while not cur.pnext:
# #         #     # print(i)
# #         #     tmp = cur.pnext.pnext
# #         #     cur.pnext.pnext = pre
# #
# #         #     pre = cur.pnext
# #         #     cur.pnext = tmp
# #         #     # i += 1
# #         # return cur
# #         cur = self._head
# #         pre = None
# #         while cur.pnext:
# #             temp = cur.pnext
# #             cur.pnext = pre
# #             pre = cur
# #             cur =temp
# #         return pre
# #     def reverseList(self):
# #         # write code here
# #         if self._head is None:
# #             return self._head
# #         pHead = self._head
# #         last = None  # 指向上一个节点
# #         while pHead:
# #             # 先用tmp保存pHead的下一个节点的信息，
# #             # 保证单链表不会因为失去pHead节点的next而就此断裂
# #             tmp = pHead.pnext
# #             # 保存完next，就可以让pHead的next指向last了
# #             pHead.pnext = last
# #             # 让last，pHead依次向后移动一个节点，继续下一次的指针反转
# #             last = pHead
# #             pHead = tmp
# #         return last
# #
# #
# #
# #
# # ch = ChainTale()
# # for i in range(5):
# #     ch.add(i)
# #     # ch.append(i)
# # # ch.reverseList()
# # ch.show()
# # ch.revese_table()
# # ch.show()
#
#
# # 线程的交替打印
# # import threading
# # from time import sleep
# #
# # def threading_a():
# #     for i in range(5):
# #         lockb.acquire()
# #         print("{}\n{}".format(i+1,i+2))
# #         locka.release()
# #         # sleep(0.13)
# #
# # def threading_b():
# #     arr = []
# #     for i in range(5):
# #         sleep(3)
# #         locka.acquire()
# #         print(chr(i + ord('A')))
# #
# #         lockb.release()
# #         # sleep(0.3)
# #
# # if __name__ == '__main__':
# #     locka = threading.Lock()
# #     lockb = threading.Lock()
# #
# #     th_a = threading.Thread(target=threading_a)
# #     th_b = threading.Thread(target=threading_b)
# #
# #     locka.acquire()
# #
# #     th_a.start()
# #     th_b.start()
#
# #     th_a.join()
#
# import socket
#
# sever = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sever.bind(('localhost',3000))
# sever.listen(5)
# conn, addr = sever.accept()
# print('客户端已上线')
# print(addr)
# while 1:
#     data = sever.recv(1024)
#     print(data)
#     if data == "close server":
#         sever.close()
#     else:
#         msg = input('>>')
#         conn.send(msg)
#
#
#
#
#
#
#
# #
# def f(string, key):
#     # print(string)
#     ptext = string.upper()
#     mainarray = [None]*key
#     for i in range(key):
#         mainarray[i] = [None]*len(ptext)
#         for s in range(len(ptext)):
#             mainarray[i][s] = ''
#     print(mainarray)
#     j = 0
#     r = 0
#     for i in range(len(ptext)):
#         p = ptext[i]
#         mainarray[j][i] = p
#         if r==0:
#             j=j+1
#         elif r==1:
#             j=j-1
#         if j==key-1:
#             r=1
#         elif j==0:
#             r=0
#
#     for i in range(len(mainarray)):
#         mainarray[i] = ''.join(mainarray[i])
#
#     ctext = ''.join(mainarray)
#     print(ctext)
#     # print(mainarray)
# f('abcdef',4)

def func_f(string,key):
    new_string = string.upper()
    arr = [[""]*len(new_string)]*key
    print(arr)

    j, r = 0, 0
    # print(new_string)
    for i in range(len(new_string)):

        arr[j][i] = new_string[i]
        print(j,i,new_string[i])
        if r == 0:
            j += 1
        elif r == 1:
            j -= 1

        if j == key - 1:
            r = 1
        elif j == 0:
            r = 0
        # print(j,r)
    for i in range(len(arr)):
        arr[i] = "".join(arr[i])
    text = "".join(arr)
    return text
print(func_f('abcd',2))
