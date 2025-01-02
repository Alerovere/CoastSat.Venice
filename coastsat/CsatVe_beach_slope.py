import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Function to generate random samples
def generate_random_samples(slope_df, length, seed=None):
    if seed is not None:
        np.random.seed(seed)
    samples = []
    while len(samples) < length:
        transect = slope_df.sample(1)
        lower = transect['CI_Lower'].values[0]
        upper = transect['CI_Upper'].values[0]
        median = transect['Slope'].values[0]
        random_value = np.random.triangular(left=lower, mode=median, right=upper)
        
        # Filter unrealistic slopes
        if 0.01 <= random_value <= 0.4:
            samples.append({
                'Transect': transect['Transect'].values[0],
                'Sampled_Value': random_value
            })
    
    return pd.DataFrame(samples)

def adjust_bounds(row):
    epsilon = 1e-6
    if row['CI_Lower'] == row['CI_Upper']:
        row['CI_Lower'] -= epsilon
        row['CI_Upper'] += epsilon
    if row['Slope'] <= row['CI_Lower']:
        row['Slope'] = row['CI_Lower'] + epsilon
    if row['Slope'] >= row['CI_Upper']:
        row['Slope'] = row['CI_Upper'] - epsilon
    return row


def beach_slope_plot(slope_df, sampled_df, images_path):
    plt.figure(figsize=(8, 4))

    # Number of samples to match the sampled_df size
    num_samples = len(sampled_df)

    # Plot original distributions as lines
    for _, row in slope_df.iterrows():
        # Generate a valid array for the triangular distribution
        triangular_samples = np.random.triangular(
            row['CI_Lower'], row['Slope'], row['CI_Upper'], size=num_samples
        )
        
        # Filter unrealistic slopes
        triangular_samples = triangular_samples[
            (triangular_samples >= 0.001) & (triangular_samples <= 0.9)
        ]
        
        # Ensure the array contains valid numeric values
        if len(triangular_samples) == 0:
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