# palindrome number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        reverse_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reverse_num = reverse_num * 10 + digit
            temp //= 10
        
        return reverse_num == x
    

# roman to integer
class different_solution:
    def romanToInt(self, s):
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        ans = 0
        
        for i in range(len(s)):
            if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]
        
        return ans



# Valid parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftSymbols = []
        for c in s:
            if c in ['(', '{', '[']:
                leftSymbols.append(c)
            elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
                leftSymbols.pop()
            elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
                leftSymbols.pop()
            elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
                leftSymbols.pop()
            else:
                return False
        return leftSymbols == []

# merging two linked lists

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

# remove duplicates from sorted array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique] = nums[i]
                unique += 1
        return unique


# remove element from array of integers

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index

#can place flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0)\
            and (i == len(flowerbed)-1 or flowerbed[i+1] ==0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False


# climbing stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: 
            return 0
        if n == 1: 
            return 1
        if n == 2: 
            return 2
        climb = [0]*(n+1)
        climb[1] = 1
        climb[2] = 2
        for i in range(3, n+1):
            climb[i] = climb[i-1] + climb[i-2]
        print(climb)
        return climb[n]


# majority element

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        majority = 0

        for i in range(len(nums)):
            if count == 0 and majority != nums[i]:
                majority = nums[i]
                count += 1
            elif majority == nums[i]:
                count += 1
            else:
                count -=1
        return majority 
        


# find the index of the first occurrence in a string