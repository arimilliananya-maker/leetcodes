class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)

        prefix = list(word[:i+1])
        prefix.reverse()

        return ''.join(prefix) + word[i+1:]