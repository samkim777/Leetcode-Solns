class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dict when list empty
       res = defaultdict(list) # mapping character count of each string to list of anagrams
       # key 1n,1a,1t : [nat,tan]
       for s in strs:
           count = [0] * 26 # Create list with 26 elements a...z

           for c in s:
               # r a t -> 17 0 19 -> corresponding keys have integer values
               # Assign keys values 0 -> 25
                                       # Increment by 1
              count[ord(c) - ord('a')] +=1 

           res[tuple(count)].append(s)

       return res.values() 