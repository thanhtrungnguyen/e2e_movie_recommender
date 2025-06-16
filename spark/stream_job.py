from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType

spark = SparkSession.builder.appName("KafkaToPostgres").getOrCreate()

schema = StructType([
    StructField("userId", IntegerType()),
    StructField("movieId", IntegerType()),
    StructField("action", StringType()),
    StructField("ts", TimestampType())
])

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "user-events") \
    .load()

json_df = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

json_df.writeStream \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://postgres:5432/movies") \
    .option("dbtable", "raw_events") \
    .option("user", "user") \
    .option("password", "pass") \
    .option("checkpointLocation", "/tmp/checkpoints/raw_events") \
    .start() \
    .awaitTermination()
