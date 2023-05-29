from __future__ import annotations
import base64
from datetime import datetime
from pathlib import Path

"""webp target sink class, which handles writing streams."""

from singer_sdk.sinks import RecordSink


class WebpSink(RecordSink):
    """webp target sink class."""

    def process_record(self, record: dict, context: dict) -> None:
        """Process the record.

        Args:
            record: Individual record in the stream.
            context: Stream partition or context dictionary.
        """
        # Sample:
        # ------
        # client.write(record)  # noqa: ERA001

        if "image_data" not in record:
            raise ValueError("No image data found in record")

        image_data = record.get("image_data", "")
        image_data = base64.b64decode(image_data.encode("utf-8"))

        installation_id = record.get("installation_id")
        timestamp = datetime.now().isoformat(timespec="seconds")

        image_path = Path(f"output/{installation_id}/{timestamp}.webp")
        image_path.parent.mkdir(parents=True, exist_ok=True)

        image_path.write_bytes(image_data)

        self.logger.info("Created WEBP image", image_path)
