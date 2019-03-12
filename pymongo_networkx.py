import networkx as nx
from pymongo import MongoClient
 
client = MongoClient('localhost', 27017)
tweets = client.aid_venezuela.tweets

G = nx.Graph()
for tweet in tweets.find():
	hashtags = tweet['entities']['hashtags']
	if len(hashtags) > 1:
		for i in range(len(hashtags)-1):
                        for j in range(i+1,len(hashtags)):
                                if G.has_edge(hashtags[i]['text'],hashtags[j]['text']):
                                        G[hashtags[i]['text']][hashtags[j]['text']]['weight'] += 1

                                else:			
                                        G.add_edge(hashtags[i]['text'],hashtags[j]['text'], weight=1)


nx.write_gexf(G, "aid_venezuela.gexf")
