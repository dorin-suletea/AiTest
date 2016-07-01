import matplotlib.pyplot as plt

class ItemGradePair:
    # String itemName 
    # Integer grade
    
    def __init__(self, itemName, grade):
        self.itemName = itemName
        self.grade = grade
        
        
class Critic:
    # String criticName 
    # ItemGradePair[] itemGrades 
    
    def __init__(self, criticName, itemGrades):
        self.criticName = criticName
        self.itemGrades = itemGrades
        
    def getSameNameItems(self,otherCritic):
        critic1Items = []
        critic2Items = []
        for item in self.itemGrades:
            for item2 in otherCritic.itemGrades:
                if item.itemName == item2.itemName:
                    critic1Items.append(item)
                    critic2Items.append(item2)
                    
        retList = []
        retList.append(critic1Items)      
        retList.append(critic2Items)      
        return retList
        
 
class Util:       
    @staticmethod        
    def parseIntoPojos(sourceJson):
        criticList = []
        for i in sourceJson:
            criticName = i
            prefferenceList = []
            for movie in sourceJson[i]:
                prefferenceList.append(ItemGradePair(movie,sourceJson[i][movie]))
            criticList.append(Critic(criticName,prefferenceList))
        return criticList
    
    #inputList is ItemGradePair
    @staticmethod
    def plotItems(inputList, color):
        movies = []
        moviesXaxis = []
        grades = []
        i = 0;
        for item in inputList:
            movies.append(item.itemName)
            moviesXaxis.append(i)
            i+=1
            grades.append(item.grade)
            
            
        plt.xticks(moviesXaxis, movies)
        plt.plot(moviesXaxis, grades,color=color)
        return plt  
     
    @staticmethod 
    def getCriticByname(criticName,criticList):
        for i in criticList:
            if i.criticName == criticName :
                return i