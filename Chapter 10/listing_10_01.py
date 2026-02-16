import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(context="notebook", style="whitegrid")

penguins = sns.load_dataset("penguins").dropna(subset=["body_mass_g", "species"])
tips = sns.load_dataset("tips").dropna(subset=["total_bill", "time"])
