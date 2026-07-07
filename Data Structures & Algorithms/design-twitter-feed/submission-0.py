from collections import defaultdict, deque
import heapq
class UserInfo:
    def __init__(self):
        self.tweets = deque()
        self.following = set()

class Twitter:

    def __init__(self):
        self.users = defaultdict(UserInfo)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].tweets.append((self.time,tweetId))
        self.time+=1
        # evict old tweets
        while len(self.users[userId].tweets)>10:
            self.users[userId].tweets.popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        q = []
        for followee in self.users[userId].following | {userId}:
            for time,tweet in self.users[followee].tweets:
                heapq.heappush(q,(-time,tweet))
        res = []
        while q and len(res)<10:
            time,tweet = heapq.heappop(q)
            res.append(tweet)    
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].following.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId].following:
            self.users[followerId].following.remove(followeeId)
