import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Function to generate random samples
def generate_random_samples(slope_df, length, seed=None):
    samples = []
    for _ in range(length):
        # Step 1: Randomly sample a transect
        transect = slope_df.sample(1)
        
        # Step 2: Generate a random value within the CI bounds for the sampled transect
        lower = transect['CI_Lower'].values[0]
        upper = transect['CI_Upper'].values[0]
        median = transect['Slope'].values[0]
        
        # Randomly sample a value weighted towards the median
        random_value = np.random.triangular(left=lower, mode=median, right=upper)
        
        samples.append({
            'Transect': transect['Transect'].values[0],
            'Sampled_Value': random_value
        })
    
    return pd.DataFrame(samples)

def beach_slope_plot(slope_df, sampled_df,images_path):
    plt.figure(figsize=(8, 4))

    # Plot original distributions as lines
    for _, row in slope_df.iterrows():
        # Generate a valid array for the triangular distribution
        triangular_samples = np.random.triangular(
            row['CI_Lower'], row['Slope'], row['CI_Upper'], size=1000
        )
        
        # Ensure the array contains valid numeric values
        if not np.all(np.isfinite(triangular_samples)):
            print(f"Invalid values encountered in transect {row['Transect']}")
            continue
        
        # Plot the triangular distribution
        sns.kdeplot(
            triangular_samples,
            label=f"Transect {int(row['Transect'])}",  # Convert to integer to remove decimals
            linewidth=1.5
        )

    # Plot the final sampled distribution as a filled curve
    sns.kdeplot(
        sampled_df['Sampled_Value'],
        label="Sampled Distribution",
        color="black",
        fill=True,
        alpha=0.5
    )

    # Title and labels
    plt.xlabel("Beach slope", fontsize=14)
    plt.ylabel("Number of datapoints", fontsize=14)
    
    # Move the legend outside
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(visible=True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(images_path, 'Slope_sampling.jpg'), dpi=300, bbox_inches='tight')
    plt.show()