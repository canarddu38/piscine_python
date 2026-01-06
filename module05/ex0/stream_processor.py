#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """
    Abstract base class defining a common interface for all data processors.

    Subclasses must implement data validation and processing logic while
    sharing a consistent interface for polymorphic behavior.
    """

    def __init__(self, silent: bool = False) -> None:
        """
        Initialize the data processor.

        :param silent: If True, suppress processing output messages.
        """
        self.silent = silent

    def print_processing(self, data: Any) -> None:
        """
        Print the data currently being processed if not in silent mode.

        :param data: The data being processed.
        """
        if not self.silent:
            print(f"Processing data: {data}")

    @abstractmethod
    def process(self, data: Any) -> str:
        """
        Process the given data and return a formatted result string.

        :param data: Input data to process.
        :return: Result of processing as a string.
        """
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """
        Validate whether the given data is suitable for this processor.

        :param data: Input data to validate.
        :return: True if valid, False otherwise.
        """
        pass

    def format_output(self, result: str) -> str:
        """
        Format the processed result for output.

        :param result: Raw processing result string.
        :return: Formatted output string.
        """
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    """
    Processor for numeric data collections.

    Handles lists of integers and computes summary statistics.
    """

    def __init__(self, silent: bool = False) -> None:
        """
        Initialize the numeric processor.

        :param silent: If True, suppress processing output messages.
        """
        super().__init__(silent)
        if not silent:
            print("Initializing Numeric Processor...")

    def process(self, data: Any) -> str:
        """
        Process numeric data by computing count, sum, and average.

        :param data: List of integers to process.
        :return: Summary string of numeric processing.
        :raises Exception: If data is invalid.
        """
        try:
            self.print_processing(data)
            s = sum(data)
            list_size = len(data)
            return (
                f"Processed {list_size} numeric values, "
                f"sum={s}, avg={int(100 * s / list_size) / 100}"
            )
        except Exception:
            raise Exception("Data is not an array of int")

    def validate(self, data: Any) -> bool:
        """
        Validate that the data is a list of integers.

        :param data: Data to validate.
        :return: True if valid numeric list, False otherwise.
        """
        if type(data) is not list:
            return False
        for elem in data:
            if type(elem) is not int:
                return False
        return True


class TextProcessor(DataProcessor):
    """
    Processor for textual data.

    Computes character and word counts for strings.
    """

    def __init__(self, silent: bool = False) -> None:
        """
        Initialize the text processor.

        :param silent: If True, suppress processing output messages.
        """
        super().__init__(silent)
        if not silent:
            print("Initializing Text Processor...")

    def process(self, data: Any) -> str:
        """
        Process text data by counting characters and words.

        :param data: String to process.
        :return: Summary string of text processing.
        """
        self.print_processing(f"\"{data}\"")
        characters = 0
        words = 1
        for char in data:
            characters += 1
            if char == ' ':
                words += 1
        return (
            f"Processed text: {characters} characters, {words} words"
        )

    def validate(self, data: Any) -> bool:
        """
        Validate that the data is a string.

        :param data: Data to validate.
        :return: True if valid string, False otherwise.
        """
        return type(data) is str


class LogProcessor(DataProcessor):
    """
    Processor for log entries.

    Detects log level and formats log messages accordingly.
    """

    def __init__(self, silent: bool = False):
        """
        Initialize the log processor.

        :param silent: If True, suppress processing output messages.
        """
        super().__init__(silent)
        if not silent:
            print("Initializing Log Processor...")

    def process(self, data: Any) -> str:
        """
        Process a log entry by identifying its severity level.

        :param data: Log message string.
        :return: Processed log message.
        """
        self.print_processing(f"\"{data}\"")
        if type(data) is str:
            return (
                data.replace("ERROR:", "ERROR level detected:")
                    .replace("INFO:", "INFO level detected:")
            )
        return f"Invalid log: {data}"

    def validate(self, data: Any) -> bool:
        """
        Validate that the data is a supported log entry.

        :param data: Data to validate.
        :return: True if valid log entry, False otherwise.
        """
        return (
            type(data) is str and
            ("ERROR:" in data or "INFO:" in data)
        )

    def format_output(self, result: str) -> str:
        """
        Format log output with severity indicator.

        :param result: Processed log message.
        :return: Formatted log output string.
        """
        log_type = "INFO"
        if "ERROR" in result:
            log_type = "ALERT"
        return f"Output: [{log_type}] {result}"


def main():
    """
    Entry point demonstrating polymorphic data processing.

    Initializes different processors, validates input data, processes
    it, and displays formatted output using a shared interface.
    """
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        num = NumericProcessor()
        num_data = [1, 2, 3, 4, 5]
        if (num.validate(num_data)):
            num_result = num.process(num_data)
            print("Validation: Numeric data verified")
        else:
            print("Validation: Numeric data not verified")
        print(num.format_output(num_result))
        print()
    except Exception as e:
        print(f"An error occurred: {e.args[0]}")

    try:
        text = TextProcessor()
        text_data = "Hello Nexus World"
        if (text.validate(text_data)):
            text_result = text.process(text_data)
            print("Validation: Text data verified")
        else:
            print("Validation: Text data not verified")
        print(text.format_output(text_result))
        print()
    except Exception as e:
        print(f"An error occurred: {e.args[0]}")

    try:
        log = LogProcessor()
        log_data = "ERROR: Connection timeout"
        if (log.validate(log_data)):
            log_result = log.process(log_data)
            print("Validation: Log entry verified")
        else:
            print("Validation: Log entry not verified")
        print(log.format_output(log_result))
        print()
    except Exception as e:
        print(f"An error occurred: {e.args[0]}")

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [
        NumericProcessor(True),
        TextProcessor(True),
        LogProcessor(True)
    ]
    processors_data = [
        [1, 2, 3],
        "abcde abcdef",
        "INFO: System ready"
    ]
    i = 0
    for (processor, data) in zip(processors, processors_data):
        try:
            output = processor.format_output(processor.process(data))
            print(f"Result {i+1}: {output}")
            i += 1
        except Exception as e:
            print(f"An error occurred: {e.args[0]}")

    print()
    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
