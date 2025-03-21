# Project_4_Machine_Learning


## Analyzing and Predicting Health Inspection Scores for Food Establishments in San Francisco ##

Objective: To analyze and predict health inspection scores and risk categories for food establishments in San Francisco.

Implementation:\
We built machine learning models that predict:
Inspection Scores based on violations and other relevant data. 
Risk Categories of food establishments based on violation data.

Dataset:\
We used a dataset provided by the San Francisco Health Department, which contains inspection reports for food establishments. The dataset includes various features that represent the violations observed, inspection scores, and business details.
Chose datset from San Francisco, California, USA https://data.sfgov.org/Health-and-Social-Services/ARCHIVED-Restaurant-Inspection-Scores-2016-2019-/pyih-qa8i/about_data

The dataset had the following columns business_id,business_name,business_address,business_city,business_state,business_postal_code,business_latitude,business_longitude,business_location,business_phone_number,inspection_id,inspection_date,inspection_score,inspection_type,violation_id,violation_description,risk_category,Neighborhoods,SF Find Neighborhoods,Current Police Districts,Current Supervisor Districts,Analysis Neighborhoods

Potential Questions we will explore :

What patterns are observed in the violations that lead to higher inspection scores or risk categories?

Can we predict the risk category (high, moderate, or low) of a food establishment based on the violation descriptions and other features?
Can we predict the inspection score for a facility based on the types and numbers of violations observed?
Potential Models:

For predicting the inspection score: Regression models like Logistic Regression, Random Forest Classifier, and Support Vector Machines (SVM) will be used to predict the risk level of each establishment.
For classifying risk categories: Classification models

Expected Outcomes:
Predictive models that can help businesses and health officials forecast inspection scores and risk categories.
Data-driven insights that identify which violations are most likely to contribute to poor inspection scores or high-risk categories.
A user-friendly interface that allows users to input violation data and receive predictions about the establishment's inspection score or risk category..

Linear Regression RMSE: 5.702782186389993
Random Forest Regressor RMSE: 3.0713432370119276
SVR RMSE: 7.140268092985499

<img width="719" alt="Screenshot 2025-03-18 at 10 18 12 PM" src="https://github.com/user-attachments/assets/57fac36f-4023-4b02-a83d-76d4dcda100b" /> 

Logistic Regression Accuracy: 0.9942363112391931
Random Forest Classifier Accuracy: 0.9932756964457252
SVM Classifier Accuracy: 0.9125840537944284

![Screenshot 2025-03-19 at 9 34 15 AM](https://github.com/user-attachments/assets/8f374f6b-a293-4ea5-87b7-4f4b9983ad97)  

Most Common Violations in High-Risk Establishments

![Screenshot 2025-03-20 at 8 05 18 PM](https://github.com/user-attachments/assets/cf240339-2f28-43bd-9c72-55c81910613f) 

Random Forest Classifier - Classification Report

![Screenshot 2025-03-19 at 9 43 46 AM](https://github.com/user-attachments/assets/6525dabb-75ea-4ddf-850d-862ee775a922) 

Violin Plot: Inspection Scores by Risk Category 

![Screenshot 2025-03-19 at 10 03 46 AM](https://github.com/user-attachments/assets/2bec1cb1-2fc7-4cfe-99f0-c6525252bc05) 


References 
[1] https://data.sfgov.org/Health-and-Social-Services/ARCHIVED-Restaurant-Inspection-Scores-2016-2019-/pyih-qa8i/about_data
[2] https://dev.socrata.com/foundry/data.sfgov.org/pyih-qa8i 
[3] https://scikit-learn.org/stable/api/sklearn.datasets.html 
[4] https://ngrok.com/docs/ 
[5] https://data.sfgov.org/Health-and-Social-Services/ARCHIVED-Restaurant-Inspection-Scores-2016-2019-/pyih-qa8i/related_content 








