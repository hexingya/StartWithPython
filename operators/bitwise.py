# Bitwise Operators (32-bits)
#
# &     AND  -- both bits are 1 then choose 1
# |     OR  -- choose 1 if one of bits is one
# ^     XOR -- choose 1 if one is 1 and another is 0 and vice versa
# ~     NOT -- flips 0 into 1 and vice versa
# <<    Left Shift with zero fill
# >>    Signed Right Shift

# 5 --  000...00101
# 7 --  000...00111
# 13 -- 000...01101

# print(5 & 7)  # 000..000101 ~ 5
# print(5 | 7)  # 000..000111 ~ 7
# print(5 ^ 7)  # 000..000010 ~ 2

# ~5
#  000...0000101  --- 5
#  111...1111010  --- ~5

# ---------------
# -(2 ** 31) => -2147483648
# Rest => (2147483647-5) => 2147483642
# result = -6
# print(~5)

# left shift
# ----------------
# 0000...00110 << 2      <---  00...0011000
# print(6 << 2)
# print(6 << 3)
# print(6 << 4)
# print(6 << 1)


# right shift
# ----------------
# 0000...00110 >> 2      --->  0000...001
# print(6 >> 2)
# print(6 >> 3)
# print(6 >> 4)
# print(6 >> 1)

# -6 -- 11...1010  (binary 1's -- 2's )

# 11...1010 >> 2      --->  1111...10
print(-6 >> 2)
# print(6 >> 3)
# print(6 >> 4)
# print(6 >> 1)
