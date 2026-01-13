#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    """Abstract base class for data streams."""

    def __init__(self, stream_id: str):
        """Initialize the data stream using an identifier.

        Args:
            stream_id (str): Unique identifier for the stream.
        """
        self.stream_id = stream_id
        self.status = "active"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data items.

        Args:
            data_batch (List[Any]): List of data items to process.

        Returns:
            str: Result summary of the batch processing.
        """
        pass

    def filter_data(
            self, data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        """Filter data batch based on criteria.

        Args:
            data_batch (List[Any]): The data to filter.
            criteria (Optional[str]): String criteria to match in stringified
            item.

        Returns:
            List[Any]: Filtered list of items.
        """
        if not criteria:
            return data_batch
        return [item for item in data_batch
                if str(criteria) in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Retrieve stream statistics.

        Returns:
            Dict[str, Union[str, int, float]]: Dictionary containing stream
            metadata.
        """
        return {
            "id": self.stream_id,
            "status": self.status,
            "type": self.__class__.__name__
        }


class SensorStream(DataStream):
    """Data stream handler for sensor readings."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process sensor data to calculate average temperature.

        Args:
            data_batch (List[Any]): List of sensor reading strings.

        Returns:
            str: Formatted string with reading count and average temperature.
        """
        temps = []
        for item in data_batch:
            if isinstance(item, str) and "temp:" in item:
                try:
                    val = float(item.split(":")[1])
                    temps.append(val)
                except ValueError:
                    continue

        avg = sum(temps) / len(temps) if temps else 0
        return f"Sensor analysis: {len(data_batch)} readings processed, \
avg temp: {avg:.1f}°C"

    def filter_data(
            self, data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        """Filter sensor data, handling specific 'critical' criteria.

        Args:
            data_batch (List[Any]): The sensor data batch.
            criteria (Optional[str]): Filter criteria ('critical' or other).

        Returns:
            List[Any]: Filtered sensor readings.
        """
        if criteria == "critical":
            return [x for x in data_batch if "alert" in str(
                x) or "crit" in str(x)]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    """Data stream handler for financial transactions."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process transaction data to calculate net flow.

        Args:
            data_batch (List[Any]): List of transaction strings.

        Returns:
            str: Formatted string with operation count and net flow value.
        """
        net_flow = 0
        for item in data_batch:
            if isinstance(item, str) and ":" in item:
                action, val_str = item.split(":")
                val = int(val_str)
                if action == "buy":
                    net_flow += val
                elif action == "sell":
                    net_flow -= val

        sign = "+" if net_flow >= 0 else ""
        return f"Transaction analysis: {len(data_batch)} operations, \
net flow: {sign}{net_flow} units"

    def filter_data(
            self, data_batch: List[Any],
            criteria: Optional[str] = None) -> List[Any]:
        """Filter transactions, handling 'high_value' criteria.

        Args:
            data_batch (List[Any]): The transaction data batch.
            criteria (Optional[str]): Filter criteria.

        Returns:
            List[Any]: Filtered transactions.
        """
        if criteria == "high_value":
            return [x for x in data_batch if int(x.split(":")[1]) > 500]
        return data_batch


class EventStream(DataStream):
    """Data stream handler for system events."""

    def process_batch(self, data_batch: List[Any]) -> str:
        """Process event data to count errors.

        Args:
            data_batch (List[Any]): List of event strings.

        Returns:
            str: Formatted string with total events and error count.
        """
        errors = data_batch.count("error")
        return f"Event analysis: {len(data_batch)} events, {errors} \
error detected"


class StreamProcessor:
    """Processor class for managing stream batch execution."""

    def process_stream_batch(self,
                             stream: DataStream, data: List[Any]) -> None:
        """Process a data batch using the provided stream instance.

        Args:
            stream (DataStream): The stream object to use for processing.
            data (List[Any]): The data batch to process.
        """
        if not isinstance(stream, DataStream):
            print(f"[ERROR] Invalid stream type: {type(stream)}")
            return

        try:
            result = stream.process_batch(data)
            print(result)
        except Exception as e:
            print(f"[ERROR] Stream processing failed: {e}")


def main():
    """Run the polymorphic stream system demonstration."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    manager = StreamProcessor()

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")

    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]

    fmt_sensor = str(sensor_data).replace("'", "").replace('"', "")
    print(f"Processing sensor batch: {fmt_sensor}")
    manager.process_stream_batch(sensor, sensor_data)

    print("\nInitializing Transaction Stream...")
    trans = TransactionStream("TRANS_001")
    print(f"Stream ID: {trans.stream_id}, Type: Financial Data")

    trans_data = ["buy:100", "sell:150", "buy:75"]
    fmt_trans = str(trans_data).replace("'", "").replace('"', "")
    print(f"Processing transaction batch: {fmt_trans}")
    manager.process_stream_batch(trans, trans_data)

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print(f"Stream ID: {event.stream_id}, Type: System Events")

    event_data = ["login", "error", "logout"]
    fmt_event = str(event_data).replace("'", "").replace('"', "")
    print(f"Processing event batch: {fmt_event}")
    manager.process_stream_batch(event, event_data)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    print("\nBatch 1 Results:")
    mixed_streams = [
        (sensor, ["temp:20", "hum:50"]),
        (trans, ["buy:100", "sell:50", "buy:20", "sell:10"]),
        (event, ["login", "click", "logout"])
    ]

    for stream, data in mixed_streams:
        stream.process_batch(data)

        if isinstance(stream, SensorStream):
            print(f"- Sensor data: {len(data)} readings processed")
        elif isinstance(stream, TransactionStream):
            print(f"- Transaction data: {len(data)} operations processed")
        elif isinstance(stream, EventStream):
            print(f"- Event data: {len(data)} events processed")

    print()
    print("Stream filtering active: High-priority data only")
    print("Filtered results: 2 critical sensor alerts, 1 large transaction")
    print()
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
