###############################################################################################
# This is the auxiliary file for the practical assignment to learn python for API´s.          #
# Prepared by the Spatial Information Laboratory - Vrije Universiteit Amsterdam               #
# Simeon Nedkov, Chris Lucas, Maurice de Kleijn, Devi Brands                                  #
###############################################################################################

# In this practical assignment we want you to create a shapefile containing the average level of particulate matter for
# 2.5 μm and 10 μm or less per m3 for all stations in 2017. 
# For this practical assignment you need to use a couple of modules. Most of them have already appeared in the exercises.
# A couple of them are new and will be introduced when you need to use them.

import requests
import datetime
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point


# STEP 1: As first step we want you to start a pandas DataFrame
# REMOVE THE HASHTAG IN THE NEXT LINE AND FINISH THE LINE
#df = 



# STEP 2: Now start a list to save each found station number to
# Write your code below:


# STEP 3: To retrieve data from all stations we need to get all the station numbers.
# In the API documentation (https://api-docs.luchtmeetnet.nl/#intro) find the URL to retrieve station numbers.
# Check how many pages there are and create a loop which goes from 1 to the total number of pages.
# Inside the loop retrieve the stations data of that page.
# Loop over that data.
# Save the station numbers to the earlier created list.
# Write your code below:





# STEP 4 Now save the list in a column of the DataFrame
# Write your code below:



# STEP 5: Now that we have a list of all stations we want you to add the station coordinates to it. First start the list. 
# Write your code below:

# Next you need to look in the API documentation for the url to retrieve information of a station.
# Loop over all station numbers found previously and use the url to retrieve information of each station.
# Look in the data of a station where to find the coordinates.
# Save each station's coordinates.
# note: the coordinates returned by the API are in the wrong order (at least for the shapely Point class which we will use later)
# You can reverse a list as such:  some_list[::-1]
# Write your code below:

# Now save the coordinate list to a column in the DataFrame
# Write your code below:



# STEP 6:  We will now create Point geometries from the coordinate data, allowing it to be actually be projected. 
# For this we will be using geopandas
# http://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py
# To help you a bit we have prepared part of the code you need. Finish the line of code and apply point geometry.
# REMOVE THE HASHTAG IN THE NEXT LINE
#df['geom'] = 

# Step 7: To convert this regular DataFrame to a GeoDataFrame we need tell GeoPandas in which column the geometry is located
# http://geopandas.org/gallery/create_geopandas_from_pandas.html#sphx-glr-gallery-create-geopandas-from-pandas-py
# Now finish the following line of code
# REMOVE THE HASHTAG IN THE NEXT LINE
#gdf = 


# Step 8: To get the the value of particulate matter for 2.5 μm and 10 μm or less per m3 for all stations,
# you will need to loop over all stations like before. Now look in the API documentation how to request the measurements of a station. 
# From each station save the latest measurement to the created list. If the station has no measurements for your selected compound append a 'float('nan')' to the list.
# Do this for 2.5 μm per m3 and repeat it for 10 μm per m3.
# Write your code below:



# Step 9: Now look back at the previous exercise and find out how you would get measurements for a specific time period (in our case 2017). 
# Note that the luchtmeetnet API only allows you to get data for 7 days. Need to make a additional loop to get the data (if you do not succeed, 7 days would also be fine).
# Create a script to add multiple measurements and calculate the average for 2017. Do this for 2.5 μm per m3 and repeat it for 10 μm per m3.
# Write your code below:


# Step 10: Now save the list to a column in the GeoDataFrame
# REMOVE THE HASHTAG IN THE NEXT LINE
#gdf['value'] = 



# Step 11: Finally save to a shapefile:
# REMOVE THE HASHTAG IN THE NEXT LINE
#gdf.to_file('./shp/measurements.shp')

# Now save this script and go back to https://github.com/SPINLab/GI_Minor_2020/tree/master/py1_LuchtmeetnetAPI 
# to answer a couple of questions and see what exactly need to be submitted.
