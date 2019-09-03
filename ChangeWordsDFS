def oneCharDiff(a, b):

    aList = list(a)
    bList = list(b)

    count = 0
    
    for i in range(len(aList)):
        if aList[i] != bList[i]:
            count += 1
            if count > 2:
                return False
    if count == 1:
        return True
    else:
        return False

minCount = 0

def DFS(begin, target, words, index):
    global minCount
    
    if len(words) == 0:
        return
    
    if words.count(target) == 0:
        return
    
    candidates = []
    hitCount = 0
    
    for i in words:
        if oneCharDiff(begin, i):
            candidates.append(i)
            hitCount += 1
    
    if hitCount > 0:
        index += 1
        
        if candidates.count(target) > 0:
            if minCount == 0:
                minCount = index
            elif minCount > index:
                minCount = index

                return
        
        for i in candidates:
            updatedWords = words.copy()
            updatedWords.remove(i)
            DFS(i, target, updatedWords, index)
    else:
        return

    
def solution(begin, target, words):
    global minCount
    
    DFS(begin, target, words, 0)

    return minCount
