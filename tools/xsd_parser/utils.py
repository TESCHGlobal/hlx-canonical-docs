"""Utility functions for XSD parsing."""
import re

from .constants import ns, logger

_BARE_URL_PATTERN = re.compile(r"(?<!\]\()(https?://[^\s\)\]>,]+)")
_MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]*\]\((https?://[^)]+)\)")


def linkify_urls(text: str) -> str:
    """Convert bare URLs in text to markdown links using the URL as link text."""
    if not isinstance(text, str) or not text or text == "–":
        return text

    placeholders: dict[str, str] = {}

    def _preserve_existing_link(match: re.Match[str]) -> str:
        key = f"__MDLINK_{len(placeholders)}__"
        placeholders[key] = match.group(0)
        return key

    protected = _MARKDOWN_LINK_PATTERN.sub(_preserve_existing_link, text)

    def _linkify(match: re.Match[str]) -> str:
        url = match.group(1).rstrip(".,;:")
        trailing = match.group(1)[len(url):]
        return f"[{url}]({url}){trailing}"

    linked = _BARE_URL_PATTERN.sub(_linkify, protected)

    for key, value in placeholders.items():
        linked = linked.replace(key, value)

    return linked


def get_documentation(elem):
    """Extract documentation from element annotation."""
    try:
        annotation = elem.find("xs:annotation/xs:documentation", ns)
        if annotation is not None and annotation.text:
            return ' '.join(annotation.text.strip().split())
    except Exception as e:
        logger.debug(f"Error extracting documentation: {e}")
    return "–"

