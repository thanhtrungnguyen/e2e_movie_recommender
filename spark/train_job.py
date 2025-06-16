from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS

spark = SparkSession.builder.appName("ALS_Trainer").getOrCreate()
ratings = spark.read.csv("../data/ratings.csv", header=True, inferSchema=True)

als = ALS(userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")
model = als.fit(ratings)

model.save("/models/als_model")
