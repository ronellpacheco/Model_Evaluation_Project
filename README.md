# Model_Evaluation_Project

ModelEvaluator is a project aimed at evaluating the performance of machine learning models, specifically CatBoost and RandomForest, for a classification task. The project involves data preprocessing, generating descriptive statistics, and comparing model performance with and without hyperparameter tuning.

Data Preprocessing

The dataset used in this project undergoes several preprocessing steps to handle missing values and address class imbalance. Categorical features are appropriately converted to string types, and class weights are used during model training.

Descriptive Statistics Functions

Two primary functions are developed using the Pandas library to generate descriptive statistics:

continuous_descriptive_stats: Calculates descriptive statistics for continuous variables, optionally grouped by a categorical variable.
categorical_descriptive_stats: Calculates counts for each category of categorical variables.
Model Evaluation
CatBoost Model
Without tuning: Achieved an F1 score of 0.7595.
With GridSearchCV tuning: Achieved an F1 score of 0.7107.
Random Forest Model
Without tuning: Achieved an F1 score of 0.6071.
With GridSearchCV tuning: Achieved an F1 score of 0.6089.
Findings and Recommendations
CatBoost outperformed RandomForest in both default and tuned states.
The superior performance of CatBoost was due to its effective handling of categorical features and robust default hyperparameters.
Future work should include further exploration of feature engineering techniques and alignment with the business context for improved model performance.
