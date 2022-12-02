#Import required library
#pip install scikit-learn
#import sklearn
from sklearn import tree

#Load the dataset
Feartures = [[35,"Rought"],[47,"Rought"],[90,"Smooth"],[48,"Rought"],[90,"Smooth"],[35,"Rought"],[92,"Smooth"],[35,"Rought"],[35,"Rought"],[35,"Rought"],[96,"Smooth"],[43,"Rought"],[110,"Smooth"],[35,"Rought"],[95,"Smooth"]]
Lables = ["Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket","Tennis","Tennis","Tennis","Cricket","Tennis","Cricket","Tennis","Cricket"]

#Decide the machine learning algorithm
obj = tree.DecisionTreeClassifier()

#perform the training model
obj = obj.fit(Feartures, Lables) #fit method internally perform training

#perform the testing
print(obj.predict([[97,"Smooth"]]))