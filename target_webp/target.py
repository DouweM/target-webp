from __future__ import annotations

"""webp target class."""

from singer_sdk import typing as th
from singer_sdk.target_base import Target

from target_webp.sinks import (
    WebpSink,
)


class TargetWebp(Target):
    """Sample target for webp."""

    name = "target-webp"

    config_jsonschema = th.PropertiesList(
        # TODO: Add output dir
    ).to_dict()

    default_sink_class = WebpSink


if __name__ == "__main__":
    TargetWebp.cli()
