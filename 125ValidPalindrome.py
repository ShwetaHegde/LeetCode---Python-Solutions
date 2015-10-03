'''Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome. '''

#Author : Shweta Hegde

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None :
            return False
        if s == "":
            return True
        
        s = s.strip();
        low = 0
        high = len(s) - 1
        while ( low < high ) :
            if s[low].isalpha() or s[low].isdigit():
                if s[high].isalpha() or s[high].isdigit():
                    if not s[low].lower() == s[high].lower():
                        return False
                    low += 1
                    high -= 1
                else:
                    high -= 1;
            else:
                low += 1
        
        return True