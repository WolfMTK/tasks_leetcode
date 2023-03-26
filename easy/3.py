class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numeral = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        count = 0
        num = 0
        for rom_num in reversed(s):
            num_dct = roman_numeral.get(rom_num)
            if num <= num_dct:
                count += num_dct
                num = num_dct
            elif num > num_dct:
                count -= num_dct
        return count


if __name__ == "__main__":
    assert Solution().romanToInt(s="III") == 3
    assert Solution().romanToInt(s="LVIII") == 58
    assert Solution().romanToInt(s="MCMXCIV") == 1994
