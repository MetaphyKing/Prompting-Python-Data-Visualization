def step_generate_code_with_fallback(design: DesignSpec, data_path: str) -> str:
    seaborn_variant = f"""
import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
df = pd.read_csv("{data_path}")
plt.figure(figsize=({design.image["figsize"][0]}, {design.image["figsize"][1]}))
sns.lineplot(data=df, x="{design.x}", y="{design.y}")
plt.title("{design.title}"); plt.xlabel("{design.xlabel}"); plt.ylabel("{design.ylabel}")
plt.tight_layout(); plt.savefig("{design.image["path"]}", dpi={design.image["dpi"]})
"""
    matplotlib_variant = f"""
import pandas as pd, matplotlib.pyplot as plt
df = pd.read_csv("{data_path}")
plt.figure(figsize=({design.image["figsize"][0]}, {design.image["figsize"][1]}))
plt.plot(df["{design.x}"], df["{design.y}"])
plt.title("{design.title}"); plt.xlabel("{design.xlabel}"); plt.ylabel("{design.ylabel}")
plt.tight_layout(); plt.savefig("{design.image["path"]}", dpi={design.image["dpi"]})
"""
    return seaborn_variant or matplotlib_variant
