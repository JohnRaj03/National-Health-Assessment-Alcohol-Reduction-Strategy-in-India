# National-Health-Assessment-Alcohol-Reduction-Strategy-in-India
Project Overview
This project presents a data-driven analysis of alcohol consumption patterns across Indian States and Union Territories. It moves beyond surface-level statistics to identify deep-rooted socio-economic challenges, categorizing regions into risk profiles to understand where economic drain is most severe.
+2

The ultimate goal is to establish a roadmap for change through a dual strategy:


Technological Safeguards: Protecting the younger generation from early exposure.


Family Wealth Plan: Redirecting alcohol expenditure into long-term financial assets, termed the "Sobriety Dividend".

Methodology: Exploratory Data Strategy (EDS)
The project utilizes an Exploratory Data Strategy (EDS) to analyze the 2021 Alcohol Consumption dataset.
+1

Data Processing Pipeline

Cleaning & Normalization: Handled data irregularities, such as negative percentage values, using clipping algorithms to ensure analytical consistency.


Pattern Recognition: Identified a "Rural-Urban Disparity," finding that male consumption in rural areas (19.92%) is significantly higher than in urban centers (16.53%).


Unsupervised Machine Learning: Implemented K-Means Clustering to group states into three distinct risk zones.

Machine Learning & Analytics
Clustering Risk Zones
Using Scikit-learn, states were categorized based on male and female consumption percentages:


High Risk (Cluster 2): States like Arunachal Pradesh and Sikkim (Male consumption >45%).


Moderate Risk (Cluster 0): States like Telangana and Goa (~34% consumption), identifying a "wealth trap" for middle-income families.


Low Risk (Cluster 1): Majority of states with consumption around 18%.

Correlation Analysis
A heatmap analysis revealed a strong positive correlation between male and female consumption within households, suggesting that alcohol use is an environmental habit affecting the entire family unit.

Strategic Interventions: The "Triple-Lock" Framework
To protect minors and reduce consumption, the project proposes three "locks":


Digital Lock: Aadhaar-linked biometric API for all alcohol transactions to automate age-gating.
+1


Educational Lock: Shifting from moral policing to a neuroscience-based curriculum focusing on prefrontal cortex development.


Legal Lock: Establishing 300-meter "Sacred Zones" around schools where retail is prohibited.

The Sobriety Dividend (Financial Modeling)
The project models the redirection of a monthly alcohol spend (e.g., ₹4,000) into a prosperity fund yielding 12% annually.


20-Year Projection: Results in a corpus of approximately ₹40 Lakhs, sufficient for higher education or clearing home loans.

Technical Implementation (SQL & Python)
Data Normalization
SQL

-- Normalizing data for analytical consistency
UPDATE National_Health_Data 
SET Consumption_Value = 0 
WHERE Consumption_Value < 0;


Wealth Projection Query
SQL

-- Calculating cumulative savings for the Family Wealth Plan
SELECT User_ID, 
       SUM(Daily_Savings) AS Total_Principal, 
       (SUM(Daily_Savings) * 1.12) AS Projected_Yearly_Growth 
FROM User_Savings_Log 
WHERE Transaction_Date >= '2025-01-01' 
GROUP BY User_ID;


Visualizations Included in Documentation

Figure 3: Urban vs. Rural Alcohol consumption.


Figure 5: Elbow method for optimal K identification.


Figure 6: Correlation heatmap of gender consumption patterns.


Figure 12: Exponential wealth growth over 20 years through redirected savings.

Author
John Raj T Date: 30/12/2025
