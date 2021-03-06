#!/usr/bin/env python -W ignore::DeprecationWarning

import pickle
import matplotlib.pyplot as plt
from sklearn.externals import joblib
import codecs
from collections import defaultdict
import csv
import sys
import csv
import codecs
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.metrics import accuracy_score
import pickle
from sklearn.externals import joblib
from sklearn.datasets import load_files
import math
from sklearn import datasets, linear_model
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

csv.field_size_limit(500000)
director_fb_likes = []
num_critic_for_reviews = []
actor3_fb_likes = []
actor1_fb_likes = []
gross = []
fb_likes = []
duration = []
num_voted_users = []
num_user_for_reviews = []
language  = []
country = []
content_rating  = []
budget  = []
year = []
actor2_fb_likes  = []
imdb_score = []
total_facebook_likes = []
#Movie Genres
genres = []
action = [0 for x in range(5043)]
adventure = [0 for x in range(5043)]
fantasy = [0 for x in range(5043)]
scifi = [0 for x in range(5043)]
thriller = [0 for x in range(5043)]
comedy = [0 for x in range(5043)]
family = [0 for x in range(5043)]
horror = [0 for x in range(5043)]
war = [0 for x in range(5043)]
animation = [0 for x in range(5043)]
western = [0 for x in range(5043)]
romance = [0 for x in range(5043)]
musical = [0 for x in range(5043)]
documentary = [0 for x in range(5043)]
drama = [0 for x in range(5043)]
history = [0 for x in range(5043)]
biography = [0 for x in range(5043)]
mystery = [0 for x in range(5043)]
crime = [0 for x in range(5043)]
#content ratings
g = [0 for x in range(5043)]
pg = [0 for x in range(5043)]
pg_13 = [0 for x in range(5043)]
r = [0 for x in range(5043)]
nc_17 = [0 for x in range(5043)]
with open("movie_metadata.csv", "r") as sentences_file:
    reader = csv.reader(sentences_file, delimiter=',')
    reader.next()
    i = 0
    for row in reader:
        content_rating = ""
        content_rating = str(row[21])
        if 'G' in content_rating:
            g[i] = 1
        if 'PG' in content_rating:
            pg[i] = 1
        if 'PG-13' in content_rating:
            pg_13[i] = 1
        if 'R' in content_rating:
            r[i] = 1
        if 'NC-17' in content_rating:
            nc_17[i] = 1
        i+=1

with open("movie_metadata.csv", "r") as sentences_file:
    reader = csv.reader(sentences_file, delimiter=',')
    reader.next()
    i = 0
    for row in reader:
        genre = ""
        genre = str(row[9])
        if 'Action' in genre:
            action[i] = 1
        if 'Adventure' in genre:
            adventure[i] = 1
        if 'Fantasy' in genre:
            fantasy[i] = 1
        if 'Sci-Fi' in genre:
            scifi[i] = 1
        if 'Thriller' in genre:
            thriller[i] = 1
        if 'Comedy' in genre:
            comedy[i] = 1
        if 'Family' in genre:
            family[i] = 1
        if 'Horror' in genre:
            horror[i] = 1
        if 'War' in genre:
            war[i] = 1
        if 'Animation' in genre:
            animation[i] = 1
        if 'Western' in genre:
            western[i] = 1
        if 'Romance' in genre:
            romance[i] = 1
        if 'Musical' in genre:
            musical[i] = 1
        if 'Documentary' in genre:
            documentary[i] = 1
        if 'Drama' in genre:
            drama[i] = 1
        if 'History' in genre:
            history[i] = 1
        if 'Biography' in genre:
            biography[i] = 1
        if 'Mystery' in genre:
            mystery[i] = 1
        if 'Crime' in genre:
            crime[i] = 1
        i+=1
        
with open("movie_metadata.csv", "r") as sentences_file:
    reader = csv.reader(sentences_file, delimiter=',')
    reader.next()
    i = 1
    for row in reader:
        director_fb_likes.append(float(row[4]))
        num_critic_for_reviews.append(float(row[2]))
        actor1_fb_likes.append(float(row[7]))
        actor3_fb_likes.append(float(row[5]))
        fb_likes.append(float(row[13]))
        duration.append(float(row[3]))
        if int(row[8])>0:
            gross.append(int(math.log(float(row[8]))/math.log(10.0)))
        else:
            gross.append(0)
        num_voted_users.append(float(row[12]))
        num_user_for_reviews.append(float(row[18]))
        if row[19] == 'English':
            language.append(1.0)
        else:
            language.append(0.0)
        if row[20] == 'USA':
            country.append(1.0)
        else:
            country.append(0.0)
        budget.append(float(row[22]))
        actor2_fb_likes.append(float(row[24]))
        imdb_score.append(float(row[25]))
        total_facebook_likes.append(float(row[27]))
# print(len(total_facebook_likes))
for i in range(0,5043):
    director_fb_likes[i]/=max(director_fb_likes)
    num_critic_for_reviews[i]/=max(num_critic_for_reviews)
    actor1_fb_likes[i]/=max(actor1_fb_likes)
    actor2_fb_likes[i]/=max(actor2_fb_likes)
    actor3_fb_likes[i]/=max(actor3_fb_likes)
    fb_likes[i]/=max(fb_likes)
    duration[i]/=max(duration)
    num_voted_users[i]/=max(num_voted_users)
    num_user_for_reviews[i]/=max(num_user_for_reviews)
    budget[i]/=max(budget)
    imdb_score[i]/=max(imdb_score)
    total_facebook_likes[i]/=max(total_facebook_likes)
num_row = 5043
num_col = 35
totalMatrix = [[0 for x in range(num_col)] for y in range(num_row)]
for i in range(0,5043):
    for j in range(0,35):
        if j==0:
            totalMatrix[i][j] = director_fb_likes[i]
        elif j==1:
            totalMatrix[i][j] = num_critic_for_reviews[i]
        elif j==2:
            totalMatrix[i][j] = actor1_fb_likes[i]
        elif j==3:
            totalMatrix[i][j] = actor2_fb_likes[i]
        elif j==4:
            totalMatrix[i][j] = actor3_fb_likes[i]
        elif j==5:
            totalMatrix[i][j] = fb_likes[i]
        elif j==6:
            totalMatrix[i][j] = duration[i]
        elif j==7:
            totalMatrix[i][j] = num_voted_users[i]
        elif j==8:
            totalMatrix[i][j] = num_user_for_reviews[i]
        elif j==9:
            totalMatrix[i][j] = budget[i]
        elif j==10:
            totalMatrix[i][j] = imdb_score[i]
        elif j==11:
            totalMatrix[i][j] = total_facebook_likes[i]
        elif j==12:
            totalMatrix[i][j] = action[i]
        elif j==13:
            totalMatrix[i][j] = adventure[i]
        elif j==14:
            totalMatrix[i][j] = fantasy[i]
        elif j==15:
            totalMatrix[i][j] = scifi[i]
        elif j==16:
            totalMatrix[i][j] = thriller[i]
        elif j==17:
            totalMatrix[i][j] = comedy[i]
        elif j==18:
            totalMatrix[i][j] = family[i]
        elif j==19:
            totalMatrix[i][j] = horror[i]
        elif j==20:
            totalMatrix[i][j] = war[i]
        elif j==21:
            totalMatrix[i][j] = animation[i]
        elif j==22:
            totalMatrix[i][j] = western[i]
        elif j==23:
            totalMatrix[i][j] = romance[i]
        elif j==24:
            totalMatrix[i][j] = musical[i]
        elif j==25:
            totalMatrix[i][j] = documentary[i]
        elif j==26:
            totalMatrix[i][j] = drama[i]
        elif j==27:
            totalMatrix[i][j] = history[i]
        elif j==28:
            totalMatrix[i][j] = biography[i]
        elif j==29:
            totalMatrix[i][j] = mystery[i]
        elif j==30:
            totalMatrix[i][j] = crime[i]
        elif j==31:
            totalMatrix[i][j] = g[i]
        elif j==32:
            totalMatrix[i][j] = pg[i]
        elif j==33:
            totalMatrix[i][j] = pg_13[i]
        elif j==34:
            totalMatrix[i][j] = r[i]
        elif j==35:
            totalMatrix[i][j] = nc_17[i]
trainMatrix = totalMatrix[:4539]
testMatrix = totalMatrix[4539:]
trainLabel = gross[:4539]
testLabel = gross[4539:]

svm_model = svm.SVC(kernel='rbf', C=2, gamma = 2)
scores2 = cross_val_score(svm_model, totalMatrix, gross, cv=5)
print("SVM_rbf")
print(scores2)
acc1 = scores2.mean()
print("Accuracy: %0.2f (+/- %0.2f)" % (scores2.mean(), scores2.std() * 2))

svm_model2 = svm.SVC(kernel='linear', C=2, gamma = 2)
scores3 = cross_val_score(svm_model2, totalMatrix, gross, cv=5)
print("SVM linear")
print(scores3)
acc2 = scores3.mean()
print("Accuracy: %0.2f (+/- %0.2f)" % (scores3.mean(), scores3.std() * 2))

svm_model3 = svm.SVC(kernel='poly', C=1, gamma = 2)
scores4 = cross_val_score(svm_model3, totalMatrix, gross, cv=5)
print("SVM poly")
print(scores4)
acc3 = scores4.mean()
print("Accuracy: %0.2f (+/- %0.2f)" % (scores4.mean(), scores4.std() * 2))

clf = GaussianNB()
scores5 = cross_val_score(clf, totalMatrix, gross, cv=5)
print("Naive Bayes")
print(scores5)
acc4 = scores5.mean()
print("Accuracy: %0.2f (+/- %0.2f)" % (scores5.mean(), scores5.std() * 2))

print("MultiLayer Perceptron")
#print("- Without cross validation")
mlp_model = MLPClassifier(hidden_layer_sizes=(20, ), activation='relu',  max_iter=200)
scores13 = cross_val_score(mlp_model, totalMatrix, gross, cv=5)
print(scores13)
acc5 = scores13.mean()
print("Accuracy: %0.2f (+/- %0.2f)" % (scores13.mean(), scores13.std() * 2))

print("Logistic Regression")
logreg_model = LogisticRegression(C=1e5)
scores = cross_val_score(logreg_model, totalMatrix, gross, cv=5)
print(scores)
acc6 = scores.mean()
print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

logreg_model.fit(trainMatrix,trainLabel)
predicted = logreg_model.predict(testMatrix)
count = 0
for i in range(len(predicted)):
    if (predicted[i]-testLabel[i])==0:
        count += 1
#print("Correctly predicted : "+str(count))
percent = float(count)/float(len(predicted))
#print("Percentage of correctly predicted :"+ str(percent * 100) + '%')
acc12 = percent
#print('\n\n\n')
print("Logistic Regression:" + str(acc12*100) + '%')

percentlist = []
for i in range(5):
    x_train, x_test, y_train, y_test = train_test_split(totalMatrix, gross, test_size=0.3)
    mlp_model.fit(x_train,y_train)
    predicted2 = mlp_model.predict(x_test)
    count2 = 0
    for i in range(len(predicted2)):
        if (predicted2[i]-y_test[i])==0 or abs(predicted2[i]-y_test[i])==1:
            count2 += 1
    #print("Correctly predicted : "+str(count2))
    percent1 = float(count2)/float(len(predicted2))
    percentlist.append(percent1)

acc11 = float(sum(percentlist)) / float(len(percentlist))
print("MultiLayerPerceptron:" + str(acc11*100) + '%')


dual = [acc11,acc12]
numbers2 = [1,2]
names2 = ['MultiLayerPerceptron','LogisticRegression']

numbers = [1,2,3,4,5,6]
names = ['SVM-RBF','SVM-LINEAR','SVM-POLY','NB','MLP','LogisticRegression']

accuracy = [acc1, acc2, acc3, acc4, acc5, acc6]
#accuracy = accuracylist['value']
#print(accuracy)
ax = plt
plt.bar(numbers, accuracy , align = 'center' )
#plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xticks(numbers,names)
plt.show()  

ax.bar(numbers2, dual , align = 'center' )
ax.xticks(numbers2,names2)
ax.show()  



