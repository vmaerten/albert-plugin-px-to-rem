"""
Albert plugin to convert PX to REM and vice versa.

Usage:
    px 16      -> converts 16px to rem (1rem with base 16)
    px 1.5rem  -> converts 1.5rem to px (24px with base 16)
    px 32 10   -> converts 32px to rem with base 10 (3.2rem)
"""

import re
from albert import (
    Action,
    PluginInstance,
    StandardItem,
    TriggerQueryHandler,
    Query,
    setClipboardText,
    makeThemeIcon,
)

md_iid = "4.0"
md_version = "1.0"
md_name = "PX to REM Converter"
md_description = "Convert pixels to rem units and vice versa"
md_license = "MIT"
md_url = "https://github.com/valentin/albert-plugin-px-to-rem"
md_authors = ["@valentin"]

DEFAULT_BASE = 16


class Plugin(PluginInstance, TriggerQueryHandler):
    def __init__(self):
        PluginInstance.__init__(self)
        TriggerQueryHandler.__init__(self)

    def id(self):
        return "px-to-rem"

    def name(self):
        return md_name

    def description(self):
        return md_description

    def defaultTrigger(self):
        return "px "

    def synopsis(self, query):
        return "<value> [base]"

    def handleTriggerQuery(self, query: Query):
        query_str = query.string.strip()

        if not query_str:
            query.add(
                StandardItem(
                    id="px-to-rem-help",
                    text="PX ↔ REM Converter",
                    subtext="Enter a value like '16' or '16px' or '1rem' [base]",
                    icon_factory=lambda: makeThemeIcon("accessories-calculator"),
                )
            )
            return

        parts = query_str.split()
        value_str = parts[0]
        base = DEFAULT_BASE

        if len(parts) > 1:
            try:
                base = float(parts[1])
            except ValueError:
                query.add(
                    StandardItem(
                        id="px-to-rem-error",
                        text="Invalid base value",
                        subtext=f"'{parts[1]}' is not a valid number",
                        icon_factory=lambda: makeThemeIcon("dialog-error"),
                    )
                )
                return

        px_match = re.match(r"^([\d.]+)\s*px$", value_str, re.IGNORECASE)
        rem_match = re.match(r"^([\d.]+)\s*rem$", value_str, re.IGNORECASE)
        number_match = re.match(r"^([\d.]+)$", value_str)

        if rem_match:
            value = float(rem_match.group(1))
            result_px = value * base
            result_px_str = f"{result_px:.4g}px"

            query.add(
                StandardItem(
                    id="px-to-rem-result",
                    text=result_px_str,
                    subtext=f"{value}rem → {result_px_str} (base: {base}px)",
                    icon_factory=lambda: makeThemeIcon("accessories-calculator"),
                    actions=[
                        Action(
                            id="copy",
                            text="Copy to clipboard",
                            callable=lambda r=result_px_str: setClipboardText(r),
                        ),
                        Action(
                            id="copy_number",
                            text="Copy number only",
                            callable=lambda r=result_px: setClipboardText(f"{r:.4g}"),
                        ),
                    ],
                )
            )
        elif px_match or number_match:
            match = px_match or number_match
            value = float(match.group(1))
            result_rem = value / base
            result_rem_str = f"{result_rem:.4g}rem"

            query.add(
                StandardItem(
                    id="px-to-rem-result",
                    text=result_rem_str,
                    subtext=f"{value}px → {result_rem_str} (base: {base}px)",
                    icon_factory=lambda: makeThemeIcon("accessories-calculator"),
                    actions=[
                        Action(
                            id="copy",
                            text="Copy to clipboard",
                            callable=lambda r=result_rem_str: setClipboardText(r),
                        ),
                        Action(
                            id="copy_number",
                            text="Copy number only",
                            callable=lambda r=result_rem: setClipboardText(f"{r:.4g}"),
                        ),
                    ],
                )
            )
        else:
            query.add(
                StandardItem(
                    id="px-to-rem-invalid",
                    text="Invalid input",
                    subtext="Enter a number, '16px', or '1rem'",
                    icon_factory=lambda: makeThemeIcon("dialog-error"),
                )
            )
