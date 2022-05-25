# Predicting House Prices in King County, US
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/readme_image.png)

## Table of Contents
- <a href="#overview">Overview</a>
- <a href="#requirements">Requirements</a>
- <a href="#installation">Installation</a>
- <a href="#demo-and-usage">Demo and Usage</a>
- <a href="#dataset">Dataset</a>
- <a href="#exploratory-data-analysis">Exploratory Data Analysis</a>
- <a href="#modelling">Modelling</a>
- <a href="#model-performance">Model Performance</a>
- <a href="#limitations">Limitations</a>
- <a href="#conclusion">Conclusion</a>

## Overview
This aim of this project is to utilize **regression algorithms** to predict final house sale prices in King County in Washington State. The project is from the perspective of being hypothetically commissioned by a local realty company in Seattle to produce a model to accurately predict sale prices. 
<br><br>
For the project, both a **predictive model** and **inferential model** have been created.

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
The data distributions also show many features with **outliers** e.g.,
- **price**
- **bedrooms**
- **sqft_living**

Once the data had been cleaned, the dataset was split into 2 parts. One part holds property values below **$1mil** and the rest is everything above that value.
This was done to make the price distributions for both of the target variables normally distributed.
![image](https://github.com/AbsIbs/King_County_Project/raw/main/images/house_price distributions.png)

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




## Modelling
The regression algorithms used are:
>Linear Regression<br>
>Random Forest<br>
>Gradient Boosting<br>
>Histogram Gradient Boosting

## Model Performance

## Limitations

## Conclusion




