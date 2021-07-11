import pandas as pd
#url formats
#https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2020-01.csv
#https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2020-01.csv
#https://nyc-tlc.s3.amazonaws.com/trip+data/fhvhv_tripdata_2020-01.csv

##
# in Jupyter and Colab, loading all 3 types of taxis crashes runtime due to big data set
# which is why only yellow cabs are loaded here while green taxis and fhv(for-hire-vehicles) are commented out 

yellow_2020url="https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2020-"
#green_2020url="https://nyc-tlc.s3.amazonaws.com/trip+data/green_tripdata_2020-"
#fhv_2020url="https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_2020-"
months=["01","02","03","04","05","06","07","08","09","10","11","12"]
end=".csv"
df_yellow2020={}
#df_green2020={}
#df_fhv2020={}

for elem in range(len(months)):
  df_yellow2020[elem]=pd.read_csv(yellow_2020url+months[elem]+end)
  #df_green2020[elem]=pd.read_csv(green_2020url+months[elem]+end)
  #df_fhv2020[elem]=pd.read_csv(fhv_2020url+months[elem]+end)