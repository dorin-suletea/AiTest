'''
Created on Jun 30, 2016

@author: dorinsuletea
'''
import matplotlib.pyplot as plt
import numpy as np
import math
from _dbus_bindings import Boolean
from src.Pojo import ItemGradePair
from src.Pojo import Critic
from src.Pojo import Util
from src.Algorithms import Algorithms

critics={
'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
'The Night Listener': 4.5, 'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0},
'Gigel': {'Lady in the Water': 1, 'Snakes on a Plane': 2,'Just My Luck': 1.5, 'Superman Returns': 2, 'You, Me and Dupree': 1,'The Night Listener': 1.5},

}


def pearsonDistance(prefs,p1,p2):
    # Get the list of mutually rated items
    si={}
    
    for item in prefs[p1]:
        if item in prefs[p2]: 
            si[item]=1
            # Find the number of elements
            n = len(si)
            # if they are no ratings in common, return 0
    
    if n==0: return 0
            
    # Add up all the preferences
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    # Sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
    
    # Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    # Calculate Pearson score
    num=pSum-(sum1*sum2/n)
    den=math.sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r

def showPearsonMatch(critics,matchedPerson):
    similarityList = []
    for person in critics:
        match = pearsonDistance(critics, matchedPerson, person)
        similarityList.append([match,person])
    return similarityList

# euclidean :
#     lowest Gene Seymour, 
#     highest Michael Phillips
#     gigel: [0.06896551724137931, 'Gigel']

#pearson 
#     accounts for grade inflation, matches lines by shape , not by atual xy
#     highest = Toby
#     lowest = Michael Phillips
#     gigel: [1, 'Gigel']
#
if __name__ == '__main__':
    # Get items to compare
    criticList = Util.parseIntoPojos(critics)
    critic1 = Util.getCriticByname('Lisa Rose', criticList)
    critic2 = Util.getCriticByname('Gigel', criticList)
    
    # Plot the preferences
    plot = Util.plotItems(critic1.itemGrades, 'y')
    plot = Util.plotItems(critic2.itemGrades, 'g')
    plot.show()
    
    # Show similarities
    algo = Algorithms()
    similarity = algo.euclidianDistance(critic1, critic2)
    print(similarity)

    pass