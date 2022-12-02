#Import required library
from sklearn import tree

#Load the dataset
#Rough      1
#Smooth     0

#Tennis     1
#Cricket    2

def BallPredictor():
    Feartures = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Lables = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    #Decide the machine learning algorithm
    obj = tree.DecisionTreeClassifier()

    #perform the training model
    obj = obj.fit(Feartures, Lables) #fit method internally perform training

    #perform the testing
    print(obj.predict([[97,0]]))

def main():
    print("-----> Ball Predictor Case Study <-----")

    BallPredictor();

if __name__ == "__main__":
    main()