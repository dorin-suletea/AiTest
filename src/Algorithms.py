class Algorithms:
    
    def euclidianDistance(self,critic1,critic2):
        # Get the list of shared_items
        # if they have no ratings in common, return 0
        sum_of_squares=0
        commonList = critic1.getSameNameItems(critic2)
        critic1Items = commonList[0]
        critic2Items = commonList[1]
        if len(critic1Items) == 0: return 0
        
        # Add up the squares of all the differences
        for i in range(0, len(critic1Items)):
            score1 = critic1Items[i].grade
            score2 = critic2Items[i].grade
            sum_of_squares += pow(score1-score2,2)
        
        return 1/(1+sum_of_squares)