'''
Given a linked list, determine if it has a cycle in it.
'''

#Author : Shweta Hegde

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        nodeListDict = {}
        
        if head == None :
            return False
        while ( head.next != None ) :
            
            if ( nodeListDict.has_key(head) ):
                
                return True
            else :
                nodeListDict[head] = 1
                head = head.next
        
        
        return False