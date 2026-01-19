class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            return str(x) == str(x)[::-1]
        else:
            return False
    
    def isPalindromeHacky(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverse_num = 0
        while x > reverse_num:
            reverse_num = (reverse_num * 10) + (x % 10)
            x = x // 10
        return x == reverse_num or x == reverse_num // 10
    
    def isPalindromeMySol(self, x: int) -> bool:
        reverse_num = 0
        given_num = x
        while given_num > 0:
            reverse_num = reverse_num * 10 + given_num % 10
            given_num = given_num // 10
        return x == reverse_num

def main():
    number = -1111
    sol = Solution()
    print(f"Is Palindrome: {sol.isPalindrome(number)}")
    
if __name__ == "__main__":
    main()
    
    
            