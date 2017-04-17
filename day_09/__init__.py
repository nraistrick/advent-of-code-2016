# -*- coding: utf-8 -*-

"""
==================================
Pseudo-Code Notes for V2 Recursive
Decompression-Algorithm
==================================

Input:
  str = “X(8x2)(3x3)ABCY”
  len = 15

Result:
  str = "XABCABCABCABCABCABCY"
  len = 20

--------------------------------------------------------
GET_DECOMPRESSED_STRING_LENGTH_CHANGE(“X(8x2)(3x3)ABCY”)
--------------------------------------------------------
length = len(input)                                                      # length = 15
size_change = 0
for match in matches:
    repeated_characters, repetitions = “(3x3)ABC”, 2
    substring = repeated_characters * repetitions = “(3x3)ABC(3x3)ABC”   # “(3x3)ABC” * 2 = “(3x3)ABC(3x3)ABC”
    added_characters = len(repeated_characters) * (repetitions - 1)      # added_characters = 8 * (2-1) = 8
    size_change += added_characters - decompression_pattern_length	     # size_change += 8 - 5 = 3

if repeated_characters.count(decompression_string_identifier):           # True -> (3x3)
    size_change += GET_DECOMPRESSED_STRING_LENGTH_CHANGE(substring) >-+  # substring = “(3x3)ABC(3x3)ABC”
    <skip_next_n_matches>                                             |  # n = 1
                                                                      |
return size_change                                                    |
                                                                      |
---------------------------------------------------------             |
GET_DECOMPRESSED_STRING_LENGTH_CHANGE(“(3x3)ABC(3x3)ABC”)  <----------+
---------------------------------------------------------
length = len(input)                                                      # length = 16
size_change = 0
for match in matches:                                                    # Two loops as there are two decompression markers
    repeated_characters,  repetitions = “ABC”,  3						 # “(3x3)ABC(3x3)ABC” * 2 = “ABCABCABCABCABCABC”
    substring = repeated_characters * repetitions = “(3x3)ABC(3x3)ABC”   # “ABC” * 3 = “ABCABCABC”
    added_characters = len(repeated_characters) * (repetitions - 1)	     # added_characters = 3 * (3-1) = 6
    size_change += added_characters - decompression_pattern_length       # size_change += 6 - 5 = 1

    if repeated_characters.count(decompression_string_identifier):       # False -> No further decompression to do
        ...

return size_change
"""
