# Descriptive Statistics Functions:
contains Python functions for generating descriptive statistics for both continuous and categorical variables using the Pandas library.

# Functions: continuous_descriptive_stats

- This function calculates descriptive statistics for continuous variables within a dataset, optionally grouped by a categorical variable.

# Arguments:

- data: Pandas DataFrame containing the dataset.
- continuous_vars: List of strings specifying the column names of continuous variables.
- group_by: Optional string specifying the column name to group the data by. Default is None.

# Returns:
- Pandas DataFrame containing descriptive statistics for each continuous variable.
  categorical_descriptive_stats
  This function calculates counts for each category of categorical variables within a dataset.

# Arguments:

- data: Pandas DataFrame containing the dataset.
  categorical_vars: List of strings specifying the column names of categorical variables.

# Returns:

- Pandas DataFrame containing counts for each category of categorical variables.