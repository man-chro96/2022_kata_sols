def reverse_bits(n):
   return int(str(bin(n))[::-1][:-2], 2)