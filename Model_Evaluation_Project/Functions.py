import pandas as pd 

def continuous_descriptive_stats(data, continuous_vars, group_by=None):
    # Initialize a list to store results
    results = []
    
    if group_by:
        # Group data by the specified categorical variable
        grouped_data = data.groupby(group_by)
    else:
        grouped_data = [('Overall', data)]
    
    for category, group in grouped_data:
        # Calculate descriptive statistics for each continuous variable within the group
        for cont_var in continuous_vars:
            stats = group[cont_var].describe()
            results.append({
                'Feature': cont_var,
                'Category': category,
                'Mean': stats['mean'],
                'Median': stats['50%'],
                'Std Dev': stats['std'],
                'Skew': group[cont_var].skew(),
                'Kurtosis': group[cont_var].kurtosis()
            })
    
    # Convert the list of dictionaries to a DataFrame
    results_df = pd.DataFrame(results)
    
    return results_df  


def categorical_descriptive_stats(data, categorical_vars):
    # Initialize a list to store results
    results = []
    
    for cat_var in categorical_vars:
        # Calculate counts for each category of the categorical variable
        counts = data[cat_var].value_counts()
        for category, count in counts.items():
            results.append({
                'Feature': cat_var,
                'Category': category,
                'Count': count
            })
    
# Convert the list of dictionaries to a DataFrame
    results_df = pd.DataFrame(results)
    
    return results_df  
