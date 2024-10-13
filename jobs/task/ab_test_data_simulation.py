import numpy as np
import pandas as pd

# Parameters
n = 20000  # number of users
p_a = 0.1  # probability of purchase for group A
p_b = 0.20  # probability of purchase for group B

# Simulate user IDs and group assignment
user_ids = np.arange(1, n + 1)
groups = np.random.choice(['A', 'B'], size=n)

# Simulate purchases based on group assignment
purchases = np.where(groups == 'A',
                     np.random.binomial(1, p_a, size=n),
                     np.random.binomial(1, p_b, size=n))

# Simulate revenue (only for users who made a purchase)
revenue = np.where(purchases == 1, np.random.randint(5, 15, size=n), 0)

# Create a DataFrame
data = pd.DataFrame({
    'user_id': user_ids,
    'group': groups,
    'purchase': purchases,
    'revenue': revenue
})

print(data.head(20))
