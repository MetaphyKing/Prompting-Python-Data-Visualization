import seaborn as sns
sns.set_theme(
    palette="colorblind"  # safe default palette for the entire session
)


import seaborn as sns
import matplotlib.pyplot as plt

with sns.color_palette("pastel"):
    sns.histplot([1,2,2,3,3,3,4,4,5])
    plt.show()
# Outside the block, the palette returns to global defaults.
