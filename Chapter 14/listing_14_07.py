import warnings

# Safer: local scope only
with warnings.catch_warnings():
    warnings.simplefilter("error")
    # run a small, targeted block that you are actively debugging
    # e.g., a single plotting call or a transformation step
    result = build_plot(df)
import warnings

with warnings.catch_warnings():
    warnings.filterwarnings("error", category=DeprecationWarning)
    build_plot(df)
