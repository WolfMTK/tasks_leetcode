class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                new_str += word1[i] + word2[i]
            new_str += word1[len(word2):]
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                new_str += word1[i] + word2[i]
            new_str += word2[len(word1):]
        else:
            for i in zip(word1, word2):
                new_str += i[0] + i[1]
        return new_str


if __name__ == "__main__":
    assert Solution().mergeAlternately(word1="abc", word2="pqr") == "apbqcr"
    assert Solution().mergeAlternately(word1="ab", word2="pqrs") == "apbqrs"
    assert Solution().mergeAlternately(word1="abcd", word2="pq") == "apbqcd"
