# National Health Assessment & Alcohol Reduction Strategy in India

## 📌 Project Overview
* **Objective:** A data-driven analysis of alcohol consumption patterns across Indian States and Union Territories.
* **Socio-Economic Insight:** Identifies deep-rooted challenges and categorizes regions into risk profiles to pinpoint economic drain.
* **Dual-Pillar Strategy:**
    * **Technological Safeguards:** Protecting the younger generation from early exposure.
    * **Family Wealth Plan:** Transitioning alcohol expenditure into long-term financial assets (The **"Sobriety Dividend"**).

---

## 🧪 Methodology: Exploratory Data Strategy (EDS)
The project utilizes **EDS** to analyze the 2021 Alcohol Consumption dataset.

### 🔄 Data Processing Pipeline
* **Cleaning & Normalization:** * Addressed data irregularities and negative percentage values.
    * Utilized clipping algorithms to ensure analytical consistency.
* **Pattern Recognition:** * Identified **Rural-Urban Disparity**.
    * Found rural male consumption (**19.92%**) significantly higher than urban centers (**16.53%**).
* **Machine Learning:** * Implemented **K-Means Clustering** to group states into three distinct risk zones.

---

## 🤖 Machine Learning & Analytics

### 📊 Clustering Risk Zones
Using `Scikit-learn`, states were categorized based on gendered consumption percentages:
* **🔴 High Risk (Cluster 2):** States like Arunachal Pradesh and Sikkim (Male consumption >45%).
* **🟡 Moderate Risk (Cluster 0):** States like Telangana and Goa (~34% consumption) — identified as a **"wealth trap."**
* **🟢 Low Risk (Cluster 1):** Majority of states with consumption levels around 18%.

### 🧠 Correlation Analysis
* **Household Habit Discovery:** Heatmap analysis revealed a strong positive correlation between male and female consumption within the same household.
* **Insight:** Suggests alcohol use is an environmental habit affecting the entire family unit rather than an individual choice.

---

## 🛡️ Strategic Interventions: The "Triple-Lock" Framework
Proposed automated and legislative "locks" to protect minors:
1. **Digital Lock:** Aadhaar-linked biometric API for all alcohol transactions to automate age-gating.
2. **Educational Lock:** A neuroscience-based curriculum focusing on **prefrontal cortex** development.
3. **Legal Lock:** Establishing 300-meter **"Sacred Zones"** around schools where retail is prohibited.

---

## 💰 The Sobriety Dividend (Financial Modeling)
Modeling the redirection of a monthly alcohol spend (approx. **₹4,000**) into a prosperity fund (**12% annual yield**):
* **20-Year Projection:** Results in a corpus of approximately **₹40 Lakhs**.
* **Impact:** Sufficient for higher education or clearing home loans.

---

## 💻 Technical Implementation

### Data Normalization (SQL)
```sql
-- Ensuring data consistency by removing negative values
UPDATE National_Health_Data 
SET Consumption_Value = 0 
WHERE Consumption_Value < 0;

---

## 💻 Technical Implementation

### Wealth Projection (SQL)
```sql
-- Calculating cumulative savings for the Family Wealth Plan
SELECT User_ID, 
       SUM(Daily_Savings) AS Total_Principal, 
       (SUM(Daily_Savings) * 1.12) AS Projected_Yearly_Growth 
FROM User_Savings_Log 
WHERE Transaction_Date >= '2025-01-01' 
GROUP BY User_ID;
sql




