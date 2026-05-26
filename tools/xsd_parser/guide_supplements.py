"""Guide-specific supplement loading for generated documentation.

This module allows injecting small amounts of hardcoded, guide-specific
documentation content (for example, Clinical guide prose) into the markdown
generated from XSD files.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml


@dataclass(frozen=True)
class TocExtra:
    title: str
    anchor: str
    before: str


@dataclass(frozen=True)
class GuideSupplementSection:
    id: str
    file: str
    inject_into: Optional[str] = None
    before: Optional[str] = None
    body: str = ""


def _repo_root() -> Path:
    # tools/xsd_parser/guide_supplements.py -> tools/xsd_parser -> tools -> repo root
    return Path(__file__).resolve().parents[2]


def _supplements_dir() -> Path:
    return _repo_root() / "tools" / "guide_supplements"


def _manifest_path() -> Path:
    return _supplements_dir() / "manifest.yaml"


def load_guide_supplements(schema_stem: str) -> Dict[str, Any]:
    """Load guide supplements for a specific schema stem.

    Args:
        schema_stem: XSD filename stem (for example, "Clinical_V4.2").

    Returns:
        Dict with keys:
          - toc_extras: list[TocExtra]
          - interoperability_append: str
          - before_required_elements_sections: list[GuideSupplementSection]
    """
    manifest_path = _manifest_path()
    if not manifest_path.exists():
        return {
            "toc_extras": [],
            "interoperability_append": "",
            "before_required_elements_sections": [],
        }

    with manifest_path.open("r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f) or {}

    schema_cfg = (manifest or {}).get(schema_stem, {}) or {}
    toc_extras_cfg = schema_cfg.get("toc_extras", []) or []
    sections_cfg = schema_cfg.get("sections", []) or []

    toc_extras: List[TocExtra] = []
    for item in toc_extras_cfg:
        if not isinstance(item, dict):
            continue
        title = item.get("title")
        anchor = item.get("anchor")
        before = item.get("before", "")
        if not title or not anchor:
            continue
        toc_extras.append(TocExtra(title=str(title), anchor=str(anchor), before=str(before)))

    guides_dir = _supplements_dir()
    interoperability_parts: List[str] = []
    before_required_sections: List[GuideSupplementSection] = []

    for sec in sections_cfg:
        if not isinstance(sec, dict):
            continue

        sec_id = sec.get("id")
        file_rel = sec.get("file")
        inject_into = sec.get("inject_into")
        before = sec.get("before")

        if not sec_id or not file_rel:
            continue

        body_path = guides_dir / str(file_rel)
        if not body_path.exists():
            # Fail soft: generation should still work even if supplements are missing.
            continue

        body = body_path.read_text(encoding="utf-8")
        section = GuideSupplementSection(
            id=str(sec_id),
            file=str(file_rel),
            inject_into=str(inject_into) if inject_into else None,
            before=str(before) if before else None,
            body=body,
        )

        if section.inject_into == "interoperability":
            interoperability_parts.append(section.body)
        elif section.before == "required-elements":
            before_required_sections.append(section)

    return {
        "toc_extras": [{"title": t.title, "anchor": t.anchor, "before": t.before} for t in toc_extras],
        "interoperability_append": "\n\n".join([p.strip() for p in interoperability_parts if p.strip()]),
        "before_required_elements_sections": before_required_sections,
    }

