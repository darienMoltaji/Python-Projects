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