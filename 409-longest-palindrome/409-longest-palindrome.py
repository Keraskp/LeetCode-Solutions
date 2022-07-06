class Solution:
    def longestPalindrome(self, s: str) -> int:
        #Get all of the unique characters in the string
        unique_characters = set(s) 
        total_length = 0
		# iterate through all of the unique characters
        for character in unique_characters:
			# get the floor of the total of half of the unique characters and then multiply that by two
			# Ex: There are 7 "c" in s   7 // 2 *2 = 6 
            total_length += s.count(character)//2*2
		# if the palindrome length is less than the total length, add 1 
		# fixes a total length of 1 
		# also gives the middle letter if a letter is available
        if total_length < len(s):
            return total_length +1
        return total_length
        