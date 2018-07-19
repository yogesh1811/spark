from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

#df = spark.read.csv("C:\\Users\\s770322\\Desktop\\yourPathToCsv.csv", header=True)
df = spark.read.csv("C:\\Yogi\\Notes\\learing\\spark\\olympix_data.csv", header=True)
print(df.count())
