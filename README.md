# Project_4_Machine_Learning


## Analyzing and Predicting Health Inspection Scores for Food Establishments in San Francisco##

Objective: to analyze and predict health inspection scores and risk categories for food establishments in San Francisco.

Implementation:\
We built machine learning models that predict:
Inspection Scores based on violations and other relevant data. 
Risk Categories of food establishments based on violation data.

Dataset:\
We used a dataset provided by the San Francisco Health Department, which contains inspection reports for food establishments. The dataset includes various features that represent the violations observed, inspection scores, and business details.
Chose datset from San Francisco, California, USA https://data.sfgov.org/Health-and-Social-Services/ARCHIVED-Restaurant-Inspection-Scores-2016-2019-/pyih-qa8i/about_data

The dataset had the following columns business_id,business_name,business_address,business_city,business_state,business_postal_code,business_latitude,business_longitude,business_location,business_phone_number,inspection_id,inspection_date,inspection_score,inspection_type,violation_id,violation_description,risk_category,Neighborhoods,SF Find Neighborhoods,Current Police Districts,Current Supervisor Districts,Analysis Neighborhoods
Potential Questions we will explore
What patterns are observed in the violations that lead to higher inspection scores or risk categories?
Can we predict the risk category (high, moderate, or low) of a food establishment based on the violation descriptions and other features?
Can we predict the inspection score for a facility based on the types and numbers of violations observed?
Potential Models:
For predicting the inspection score: Regression models like Logistic Regression, Random Forest Classifier, and Support Vector Machines (SVM) will be used to predict the risk level of each establishment.
For classifying risk categories: Classification models
Expected Outcomes:
Predictive models that can help businesses and health officials forecast inspection scores and risk categories.
Data-driven insights that identify which violations are most likely to contribute to poor inspection scores or high-risk categories.
A user-friendly interface that allows users to input violation data and receive predictions about the establishment's inspection score or risk category.
