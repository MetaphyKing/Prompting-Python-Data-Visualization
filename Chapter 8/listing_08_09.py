from src.production_style import use_production_style
from src.utils.save import save_with_provenance
from src.utils.provenance import snapshot_environment

use_production_style()
snapshot_environment("figures/_provenance/env_snapshot.json")

# build figure...
meta = {
    "author": "Aleksei",
    "subject": "Chapter 1",
    "data_version": "sha256:7a9e…",
    "rc_profile": "production_style@1.3"
}
save_with_provenance(fig, "ch08/ch08_fig_02_sine", meta)
