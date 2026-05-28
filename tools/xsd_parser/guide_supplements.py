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
    title: str
    file: str
    inject_into: Optional[str] = None
    replace: Optional[str] = None
    after: Optional[str] = None
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
          - toc_extras: list[dict]
          - after_interoperability_sections: list[GuideSupplementSection]
          - before_required_elements_sections: list[GuideSupplementSection]
    """
    manifest_path = _manifest_path()
    if not manifest_path.exists():
        return {
            "toc_extras": [],
            "after_interoperability_sections": [],
            "before_required_elements_sections": [],
            "member_identification_override": None,
            "adds_updates_and_deletes_override": None,
            "after_member_identification_sections": [],
            "after_submission_frequency_sections": [],
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
    after_interoperability_sections: List[GuideSupplementSection] = []
    before_required_sections: List[GuideSupplementSection] = []
    member_identification_override: Optional[GuideSupplementSection] = None
    adds_updates_and_deletes_override: Optional[GuideSupplementSection] = None
    after_member_identification_sections: List[GuideSupplementSection] = []
    after_submission_frequency_sections: List[GuideSupplementSection] = []

    for sec in sections_cfg:
        if not isinstance(sec, dict):
            continue

        sec_id = sec.get("id")
        file_rel = sec.get("file")
        title = sec.get("title") or sec_id
        inject_into = sec.get("inject_into")
        replace = sec.get("replace")
        after = sec.get("after")
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
            title=str(title),
            file=str(file_rel),
            inject_into=str(inject_into) if inject_into else None,
            replace=str(replace) if replace else None,
            after=str(after) if after else None,
            before=str(before) if before else None,
            body=body,
        )

        if section.replace == "member-identification":
            member_identification_override = section
        elif section.replace == "adds-updates-and-deletes":
            adds_updates_and_deletes_override = section
        elif section.after == "interoperability":
            after_interoperability_sections.append(section)
        elif section.after == "member-identification":
            after_member_identification_sections.append(section)
        elif section.after == "submission-frequency":
            after_submission_frequency_sections.append(section)
        elif section.before == "required-elements":
            before_required_sections.append(section)

    toc_extras_out = [
        {"title": t.title, "anchor": t.anchor, "before": t.before}
        for t in toc_extras
    ]
    for section in after_interoperability_sections:
        toc_extras_out.append({
            "title": section.title,
            "anchor": section.id,
            "before": "change-log",
        })
    for section in before_required_sections:
        toc_extras_out.append({
            "title": section.title,
            "anchor": section.id,
            "before": "required-elements",
        })
    for section in after_member_identification_sections:
        toc_extras_out.append({
            "title": section.title,
            "anchor": section.id,
            "after": "member-identification",
        })
    for section in after_submission_frequency_sections:
        toc_extras_out.append({
            "title": section.title,
            "anchor": section.id,
            "after": "submission-frequency",
        })

    return {
        "toc_extras": toc_extras_out,
        "after_interoperability_sections": after_interoperability_sections,
        "before_required_elements_sections": before_required_sections,
        "member_identification_override": member_identification_override,
        "adds_updates_and_deletes_override": adds_updates_and_deletes_override,
        "after_member_identification_sections": after_member_identification_sections,
        "after_submission_frequency_sections": after_submission_frequency_sections,
    }

