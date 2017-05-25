#!/usr/bin/env python
#-*- coding: utf-8 -*-
from pyspark.mllib.recommendation import ALS, MatrixFactorizationModel, Rating
import pyspark
# check exist of sc
try :
    sc
except NameError:
    sc=pyspark.SparkContext('local[*]')
data = sc.textFile("file:///home/jovyan/work/_data/cf_all.data")
# Load and parse the data
ratings = data.map(lambda l: l.split(',')).map(lambda l: Rating(int(l[0]), int(l[1]), float(l[2])))
print(ratings.collect())
#like bellow tyle
# [Rating(user=1, product=101, rating=5.0), 
# Rating(user=1, product=102, rating=3.0), 
# Rating(user=1, product=103, rating=2.5), 
# Rating(user=2, product=101, rating=2.0)]
# Build the recommendation model using Alternating Least Squares
# rank parameter is user-feature matrix and  product-feature matrix size of column 
rank = 10
numIterations = 10
#ALS is Alternating Least Squares Recommender Algorithm
model = ALS.train(ratings, rank, numIterations)
# Evaluate the model on training data
testdata = ratings.map(lambda p: (p[0], p[1]))
predictions = model.predictAll(testdata).map(lambda r: ((r[0], r[1]), r[2]))
ratesAndPreds = ratings.map(lambda r: ((r[0], r[1]), r[2])).join(predictions)
# mean is average / median center value
MSE = ratesAndPreds.map(lambda r: (r[1][0] - r[1][1])**2).mean()
print("Mean Squared Error = " + str(MSE))

# Save and load model
# model.save(sc, "target/tmp/myCollaborativeFilter")
# sameModel = MatrixFactorizationModel.load(sc, "target/tmp/myCollaborativeFilter")

#file:///home/jovyan/work/_data/cf_all.data
# 1,101,5.0
# 1,102,3.0
# 1,103,2.5
# 2,101,2.0
# 2,102,2.5
# 2,103,5.0
# 2,104,2.0
# 3,101,2.5
# 3,104,4.0
# 3,105,4.5
# 3,107,5.0
# 4,101,5.0
# 4,103,3.0
# 4,104,4.5
# 4,106,4.0
# 5,101,4.0
# 5,102,3.0
# 5,103,2.0
# 5,104,4.0
# 5,105,3.5
