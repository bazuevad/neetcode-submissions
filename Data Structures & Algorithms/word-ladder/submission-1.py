class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        d = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j]+"*"+word[j+1:]
                d[pattern].append(word)
        q = deque([beginWord])
        res = 1
        visit = set([beginWord])
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word==endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for w in d[pattern]:
                        if w not in visit:
                            visit.add(w)
                            q.append(w)
            res+=1

        return 0