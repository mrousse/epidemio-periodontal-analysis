# 19/08/2024 - Manon ROUSSE
# Use the different classes to link info

from class_graph import Boxplot, Distribution, XYplot
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu

# Import data
file_path = "/Users/manon/Downloads/Enquete Epidemio 2022 - CNEP RÉPONSES 2.xlsx"
dataframe = pd.read_excel(file_path)
total_rows = len(dataframe)

## Nettoyage/age
# ax = plt.subplot()
# brossage_age = XYplot("Fréquence du brossage des dents en fonction de l'âge", ax)
# brossage_age.set_values_from_df(
#     dataframe,
#     "Age",
#     "Fréq.Brossage",
# )
# brossage_age.plot_it(
#     {
#         2: "< 1 fois/j",
#         3: "1 fois/j",
#         4: "2 fois/j",
#         5: "3 fois/j",
#         6: "> 3 fois/j",
#     },
# )
# plt.show()

## Nettoyage/age 2
ax = plt.subplot()
match_freq_int = {
    2: "< 1 fois/j",
    3: "1 fois/j",
    4: "2 fois/j",
    5: "3 fois/j",
    6: "> 3 fois/j",
}
# Group the ages by frequency values without creating a new column
groups = [
    dataframe["Age"][dataframe["Fréq.Brossage"] == key].tolist()
    for key in match_freq_int.keys()
]


# Compute the Mann-Whitney U test p-values between each pair of groups
p_values = {}
for i in range(len(groups)):
    for j in range(i + 1, len(groups)):
        stat, p_value = mannwhitneyu(groups[i], groups[j])
        p_values[
            (list(match_freq_int.values())[i], list(match_freq_int.values())[j])
        ] = p_value

# Print the p-values
for pair, p_value in p_values.items():
    print(f"P-value between {pair[0]} and {pair[1]}: {p_value:.4f}")

# Create the box plot
plt.figure(figsize=(10, 6))
plt.boxplot(
    groups,
    labels=[match_freq_int[key] for key in match_freq_int.keys()],
    patch_artist=True,
)

# Set labels and title
plt.xlabel("Fréquence de brossage")
plt.ylabel("Age")
plt.title("Distribution de l'âge des participant\npour chaque catégorie de brossage")

# Display the plot
plt.show()
