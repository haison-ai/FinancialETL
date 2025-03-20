#api test
import requests
from pyspark.sql import SparkSession
from io import StringIO
import pandas as pd

spark = SparkSession.builder.appName("Firts attemps").getOrCreate()



def response_api(key, file_path="data.csv"):
    url = f"https://www.alphavantage.co/query?function=HISTORICAL_OPTIONS&symbol=IBM&date=2021-11-15&apikey={key}&datatype=csv"
    r = requests.get(url)

    print(f"Status Code: {r.status_code}")
    print(f"Response Text: {r.text[:500]}")

    df_pandas = pd.read_csv(StringIO(r.text))

    df_spark = spark.createDataFrame(df_pandas)

    return df_spark


if __name__ == "__main__":
    df_spark = response_api("LXQ6FK4GTHDDC9QT")
    df_spark.show(10)









