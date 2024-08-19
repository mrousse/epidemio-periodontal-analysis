# 19/08/2024 - Manon ROUSSE
# Use the different classes to plot basic info

from class_graph import Boxplot, Distribution, XYplot
import pandas as pd
import matplotlib.pyplot as plt

# Import data
file_path = "/Users/manon/Downloads/Enquete Epidemio 2022 - CNEP RÉPONSES 2.xlsx"
dataframe = pd.read_excel(file_path)
total_rows = len(dataframe)

## Ville
# ax = plt.subplot()
# villes = Boxplot("Répartition des villes de collecte des données", ax)
# villes.set_labels_values_from_df(
#     dataframe, "Ville", {"Strasbourg": "Strasbourg", "Mulhouse": "Mulhouse"}
# )
# print("Villes :", villes.labels_values)
# villes.plot_it()

## Centre
# ax = plt.subplot()
# centre = Boxplot("Répartition des lieux de collecte des données", ax)
# centre.set_labels_values_from_df(
#     dataframe, "Centre", {0: "Gare", 1: "Centre \n commercial"}
# )
# print("Centre :", centre.labels_values)
# centre.plot_it()

## Age
# ax = plt.subplot()
# age = Distribution("Répartition des âges de la population interrogée", ax)
# age.set_values_from_df(dataframe, "Age")
# print("Age :", age.values)
# percent = age.plot_it()
# print(percent)

## Sexe
# ax = plt.subplot()
# sexe = Boxplot("Part des hommes et des femmes dans la population interrogée", ax)
# sexe.set_labels_values_from_df(dataframe, "Sexe", {0: "Homme", 1: "Femme"})
# print("Sexe :", sexe.labels_values)
# sexe.plot_it()

## Tabagisme
# fig, axes = plt.subplots(1, 2, figsize=(18, 10))  # For big screen
# axes = axes.flatten()
# tabagisme = Boxplot(
#     "Part des non-fumeurs et des fumeurs\ndans la population interrogée", axes[0]
# )
# tabagisme.set_labels_values_from_df(dataframe, "Fumeur", {0: "Non-fumeur", 1: "Fumeur"})
# tabagisme.plot_it()
# print(tabagisme.labels_values)

# conso = Boxplot(
#     "Consommation tabagique en cigarettes/jour\ndes fumeurs dans la population interrogée",
#     axes[1],
# )
# conso.set_labels_values_from_df(
#     dataframe, "Nbre cigarettes", {0: "<10 cig/j", 1: ">10 cig/j"}
# )
# conso.plot_it()
# print(conso.labels_values)
# plt.show()

## Tabagisme 2
# ax = plt.subplot()
# tabac = Boxplot("Consommation tabagique dans la population interrogée", ax)
# tabac.labels_values = {
#     "Non-fumeur": 78.189,
#     "<10 cigarettes/j": 12.345,
#     ">10 cigarette/j": 9.465,
# }
# tabac.plot_it()
# plt.show()

## Tabagisme 3
# categories = ["Non-fumeur", "Fumeur"]
# percentages = [78.18930041152264, 21.810699588477366]
# fumeur_subcategories = [
#     0.5660377358490566 * percentages[1],
#     0.4339622641509434 * percentages[1],
# ]  # 56% and 44% of 'Fumeur'

# # Colors
# colors = ["#1f77b4", "#4b92c3", "#185f90"]

# # Plotting
# fig, ax = plt.subplots()

# # Plot Non-fumeur
# ax.bar(categories[0], percentages[0], color=colors[0], label="Non-fumeur")

# # Plot Fumeur with two subcategories
# ax.bar(categories[1], fumeur_subcategories[0], color=colors[1])
# ax.bar(
#     categories[1],
#     fumeur_subcategories[1],
#     bottom=fumeur_subcategories[0],
#     color=colors[2],
# )

# # Add text annotations
# ax.text(
#     1,
#     4.5,
#     f"<10 cig/j\n{int(fumeur_subcategories[0])}%",
#     ha="center",
#     color="black",
# )
# ax.text(
#     1,
#     15,
#     f">10 cig/j\n{int(fumeur_subcategories[1])}%",
#     ha="center",
#     color="black",
# )

# # Set labels and title
# ax.set_title("Consommation tabagique dans la population interrogée")
# plt.show()

## Formation
# ax = plt.subplot()
# formation = Boxplot("Niveau d’études des participants", ax)
# formation.set_labels_values_from_df(
#     dataframe,
#     "Formation",
#     {
#         0: "Aucune",
#         1: "CAP, BEP, \nCertifcat d'étude",
#         2: "Bac",
#         3: "Bac et ≤ 3 ans",
#         4: "Bac et > 3 ans",
#     },
# )
# formation.plot_it()
# print("Formation :", formation.labels_values)
# plt.show()

## Profession
# ax = plt.subplot()
# profession = Boxplot("Catégorie professionnelle des participants", ax)
# profession.set_labels_values_from_df(
#     dataframe,
#     "Profession",
#     {
#         0: "Agriculteurs\nexploitants",
#         1: "Artisans,\ncommerçants et\nchefs d’entreprise",
#         2: "Cadres\nprofessions libérales\net intellectuelles\nsupérieures",
#         3: "Professions\nintermédiaires,\ntechnicien,\ncontremaîtres,\nagent de\nmaitrise",
#         4: "Employés",
#         5: "Ouvriers",
#         6: "Retraités",
#         7: "Sans activité\nprofessionnelle",
#     },
# )
# profession.plot_it()
# print("Profession :", profession.labels_values)
# plt.show()

## Maladie générale
# ax = plt.subplot()
# maladie_gene = Boxplot("Part des participants atteints d’une maladie générale", ax)
# maladie_gene.set_labels_values_from_df(
#     dataframe,
#     "Maladie gen + type de mal.",
#     {
#         0: "Pas de maladie",
#         2: "Diabète",
#         3: "Polyarthrite\nrhumatoïde",
#         4: "Maladies\ncardiovasculaires",
#         5: "Autres",
#         1: "Ne souhaite\npas répondre",
#     },
# )
# maladie_gene.plot_it()
# print(maladie_gene.labels_values)
# plt.show()

## Brosse à dent
# ax = plt.subplot()
# brosse_dent = Boxplot("Type de brosse à dents utilisée par les participants", ax)
# brosse_dent.set_labels_values_from_df(
#     dataframe,
#     "Type BàDents",
#     {
#         2: "Manuelle",
#         3: "Electrique",
#         4: "Les deux",
#     },
# )
# brosse_dent.plot_it()
# print("Brosse à dent :", brosse_dent.labels_values)
# plt.show()
# print(sum(brosse_dent.labels_values.values()))

## Poil BaD
# ax = plt.subplot()
# poils_bad = Boxplot("Type de poils de brosse à dents utilisés par les participants", ax)
# poils_bad.set_labels_values_from_df(
#     dataframe,
#     "Type poils",
#     {
#         1: "Ne sais pas",
#         2: "Durs",
#         3: "Moyens",
#         4: "Souples",
#     },
# )
# poils_bad.plot_it()
# print("Poils de BàD :", poils_bad.labels_values)
# print(sum(poils_bad.labels_values.values()))
# plt.show()

## Tech Brossage
# ax = plt.subplot()
# tech_brossage = Boxplot("Technique de brossage pratiquée par les participants", ax)
# tech_brossage.set_labels_values_from_df(
#     dataframe,
#     "TK brossage",
#     {
#         1: "Ne sais pas",
#         2: "Horizontale",
#         3: "Verticale",
#         4: "Petits ronds",
#         5: "Oscillo-rotatif",
#     },
# )
# tech_brossage.plot_it()
# print("Technique brossage :", tech_brossage.labels_values)
# print(sum(tech_brossage.labels_values.values()))
# plt.show()

## Freq Brossage
# ax = plt.subplot()
# freq_brossage = Boxplot("Fréquence de brossages dentaires des participants", ax)
# freq_brossage.set_labels_values_from_df(
#     dataframe,
#     "Fréq.Brossage",
#     {
#         2: "< 1 fois/j",
#         3: "1 fois/j",
#         4: "2 fois/j",
#         5: "3 fois/j",
#         6: "> 3 fois/j",
#     },
# )
# freq_brossage.plot_it()
# print("Fréquence brossage :", freq_brossage.labels_values)
# print(sum(freq_brossage.labels_values.values()))
# plt.show()

## Maladie gencive
# ax = plt.subplot()
# mal_gencives = Boxplot(
#     "Part des participants pensant avoir une maladie parodontale", ax
# )
# mal_gencives.set_labels_values_from_df(
#     dataframe,
#     "Mal. Gencive",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# mal_gencives.plot_it()
# print("Maladie gencives :", mal_gencives.labels_values)
# print(sum(mal_gencives.labels_values.values()))
# plt.show()

## Dents et gencive
# ax = plt.subplot()
# dent_gencives = Boxplot("Évaluation de la santé parodontale par les participants", ax)
# dent_gencives.set_labels_values_from_df(
#     dataframe,
#     "Santé D & gcive",
#     {
#         1: "Ne sais pas",
#         2: "Excellente",
#         3: "Très bonne",
#         4: "Bonne",
#         5: "Moyenne",
#         6: "Mauvaise",
#     },
# )
# dent_gencives.plot_it()
# print("Santé dent et gencives:", dent_gencives.labels_values)
# print(sum(dent_gencives.labels_values.values()))
# plt.show()

## Traitement maladie gencives
# ax = plt.subplot()
# traitement_gencives = Boxplot(
#     "Part des participants ayant déjà eu un traitement parodontal", ax
# )
# traitement_gencives.set_labels_values_from_df(
#     dataframe,
#     "TTT Mal. Gcive",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# traitement_gencives.plot_it()
# print("Traitement gencives:", traitement_gencives.labels_values)
# print(sum(traitement_gencives.labels_values.values()))
# plt.show()

## Dent mobiles
# ax = plt.subplot()
# dent_mobile = Boxplot(
#     "Part des participants ayant déjà eu une mobilité spontanée d’une dent", ax
# )
# dent_mobile.set_labels_values_from_df(
#     dataframe,
#     "D mobile",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# dent_mobile.plot_it()
# print("Dent mobile:", dent_mobile.labels_values)
# print(sum(dent_mobile.labels_values.values()))
# plt.show()

# ## Perte os
# ax = plt.subplot()
# perte_os = Boxplot(
#     "Part des participants ayant déjà été alertés d’une perte d’os\npar leur dentiste",
#     ax,
# )
# perte_os.set_labels_values_from_df(
#     dataframe,
#     "Perte Os",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# perte_os.plot_it()
# print("Dent mobile:", perte_os.labels_values)
# print(sum(perte_os.labels_values.values()))
# plt.show()

## Chose anormale
# ax = plt.subplot()
# anormal = Boxplot(
#     "Part des participants ayant remarqué une anomalie\nbucco-dentaire au cours des 3 derniers mois",
#     ax,
# )
# anormal.set_labels_values_from_df(
#     dataframe,
#     "Chose aN",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# anormal.plot_it()
# print("Anormal:", anormal.labels_values)
# print(sum(anormal.labels_values.values()))
# plt.show()

# ## Nbr nettoyage
# ax = plt.subplot()
# nbr_nettoyage = Boxplot(
#     "Nombre de nettoyages interdentaires réalisés par\nles participants au cours des 7 derniers jours",
#     ax,
# )
# nbr_nettoyage.set_labels_values_from_df(
#     dataframe,
#     "Nbre Nettoyage entre D",
#     {
#         1: "Ne sais pas",
#         2: "0 nettoyage",
#         3: "1 nettoyage",
#         4: "2 nettoyages",
#         5: "3 nettoyages",
#         6: "4 nettoyages",
#         7: "5 nettoyages",
#         8: "6 nettoyages",
#         9: "7 nettoyages",
#     },
# )
# nbr_nettoyage.plot_it()
# print("Nbr nettoyage:", nbr_nettoyage.labels_values)
# print(sum(nbr_nettoyage.labels_values.values()))
# plt.show()


## Nbr bdb
# ax = plt.subplot()
# nbr_bdb = Boxplot(
#     "Nombre de bains de bouche réalisés par\nles participants au cours des 7 derniers jours",
#     ax,
# )
# nbr_bdb.set_labels_values_from_df(
#     dataframe,
#     "Nbre B de bouche",
#     {
#         1: "Ne sais pas",
#         2: "0 bain de\nbouche",
#         3: "1 bain de\nbouche",
#         4: "2 bains de\nbouche",
#         5: "3 bains de\nbouche",
#         6: "4 bains de\nbouche",
#         7: "5 bains de\nbouche",
#         8: "6 bains de\nbouche",
#         9: "7 bains de\nbouche",
#     },
# )
# nbr_bdb.plot_it()
# print("Nbr bdb:", nbr_bdb.labels_values)
# print(sum(nbr_bdb.labels_values.values()))
# plt.show()

## Bourrage
# ax = plt.subplot()
# bourrage = Boxplot(
#     "Part des participants présentant un bourrage alimentaire",
#     ax,
# )
# bourrage.set_labels_values_from_df(
#     dataframe,
#     "Bourrage",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# bourrage.plot_it()
# print("Bourrage:", bourrage.labels_values)
# print(sum(bourrage.labels_values.values()))
# plt.show()

# ## Déchaussement
# ax = plt.subplot()
# dechaussement = Boxplot(
#     "Part des participants ayant remarqué un déchaussement de leurs dents",
#     ax,
# )
# dechaussement.set_labels_values_from_df(
#     dataframe,
#     "Déchaussement",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# dechaussement.plot_it()
# print("Déchaussement:", dechaussement.labels_values)
# print(sum(dechaussement.labels_values.values()))
# plt.show()

# # Rétraction
# ax = plt.subplot()
# retraction = Boxplot(
#     "Part des participants ayant remarqué une rétraction de leur gencive",
#     ax,
# )
# retraction.set_labels_values_from_df(
#     dataframe,
#     "Rétraction",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Oui",
#     },
# )
# retraction.plot_it()
# print("Rétraction:", retraction.labels_values)
# print(sum(retraction.labels_values.values()))
# plt.show()

# ## Saignement
# ax = plt.subplot()
# saignement = Boxplot(
#     "Part des participants souffrant de saignement gingival",
#     ax,
# )
# saignement.set_labels_values_from_df(
#     dataframe,
#     "Saignement",
#     {
#         1: "Ne sais pas",
#         2: "Non",
#         3: "Au brossage",
#         4: "Spontanément",
#     },
# )
# saignement.plot_it()
# print("Saignement:", saignement.labels_values)
# print(sum(saignement.labels_values.values()))
# plt.show()

## Freq saignement
# ax = plt.subplot()
# freq_saignement = Boxplot(
#     "Fréquence de saignement chez les participants\nsouffrant de saignement gingival",
#     ax,
# )
# freq_saignement.set_labels_values_from_df(
#     dataframe,
#     "Fréq. Saignement",
#     {
#         1: "Ne sais pas",
#         -1: "Pas de\nsaignement",
#         2: "1 fois/mois",
#         3: "1 fois/semaine",
#         4: "> 1 fois/semaine",
#     },
# )
# freq_saignement.plot_it()
# print("Freq saignement:", freq_saignement.labels_values)
# print(sum(freq_saignement.labels_values.values()))
# plt.show()
