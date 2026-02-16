# file: guard.py
import ast, re

ALLOWED_IMPORTS = {"pandas", "matplotlib", "matplotlib.pyplot", "seaborn", "numpy"}
FORBIDDEN_CALLS = {("os", "system"), ("subprocess", None), ("requests", None)}

def lint_code(py: str) -> list[str]:
    issues = []
    try:
        tree = ast.parse(py)
    except SyntaxError as e:
        return [f"Syntax error: {e}"]

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                if n.name not in ALLOWED_IMPORTS:
                    issues.append(f"Forbidden import: {n.name}")
        if isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            name = f"{mod}.{node.names[0].name}" if node.names else mod
            if mod not in ALLOWED_IMPORTS and name not in ALLOWED_IMPORTS:
                issues.append(f"Forbidden import: {mod}")
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            mod = getattr(getattr(node.func, 'value', None), 'id', None)
            fn = node.func.attr
            if (mod, fn) in FORBIDDEN_CALLS or (mod, None) in FORBIDDEN_CALLS:
                issues.append(f"Forbidden call: {mod}.{fn}")

    required = ["plt.title(", "plt.xlabel(", "plt.ylabel(", "plt.savefig("]
    for tok in required:
        if tok not in py:
            issues.append(f"Missing required element: {tok}")
    if not re.search(r"plt\.savefig\([\"']artifacts\/", py):
        issues.append("Output must be saved under artifacts/ directory")
    return issues
