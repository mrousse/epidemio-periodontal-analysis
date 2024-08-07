## 07/08/24 - Manon ROUSSE
## Plot distribution of survey participants

from scipy import stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import data
file_path = "/Users/manon/Downloads/Enquete Epidemio 2022 - CNEP RE_PONSES 2.xlsx"
dataframe = pd.read_excel(file_path)
total_rows = len(dataframe)

# Plot distribution Age
profile_characteristics = {
    "Sexe": ["Homme", "Femme"],
    "Fumeur": ["Oui", "Non"],
    "Formation": ["Aucune", "CAP,BEP...", "Bac", "Bac à Bac+3", "Bac+4 et +"],
    "Profession": [
        "Agriculteurs",
        "Artisans",
        "Cadres",
        "Professions \n intermédiaires",
        "Salariés",
        "Ouvriers",
        "Retraités",
        "Autres",
    ],
}

num_characteristics = len(profile_characteristics.keys()) + 1

# Determine the grid size for the plots
rows = 2 if num_characteristics > 1 else 1
cols = (num_characteristics + 1 + rows - 1) // rows

# Create subplots
# fig, axes = plt.subplots(rows, cols, figsize=(15, 7)) # For little screen
fig, axes = plt.subplots(rows, cols, figsize=(18, 10))  # For big screen
axes = axes.flatten()  # Flatten the array of axes for easy iteration

# Plot Age distribution
age_name = "Age"
if age_name in dataframe.columns:
    axes[0].hist(dataframe[age_name].dropna(), bins=20, edgecolor="black")

    axes[0].grid(True)
else:
    axes[0].text(0.5, 0.5, f'Column "{age_name}" not found', ha="center", va="center")
# Set title
axes[0].set_title(f"Distribution de {age_name}")

# Plot other characteristics as bar plots
for i, characteristic in enumerate(profile_characteristics.keys()):
    if (
        characteristic in dataframe.columns
        and characteristic in profile_characteristics.keys()
    ):
        # Get the data for the characteristic
        data = dataframe[characteristic].dropna()

        # Count the occurrences of each label
        counts = data.value_counts().sort_index()

        # Get the bar labels and their corresponding counts
        labels = profile_characteristics[characteristic]
        values = [counts.get(i, 0) / total_rows * 100 for i in range(len(labels))]

        # Plot the bar chart
        axes[i + 1].bar(labels, values, edgecolor="black")
        axes[i + 1].grid(True)
        axes[i + 1].set_xticks(
            range(len(labels)), labels=labels, rotation=45, ha="right"
        )
    else:
        axes[i + 1].text(
            0.5,
            0.5,
            f'Characteristic "{characteristic}" not found or no labels',
            ha="center",
            va="center",
        )
    # Set title
    axes[i + 1].set_title(f"Distribution de {characteristic}")

# Hide any unused subplots
for j in range(i + 2, len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
