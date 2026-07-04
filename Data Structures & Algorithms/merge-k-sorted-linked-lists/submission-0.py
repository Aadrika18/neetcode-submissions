class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = ListNode(0)
        cur = res

        while True:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
                
            if minNode == -1:
                break
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next
            
        return res.next