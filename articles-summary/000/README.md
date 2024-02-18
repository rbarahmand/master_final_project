# Demand Prediction Based on Machine Learning Algorithms for Optimal Distribution of Insulin

Fields: data, drug, ml, prediction model
: 1
Added by: Dr. Ebadati
Created time: February 13, 2024 8:42 PM
Interesting?: ⭐⭐⭐
Status: Reading
URL: https://www.sciencedirect.com/science/article/pii/S2405896323012764
Year: 2023

### Title

- **Keywords:** demand, prediction, ML, distribution, Insulin
- **Abbreviations:** PSC (pharmaceutical supply chain)

### Abstract

- **Research gap:** In pharmaceutical segment we often have complex supply chain network with many stockholders, so coming up with fairly good prediction method can leads to optimal producing and distribution (predict required quantity of Insulin) .
- **Methods:**
  - Modeling: Random forest, multiple regression, ANN
  - Performance metrics: Mean squared error, The coefficient of determination, R-value
  - Mathematical model (uncertain predicts) = max(customer satisfaction)
- Result and discussion: Maximize customer satisfaction and optimal distribution at the same time, by predicting Insulin demand.

### Introduction

**Background:** We have a fairly complex pharmaceutical supply chain (PSC) in one side, in other side we have the demand constantly changing (either because of diseases evolution affecting their health or the emergence of new epidemics), so the demand prediction part become essential for special drugs (like insulin), because it is the entry point for optimizing complex parts in drug production and drug delivery time and quantity. It is also obvious that we can not relay on a single time series analysis due to uncertainty nature of this segment.

Methods: at PSC level, demand prediction is not the only part affecting the optimal distribution of drugs, thus many mathematical models developed over the years to address this issue, mostly operation parts (facility location, location for delivering drugs in large cities).

**Aim:**

- Develop a mathematical model to optimize the distribution of insulin demand, using several factors to ensure costumer satisfaction:
  - Quality of transported products
  - the storage conditions during transport
  - delivery time
  - Prediction model to forecast customer demand
    - ML algorithms
    - Factors that triggers this feature

---

### Method

- **The problem:**

  - Supply chain network

  - <img src=./images/Untitled.png width=500>

  - Our main focus in this context, is more on the downstream part of the distribution (aka. PSC)
  - There are different types of insulin, but this study aims to just identify the need of Insulin.
  - **Assumptions:**
    - The locations of manufacturers, distributors, and customers are predefined and fixed.
    - We consider that the supply and production processes do not affect our distribution process. Therefore, it is always possible that a manufacturer supplies a distributor in each given period.
    - Each customer could be served by one or more distributors depending on its amount of demand.
    - The demand for each customer is uncertain and changes according to the need of the customers and the factors influencing its variability.

- **Optimization of distribution:**

  - Create a diagram for the mathematic model

  - <img src=./images/article00.drawio.png width=600>

  - What optimization algorithm used is not mentioned.
  - Mathematical formulation is presented in GAMS and solved CPLEX solver.
  - The Problem Generated

    - 4 distributors (I=4)
    - 8 demand zones (J=8)
    - 12 time periods (T=12)
    - 4 different vehicles (V=4)
    - Parameters are generated uniformly random

    - <img src=./images/Untitled%201.png width=500>

    - The demand information obtained from ANN (best model)
    - Generated demand is also use uniform distribution
    - For the test problem, the optimum value of the objective function is 15 368×103.

- **ML model for predicting demand:**

  - Data:

    - USA (2013 - 2019)
    - Companies: Sanofi, Eli Lilly, and Novo Nordisk
    - Data grouped into an output variable target (total number of patients, available on website clincalc.com)
    - Input (vector of features).

    - <img src=./images/Untitled%202.png width=500>

    - output (target value, total number of patients)

  - Model:
    - Supervised, Regression Problem
    - ANN
      - Sigmoid activation function
      - regularization rate 0.01 (avoid overfit)
      - Number of epochs (8000)
      - back propagation algo. (Levenberg–Marquardt Method)
    - Multiple Regression (differs form multivariate regression)
      - find relationship between multiple independent features and one dependent target.
    - Random forest
      - Number of trees is the most important parameter (not mentioned)
  - Evaluation metrics:
    - (80/20 data split)
    - $R^2$ (the lower the better)
    - $RMSE$ (the lower the better)
    - Regression R-value (the more the better)

### Results

- The best model was ANN

- <img src=./images/Untitled%203.png width=500>

- They might not tune the parameters for random forest good enough
- ANN R-value approximately is equal to 93.10%
- These predictions then fed into the mathematical model, for optimization.

---

### Seductions:

- Use more sophisticated ensemble algorithms: XGBOOST, CATBOOST, LightGBM
- Search for other models
- Search for types of data needed to implement this problem in IRAN

---

### Important resources:

- **The mathematical model used:** Liu, P., Hendalianpour, A., Razmi, J., & Sangari, M. S. (2021). A solution algorithm for integrated production-inventory-routing of perishable goods with transshipment and uncertain demand. Complex & Intelligent Systems, 7(3), 1349-1365.
- **The ANN used:**
  - Ayyadevara, V. (2018). Pro Machine Learning Algorithms: A Hands-On Approach to Implementing Algorithms in Python and R. Apress, ISBN: 978-1484235638.
  - Kroese, D. P., Botev, Z. I., Taimre, T., & Vaisman, R. (2019). Data science and machine learning: mathematical and statistical methods. Chapman and Hall/CRC, New York.
- **Multiple regression:**
  - Moore, A. W., Anderson, B., Das, K., & Wong, W. K. (2006). Combining multiple signals for biosurveillance. Handbook of biosurveillance, 235.
  - Kroese, D. P., Botev, Z. I., Taimre, T., & Vaisman, R. (2019). Data science and machine learning: mathematical and statistical methods. Chapman and Hall/CRC, New York.
- **Random forest used:**
  - Ayyadevara, V. (2018). Pro Machine Learning Algorithms: A Hands-On Approach to Implementing Algorithms in Python and R. Apress, ISBN: 978-1484235638.
  ***

### What to do?

- [x] Add mathematical part (use plain Eq. or diagram)
