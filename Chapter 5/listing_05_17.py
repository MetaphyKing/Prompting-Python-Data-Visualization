import matplotlib.pyplot as plt
plt.style.use(["reporting", "brand_overrides.mplstyle"])



with plt.style.context(["slides"]):
    fig, ax = plt.subplots(figsize=(8.0, 4.5))
    ax.plot(df.index, df["A"], label="A")
    ax.plot(df.index, df["B"], linestyle="--", label="B")
    ax.set_title("Temporary use of 'slides' style", loc="left")
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0))
    plt.tight_layout(); plt.show()
# outside the block, settings are restored

