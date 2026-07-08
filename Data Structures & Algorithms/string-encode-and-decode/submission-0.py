class Solution:

    def encode(self, strs: List[str]) -> str:

        # Encode the strings together with some delimiter
        # So for each iteration of the string when decoded
        # the code will look for a integer specifying length of the word
        # and a delimiter seperating the integer and the number

        # Hello, World -> 5#Hello5#World

        

        string = ""
        for sr in strs:
            string += str(len(sr)) + "#" + sr
        return string
            
    def decode(self, s: str) -> List[str]:

        # Based on the integer specifying the length of the string
        # and based on the delimiter we can seperate the word and the number

        i = 0 
        strs = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            strs.append(s[j + 1 : j + 1 + length])
        
            i = j + 1 + length
        return strs

        
        