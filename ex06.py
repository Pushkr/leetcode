'''
Given  an  arbitrary  ransom  note  string  and  another  string  containing  letters from  all  the  magazines,  write  a  function  that  will  return  true  if  the  ransom   note  can  be  constructed  from  the  magazines ;  otherwise,  it  will  return  false.   

Each  letter  in  the  magazine  string  can  only  be  used  once  in  your  ransom  note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        rList = list(ransomNote.lower().replace(" ",""))
        mList = list(magazine.lower().replace(" ",""))
        rSet = set(rList)
        mSet = set(mList)
        #mList =
        # unique letters are not sufficient
        if len(rSet) > len(mSet) :
            return False
        print(list(map(lambda x : {x : mList.count(x)},mSet)))
        print(list(map(lambda x: {x: rList.count(x)}, rSet)))
        for letter in rSet:
            if rList.count(letter) > mList.count(letter):
                return False
                break

        return True
