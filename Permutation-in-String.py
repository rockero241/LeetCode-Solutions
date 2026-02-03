1from collections import Counter
2
3class Solution:
4    def checkInclusion(self, s1: str, s2: str) -> bool:
5        if len(s1) > len(s2): return False
6        
7        count1 = Counter(s1)
8        window = {}
9        have, need = 0, len(count1)
10        
11        l = 0
12        for r in range(len(s2)):
13            # 1. Add right character to window
14            char = s2[r]
15            window[char] = 1 + window.get(char, 0)
16            
17            # 2. Update 'have' if count matches exactly
18            if char in count1 and window[char] == count1[char]:
19                have += 1
20            
21            # 3. If window is too big, shrink from the left
22            if (r - l + 1) > len(s1):
23                left_char = s2[l]
24                if left_char in count1 and window[left_char] == count1[left_char]:
25                    have -= 1
26                window[left_char] -= 1
27                l += 1
28            
29            # 4. Check if we found a permutation
30            if have == need:
31                return True
32                
33        return False