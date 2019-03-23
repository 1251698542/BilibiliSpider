# 1.[两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 `nums` 和一个目标值 `target`，请你在该数组中找出和为目标值的那 **两个** 整数，并返回他们的数组下标。(就是说，在数组中找出两个元素，他们的和为target)

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例:**

```
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

最垃圾的算法，复杂度为O(n^2^)

```python
def twoSum(nums,target):
	for index1,num1 in enumerate(nums):
		for index2,num2 in enumerate(nums):
			if (index1 != index2) and (num1 + num2 == target):
				return [index1,index2]

a = [2,5,7,9]
print(func(a,9))  # (0, 2)
```

正确的实现如下

```python
def twoSum(nums, target):
    hashmap = {}
    for index, num in enumerate(nums):
    	# 另一个数字
        another_num = target - num
        # 如果另一个数字在字典中
        if another_num in hashmap:
            return [hashmap[another_num], index]
        # 将数字本身加入到字典中
        hashmap[num] = index
    return None
```

==经验:下回遇到相加减乘除,都可以考虑移项,使用一个列表或集合将他装起来.==



------

# [7. 整数反转](https://leetcode-cn.com/problems/reverse-integer/)

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

**示例 1:**

```
输入: 123
输出: 321
```

 **示例 2:**

```
输入: -123
输出: -321
```

**示例 3:**

```
输入: 120
输出: 21
```

**注意:**

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31^,  2^31^ − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

下面是我写的

```python
class Solution:
    def reverse(self, x: int) -> int:
        if x >0:
            temp = int(str(x)[::-1])
        elif x <0:
            temp = - int(str(x)[1:][::-1])
        else:
            return 0
        if -2**31 <temp < 2**31-1:
            return temp
        else: return 0
```

可以更加美观:

```python
class Solution(object):
    def reverse(self, x):
    	if x < 0:
    		s = '-'
    		x = -x
    	else:
    		s = ''

    	result = s + str(x)[::-1]
    	if int(result) > pow(2, 31) - 1 or int(result) < pow(-2, 31):
    		return 0
    	return int(result)
```



------

# [9. 回文数](https://leetcode-cn.com/problems/palindrome-number/)

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1:**

```
输入: 121
输出: true

```

**示例 2:**

```
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

```

**示例 3:**

```
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

```

**进阶:**

你能不将整数转为字符串来解决这个问题吗？

我的代码:

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
    	x = str(x)
    	x_half_len = len(x) // 2

    	if len(x) % 2 == 0:
    		part1,part2 = x[:x_half_len],x[x_half_len:]
    	else:
    		part1,part2 = x[:x_half_len],x[x_half_len+1:]
    	
    	if part1 == part2[::-1]:
    		return True
    	else:
    		return False

```

使用算法:

```python
class Solution:
	def isPalindrome(self, x):
		temp_x = x 
		k = 0
		while temp_x != 0:
			# 重点,每次都是弹出最后一位数
			# 所以k就是倒序的x
			k = k * 10 + temp_x % 10
			print(k)
			temp_x = temp_x // 10
		if k == x:
			return True
		else:
			return False

```



------

# [13. 罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

```

例如， 罗马数字 2 写做 `II` ，即为两个并列的 1。12 写做 `XII` ，即为 `X` + `II` 。 27 写做  `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，**罗马数字中小的数字在大的数字的右边**。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

**示例 1:**

```
输入: "III"
输出: 3

```

**示例 2:**

```
输入: "IV"
输出: 4

```

**示例 3:**

```
输入: "IX"
输出: 9

```

**示例 4:**

```
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

```

**示例 5:**

```
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

```

代码如下:

```python
class Solution:
    def romanToInt(self, s):
        hashmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
        result = 0        

        for i in range(len(s)):
            # 特殊情况
            if i < len(s)-1 and hashmap[s[i]] < hashmap[s[i+1]]:   
            	# XLII:此时就把X当成-10
                result -= hashmap[s[i]]
            else:
                result += hashmap[s[i]]
        return result

```

我一开始想的是跳过:当遇到XL,当扫描到X时直接输出90,然后跳过L.
==经验:当想要跳过的时候,可以考虑X本身可以变成什么==



------

# [14. 最长公共前缀](https://leetcode-cn.com/problems/longest-common-prefix/)

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""`。

**示例 1:**

```
输入: ["flower","flow","flight"]
输出: "fl"

```

**示例 2:**

```
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

```

**说明:**

所有输入只包含小写字母 `a-z` 。  

代码如下:

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxStr, minStr = max(strs, default=""), min(strs, default="")
        for i in range(len(minStr)):
            if maxStr[i] != minStr[i]:
                return minStr[:i]
        # 如果for里的if都成功,说明最短单词就是共同子串
        return minStr

```

==经验:==

1. ==如果比较数组for循环的两个each,可以考虑是不是只需比较最长和最短的两个.
   如果是在不行,可以取出数组的第一个值,然后使用for循环.==
2. ==那么如何比较最长和最短的两个,先将他们在for外面取出来,然后在for里使用index,这样就可以使用两个索引来取出这两个值了==
3. ==所以说不要总是想着使用for each in alist,而是使用for index in range(len(alist)-1)==

如果使用二分法:

```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs == []:
            minlen = min([len(x) for x in strs])
            if minlen == 0:
            	return ''
            # 使用二分法
            low = 1
            high = minlen
            while low <= high:
                mid = (low + high) // 2
                if self.start_with(strs,mid):
                    low = mid + 1
                else:
                    high = mid - 1
            # 注意这里要使用min(low,high)
            return strs[0][:min(low,high)]
        else:
            return ''

    def start_with(self,strs,str_len):
        word = strs[0][:str_len]
        for each in strs:
            if not each.startswith(word):
                return False
        return True

```



------

# [20. 有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

给定一个只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

注意空字符串可被认为是有效字符串。

**示例 1:**

```
输入: "()"
输出: true

```

**示例 2:**

```
输入: "()[]{}"
输出: true

```

**示例 3:**

```
输入: "(]"
输出: false

```

**示例 4:**

```
输入: "([)]"
输出: false

```

**示例 5:**

```
输入: "{[]}"
输出: true

```

使用栈,代码如下:

```python
class Solution:
    def isValid(self,s):
        hashmap = {')':'(',']':'[','}':'{'}
        stack = []
        # 特殊情况
        if s == '':
        	return True
        elif not s[0] in ['(','[','{']:
        	return False

        for each in s:
            # 遇到左括号就将他们压入栈
        	if each in ['(','[','{']:
        		stack.append(each)
        	# 当遇到右括号
        	else:
        		if stack and stack[-1] == hashmap[each]:
        			stack.pop()
        		else:
        			return False
        # 最后当stack为空,说明全部配对成功
        if not stack:
        	return True
        else:
        	return False

```

还有一种思路:

```python
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

```



------

# [21. 合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

**示例：**

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

```

代码:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

```

我的代码如下:

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newnode = ListNode(None)
        # 注意这里,否则最后只会返回最后一个节点
        result = newnode

        while l1 or l2:
            # 当l1和l2都存在
            if l1 and l2:
            	# 当l2的值比较小
                if l1.val >= l2.val:
                	# 注意需要使用ListNode类来新建一个节点
                    newnode.next = ListNode(l2.val)
                    newnode = newnode.next
                    l2 = l2.next
                # 当l1的值比较小
                else:
                    newnode.next = ListNode(l1.val)
                    newnode = newnode.next
                    l1 = l1.next
            # 当l1存在而l2不存在
            elif l1 and (not l2):
                newnode.next = ListNode(l1.val)
                newnode = newnode.next
                l1 = l1.next
            # 当l2存在而l1不存在
            elif l2 and (not l1):
                newnode.next = ListNode(l2.val)
                newnode = newnode.next
                l2 = l2.next
        # 因为刚刚创建newnode的时候,传入了None作为头节点,需要使用next去除
        return result.next

```

==经验:==

1. ==注意13-15行,使用next连接的逻辑:赋值的右边必须新建一个节点==
2. ==必须使用result = newnode来建立一个副本,不然最后return newnode只会返回最后一个节点==
3. ==我们可以在新建ListNode的时候传入一个None作为头节点,最后使用next去除这个头节点==



上面的代码很垃圾,问题出在当其中一个链表不存在的时候,==不需要一个节点一个节点的移动,直接把剩下的链表连接上去就行==

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        newnode = ListNode(None)
        result = newnode
        # 当两者都存在
        while l1 and l2:
            if l1.val >= l2.val:
                    newnode.next = ListNode(l2.val)
                    newnode = newnode.next
                    l2 = l2.next
            else:
                newnode.next = ListNode(l1.val)
                newnode = newnode.next
                l1 = l1.next
        # 当其中一个链表不存在,直接将另一个链表连接上去
        if l1 and (not l2):
            newnode.next = l1
        elif l2 and (not l1):
            newnode.next = l2
            
        return result.next

```

我们根据上面两个代码,总结如下:

```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # 使用链表最经常的操作,连续两次赋值
        dummy = pre = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        # 使用惰性赋值
        pre.next = l1 or l2
        return dummy.next

```

==注意上面代码的第4行和第14行,是链表最为经常的操作.==



------

# [26. 删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)

给定一个排序数组，你需要在**原地**删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在**原地修改输入数组**并在使用 O(1) 额外空间的条件下完成。

**示例 1:**

```
给定数组 nums = [1,1,2], 
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。 
你不需要考虑数组中超出新长度后面的元素。

```

**示例 2:**

```
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

```

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以**“引用”**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

```

我的代码:

```python
class Solution:
    def removeDuplicates(self, nums):
        if nums == []:return 0

        cur = nums[-1]
        # 注意这里的range里的参数,其实就是倒序迭代数组(从倒数第二元素开始)
        for index in range(len(nums)-2,-1,-1):
            # 如果前面的元素和当前元素一样,删除它
            if cur == nums[index]:
                nums.pop(index)
            # 否则将当期元素设置为它
            else:
                cur = nums[index]

        return len(nums)

```

理解第7行的代码,看下面:

```python
x = [1,2,3,'?','?','?']
# 列表遍历删除元素必须倒序
for each in x[::-1]:
    if each == '?':
        x.remove('?')

print(x)  # [1, 2, 3]

```

那个,如果不使用for each in alist,而是使用for index in range呢,该如何倒序:

```python
x = [1,2,3,'?','?','?']
for index in range(len(x)-1,-1,-1):
    if x[index] == '?':
        x.remove('?')

print(x) # [1, 2, 3]

```

经验:

1. ==range使用倒序的话,第一参数和第二参数需要互换位置==
2. 原先range的使用规则是for index in range(0,len(alist))
   因为range是上限不在内,即第一参数包含而第二参数不包含.所以第二参数len(alist)移到第一参数位置需要减一,第一参数0移到第二位置也需要减一.
   (所以前面代码中的for index in range(len(nums)-2,-1,-1)就表示从倒数第二元素开始遍历到最前面)

使用for index in range(len(nums)-2,-1,-1)固然可以,可是这时候使用while会更好:

```python
def func1(alist):
    i = 0
    while i < len(alist):
        print(alist[i])
        i += 1

func1([1,2,3,4])   # [1,2,3,4]

```

```python
def func2(alist):    
    i = len(x) - 1
    while i >= 0:
        print(alist[i])
        i -= 1
        
func2([1,2,3,4])    # [4,3,2,1]

```

所以代码如下:

```python
class Solution:
    def removeDuplicates(self, nums):
        if nums == []:return 0

        cur = nums[-1]
        index = len(nums) - 2

        while index >= 0:
            if cur == nums[index]:
                nums.pop(index)
            else:
                cur = nums[index]
            index -= 1

        return len(nums)

```

经验:
==对于数组的循环,while会比for循环慢一点,但是内存消耗会小很多==



------

# [27. 移除元素](https://leetcode-cn.com/problems/remove-element/)

给定一个数组 *nums* 和一个值 *val*，你需要**原地**移除所有数值等于 *val* 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在**原地修改输入数组**并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

**示例 1:**

```
给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。

```

**示例 2:**

```
给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。

```

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以**“引用”**方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

```

这道题很简单了,使用while循环:

```python
class Solution:
    def removeElement(self,nums,val):
        index = len(nums) - 1

        while index >= 0:
            if nums[index] == val:
                nums.remove(val)
            index -= 1

        return len(nums)

```



------

# [28. 实现strStr()](https://leetcode-cn.com/problems/implement-strstr/)

实现 [strStr()](https://baike.baidu.com/item/strstr/811469) 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  **-1**。

**示例 1:**

```
输入: haystack = "hello", needle = "ll"
输出: 2

```

**示例 2:**

```
输入: haystack = "aaaaa", needle = "bba"
输出: -1

```

**说明:**

当 `needle` 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 `needle` 是空字符串时我们应当返回 0 。这与C语言的 [strstr()](https://baike.baidu.com/item/strstr/811469) 以及 Java的 [indexOf()](https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)) 定义,以及python中的find()相符。

```python
class Solution:
    def strStr(self, haystack, needle) -> int:
        return haystack.find(needle)

```

自己模拟find函数,代码如下:

```python
class Solution:
    def strStr(self,haystack,needle):
        needle_len = len(needle)
        haystack_len = len(haystack)
        # 特殊情况
        if needle_len == 0:
            return 0
        elif haystack_len == 0:
            return -1

        index = 0
        while index <= haystack_len - needle_len:
            if haystack[index:index + needle_len] == needle:
                return index
            index += 1

        return -1

```



------

# [35. 搜索插入位置](https://leetcode-cn.com/problems/search-insert-position/)

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

**示例 1:**

```
输入: [1,3,5,6], 5
输出: 2

```

**示例 2:**

```
输入: [1,3,5,6], 2
输出: 1

```

**示例 3:**

```
输入: [1,3,5,6], 7
输出: 4

```

**示例 4:**

```
输入: [1,3,5,6], 0
输出: 0

```

明显该使用二分法,代码如下:

```python
class Solution:
    def searchInsert(self, nums, target) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid -1
            elif target > nums[mid]:
                low = mid + 1
            elif target == nums[mid]:
                return mid

        # 注意最后的return
        # 不是return min(low,high)
        if low > mid:
            return low
        else:
            return high + 1

```

二分法经验:

1. ==注意第3,4,6行,low=0,high=len(alist)-1,while的判断条件是while low<=high==
2. ==注意最后mid的取值,需要使用if...else语句,而不是直接return min(low,high)==

其实还有一种二分写法:

```python
class Solution:
    def searchInsert(self, nums, target) -> int:
            low = 0
            high = len(nums)
            while low < high:
                mid = low + (high - low)//2
                if nums[mid] > target:
                    high = mid
                elif nums[mid] < target:
                    low = mid +1
                else:
                    return mid
            return low

```

递归的二分法:

```python
class Solution(object):
    def searchInsert(self, nums, target):
        #  基线条件
        if len(nums) == 0:
            return 0
        
        left = 0
        right = len(nums)
        mid = (left + right) // 2

        if mid == left:
            if nums[mid] < target:
                return 1
            else:
                return 0
        
        if nums[mid] <= target:
            return mid + self.searchInsert(nums[mid:],target)
        else:
            return self.searchInsert(nums[:mid],target)

```



------

# [38. 报数](https://leetcode-cn.com/problems/count-and-say/)

报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

```
1.     1
2.     11
3.     21
4.     1211
5.     111221

```

`1` 被读作  `"one 1"`  (`"一个一"`) , 即 `11`。
`11` 被读作 `"two 1s"` (`"两个一"`）, 即 `21`。
`21` 被读作 `"one 2"`,  "`one 1"` （`"一个二"` ,  `"一个一"`) , 即 `1211`。

给定一个正整数 *n*（1 ≤ *n* ≤ 30），输出报数序列的第 *n* 项。

注意：整数顺序将表示为一个字符串。

**示例 1:**

```
输入: 1
输出: "1"
```

**示例 2:**

```
输入: 4
输出: "1211"
```

说人话:
题目的意思是**对序列前一个数进行报数**，
数列第一项不是1吗，那第二项就报第一项的有1个1，输出11，
然后第三项就在第二项的基础上报数，第二项是11，第三项不就是2个1么，然后输出21。

> 第一项是一个 1
> 第二项是对第一项的描述：第二项报数：第一项是一个一 ：11
> 第三项报数：第二项是两个一： 21
> 第四项报数：第三项是一个二，一个一：1211
> 第五项报数：第四项是一个一，一个二，两个一：111221

