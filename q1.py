class WordBreaker:
    def __init__(self, dictionary):
        self.word_set = set(dictionary)

    def can_break(self, s):
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in self.word_set:
                    dp[i] = True
                    break
        return dp[n]

    def get_all_segmentations(self, s):
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [[]]
            if start in memo:
                return memo[start]

            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in self.word_set:
                    for sublist in backtrack(end):
                        result.append([word] + sublist)

            memo[start] = result
            return result

        return [" ".join(words) for words in backtrack(0)]


def run_tests():
    test_cases = [
        {
            "s": "leetcode",
            "wordDict": ["leet", "code"],
            "expected": True
        },
        {
            "s": "applepenapple",
            "wordDict": ["apple", "pen"],
            "expected": True
        },
        {
            "s": "catsandog",
            "wordDict": ["cats", "dog", "sand", "and", "cat"],
            "expected": False
        },
        {
            "s": "pineapplepenapple",
            "wordDict": ["apple", "pen", "applepen", "pine", "pineapple"],
            "expected": True
        }
    ]

    for i, test in enumerate(test_cases, 1):
        wb = WordBreaker(test["wordDict"])
        result = wb.can_break(test["s"])
        print(f"Test case {i}: {'Passed' if result == test['expected'] else 'Failed'}")

        if result:
            segmentations = wb.get_all_segmentations(test["s"])
            print("  Possible segmentations:")
            for seg in segmentations:
                print("   -", seg)
        print()


if __name__ == "__main__":
    run_tests()
