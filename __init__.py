"""
CellGraph — Reactive computational graph engine for Python.

Licensed under AGPL-3.0-or-later.
Copyright (C) 2026 CellGraph Contributors.

Usage:
    >>> from cellgraph import CellGraph
    >>> g = CellGraph("demo")
    >>> price = g.cell("price", value=100.0)
    >>> tax = g.cell("tax_rate", value=0.2)
    >>> @g.computed("total", depends_on=["price", "tax_rate"])
    ... def total(p, t):
    ...     return p * (1 + t)
    >>> g["total"].value
    120.0
"""

from __future__ import annotations

__version__: str = "0.1.0"
__license__: str = "AGPL-3.0-or-later"
__all__: list[str] = [
    "CellGraph",
    "CellError",
    "CycleDetectedError",
    "CellNotFoundError",
    "ValidationError",
]

from cellgraph.core.graph import CellGraph
from cellgraph.exceptions import (
    CellError,
    CellNotFoundError,
    CycleDetectedError,
    ValidationError,
)


def _check_runtime() -> None:
    """Enforce minimum Python version at import time."""
    import sys

    if sys.version_info < (3, 11):
        raise RuntimeError(
            f"CellGraph requires Python >=3.11, got {sys.version_info.major}.{sys.version_info.minor}"
        )


_check_runtime()
