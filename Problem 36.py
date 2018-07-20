from utils.utils import is_palindrome

double_base_palindromes = [i for i in range(1, 1000000) if is_palindrome(str(i)) and is_palindrome("{0:b}".format(i))]
print(sum(double_base_palindromes))