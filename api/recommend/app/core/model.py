from pyspark.sql import SparkSession
from app.core.config import settings

# Placeholder for ALSModel loading

def get_recs(user_id: int, n: int = 10):
    # In production, load ALS model from settings.model_path and return recommendations
    # spark = SparkSession.builder.appName("ALSRec").getOrCreate()
    # model = ALSModel.load(settings.model_path)
    # recs = model.recommendForUser(user_id, n)
    # return recs
    return [1, 2, 3, 4, 5][:n]
