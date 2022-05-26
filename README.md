# Predicting House Prices in King County, US
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/readme_image.png)

## Table of Contents
- <a href="#business-case">Business Case</a>
- <a href="#requirements">Requirements</a>
- <a href="#installation">Installation</a>
- <a href="#demo-and-usage">Demo and Usage</a>
- <a href="#dataset">Dataset</a>
- <a href="#exploratory-data-analysis">Exploratory Data Analysis</a>
- <a href="#modelling">Modelling</a>
- <a href="#model-performance">Model Performance</a>
- <a href="#conclusion">Conclusion</a>

## Business Case
This aim of this project is to utilize **regression algorithms** to predict final house sale prices in King County in Washington State. The project is from the perspective of being hypothetically commissioned by a local realty company in Seattle to produce a model to accurately predict sale prices. 
<br><br>
For the project, both a **predictive model** and **inferential model** have been created. Our inferential model aims to answer the question, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**"How much does a predictor affect price? If we raise the value of the predictor, how will price change?"**

## Requirements
This project assumes you already have these system dependencies set up:
- **Python 3.8.5**
- **pip**
- **Conda environment set-up**

## Installation
As all the dependencies are stored in the **requirements.txt** file, running this command in your bash/terminal  <br>
```bash
pip: -r requirements.txt
```

## Demo and Usage
The project has been summarized in the form of a **house prediction** <a href="https://kc-house-predictor.herokuapp.com/">webapp</a> where users can select values from a host of features and retrieve the predicted house price.<br><br>
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/kc_county_project_image.png)

## Dataset
- Source: **King County Assessor's public website**
- Over 21,000 houses
- Period: **May 2014 - May 2015**
- Additional fetures: web scraped data from **www.UnitedStatesZipCodes.org**

## Exploratory Data Analysis
### Data Cleaning
Examining the distributions of features revealed a large amount of missing values skewed distributions which had to be resolved.
<br><br>
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/initial_distributions.png)
<br><br>
The data distributions also show many features with **outliers** e.g.
- **price**
- **bedrooms**
- **sqft_living**

Once the data had been cleaned, the dataset was split into 2 parts. One part holds property values below **$1mil** and the rest is everything above that value.
This was done to make the price distributions for both of the target variables normally distributed.
<br><br>
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/house_price_distributions.png)

### Feature Engineering
#### Feature engineering from the dataset
Focused mainly on ratios and the distance between the house and major cities i.e. **Seattle and Redmond**
<br><br>
Example
```python
# average room size
low_prices_df['average_room_size'] = low_prices_df['sqft_living'] / (low_prices_df['bathrooms'] + low_prices_df['bedrooms'])

# floor area ratio
low_prices_df['floor_area_ratio'] = low_prices_df['sqft_living'] / low_prices_df['sqft_lot']

# bedroom - bathroom ratio
low_prices_df['bedroom_bathroom_ratio'] = low_prices_df['bathrooms'] / low_prices_df['bedrooms']

high_prices_df['average_room_size'] = high_prices_df['sqft_living'] / (high_prices_df['bathrooms'] + high_prices_df['bedrooms'])
high_prices_df['floor_area_ratio'] = high_prices_df['sqft_living'] / high_prices_df['sqft_lot']
high_prices_df['bedroom_bathroom_ratio'] = high_prices_df['bathrooms'] / high_prices_df['bedrooms']
```

#### Web scraped data from [UnitedStatesZipcodes](www.UnitedStatesZipCodes.org)
For each zipcode, we retrieve data from this list of items.
<br><br>
```python
['population', 'land_area', 'pop_density', 'water_area', 'income', 'nearby_schools']
```

Finally, we can view a heatmap of all of our features.
<br><br>
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/heatmap.png)

In addition, when utilising the data gained from web scraping and longitude & latitude, we can visualise the house price with respect to location.
<br><br>
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/price_maps.png)

## Modelling
The regression algorithms used are:
>Linear Regression<br>
>Random Forest<br>
>Gradient Boosting<br>
>Histogram Gradient Boosting

## Model Performance
To record our model performance, we'll use 2 metrics:
- **R2**
- **RMSE**

### **Predictive Modelling**
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/predictive_models.png)
<br><br>
**Low house prices summary**
<br>
|                Regressor 	|     R2 	|   RMSE 	|
|-------------------------:	|-------:	|-------:	|
| Histogram_Gradient_Boost 	|  0.852 	|  73800 	|
|            Random_Forest 	|  0.846 	|  75400 	|
|           Gradient_Boost 	|  0.838 	|  77400 	|
|        Linear_Regression 	|  0.795 	|  87000 	|
|          Dummy Regressor 	| -0.000 	| 192200 	|

**High house prices summary**
<br>
|                Regressor 	|     R2 	|   RMSE 	|
|-------------------------:	|-------:	|-------:	|
|            Random_Forest 	|  0.337 	| 284800 	|
|           Gradient_Boost 	|  0.287 	| 293300 	|
| Histogram_Gradient_Boost 	|  0.263 	| 297600 	|
|        Linear_Regression 	|  0.222 	| 307600 	|
|          Dummy Regressor 	| -0.004 	| 354200 	|

<br>
Interestingly, we can see a clear disparity in performance between our 2 sets of models. The poor performance from our high house price predictive models may be due to lack of clear correlations between features and price as well as lack of data.

### **Inferential Modelling**
- For our inferential models, adhering to the assumptions of linear regression becomes critical.
- A crucial rule when conducting inferential modelling revolves around avoiding autocorrelation between features. As such, our feature count is heavily cut. 
- In addition to this, the features used were categorical features and the logged continuous features.
- Rather than price as the target variable, our inferential model used **log price** as the target.

|                   	|     R2 	| RMSE 	|
|------------------:	|-------:	|-----:	|
| Low house prices 	|   0.56 	| 0.24 	|
| High house prices 	| -4.482 	| 0.22 	|

Whilst the low house prices did not perform too well, the high house prices model performed terribly. Again, this may be due to the reasons mentioned above.

## Results
These results will focus on the performance of our superior **low house prices models**.
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/predictive_model_results.png)
<br><br>
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/inferential_results.png)

With regards to our inferential models, the main findings were,
- for every 1% increase in average income in the area, the price of the house increases by 0.38%
- for every 1% increase in the average room size, the price of the house increases by 0.54%
- for every 1% increase in the distance from Redmond, the price of the house decreases by 0.16%

## Conclusion
Our predictive model and inferential model seem to be usable for house prices up to $1mil however, unusable for more expensive houses. Our inferential model shows that the average income of the area, distance from redmond and average room size affect house prices the most.
<br><br>
For future studies, it is advised to retrieve a significantly larger amount of data for houses above the $1mil mark in order to train more accurate models.



