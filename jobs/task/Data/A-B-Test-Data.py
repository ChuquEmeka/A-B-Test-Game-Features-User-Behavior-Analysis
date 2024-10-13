import numpy as np
import pandas as pd

def generate_ab_test_data(total_users):
    """
    Generates simulated A/B test data with a given total number of users.
    49% of the users are assigned to Group A and 51% to Group B, without sorting.
    
    Parameters:
    - total_users: int, total number of users (sum of Group A and Group B)
    
    Returns:
    - pd.DataFrame: DataFrame containing user_id, group, purchase, and revenue for each user
    """
    # Setting random seed for reproducibility
    np.random.seed(42)

    # Defining percentage split between Group A and Group B
    percentage_A = 0.49  # Assigning 49% for Group A
    percentage_B = 0.51  # Assigning 51% for Group B

    # Calculating the number of users for each group
    num_users_A = int(total_users * percentage_A)
    num_users_B = total_users - num_users_A  # Ensuring total equals total_users

    # Specifying probabilities of making a purchase for each group
    purchase_probability_A = 0.1  # Setting a 10% chance to purchase in Group A
    purchase_probability_B = 0.15  
    revenue_per_purchase_A = 10    # Setting revenue per purchase for Group A
    revenue_per_purchase_B = 10     # Setting revenue per purchase for Group B

    # Generating user IDs for both groups
    user_ids_A = np.arange(1, num_users_A + 1)
    user_ids_B = np.arange(num_users_A + 1, num_users_A + num_users_B + 1)

    # Simulating purchases and revenue for each group
    purchases_A = np.random.binomial(1, purchase_probability_A, num_users_A)
    purchases_B = np.random.binomial(1, purchase_probability_B, num_users_B)

    revenue_A = purchases_A * revenue_per_purchase_A
    revenue_B = purchases_B * revenue_per_purchase_B

    # Creating DataFrames for Group A and Group B
    data_A = pd.DataFrame({'user_id': user_ids_A, 'group': 'A', 'purchase': purchases_A, 'revenue': revenue_A})
    data_B = pd.DataFrame({'user_id': user_ids_B, 'group': 'B', 'purchase': purchases_B, 'revenue': revenue_B})

    # Combining the two groups into one dataset without sorting
    data = pd.concat([data_A, data_B], ignore_index=True)

    # Shuffling the DataFrame to avoid sorted order of groups
    data = data.sample(frac=1).reset_index(drop=True)

    return data

total_users = 50000  
data = generate_ab_test_data(total_users)

data.head()
data.to_csv('Dataset/A-B-Test-Data.csv', index=False)