from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol
import time


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        return {"input": data}


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            return {k: str(v).upper() for k, v in data.items()}
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        return f"OUTPUT -> {data}"


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        self.stats: Dict[str, Any] = {
            "runs": 0,
            "errors": 0,
            "last_duration": None,
        }

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def _run_stages(self, data: Any) -> Any:
        for stage in self.stages:
            data = stage.process(data)
        return data

    @abstractmethod
    def process(self, data: Any) -> Any:
        ...


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        start = time.time()
        try:
            result = self._run_stages(data)
            self.stats["runs"] += 1
            return f"[JSON:{self.pipeline_id}] {result}"
        except Exception as e:
            self.stats["errors"] += 1
            return f"[JSON:{self.pipeline_id}] ERROR: {e}"
        finally:
            self.stats["last_duration"] = time.time() - start


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        start = time.time()
        try:
            result = self._run_stages(data)
            self.stats["runs"] += 1
            return f"[CSV:{self.pipeline_id}] {result}"
        except Exception as e:
            self.stats["errors"] += 1
            return f"[CSV:{self.pipeline_id}] ERROR: {e}"
        finally:
            self.stats["last_duration"] = time.time() - start


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        start = time.time()
        try:
            result = self._run_stages(data)
            self.stats["runs"] += 1
            print(f"[STREAM:{self.pipeline_id}] {result}")
            return result
        except Exception as e:
            self.stats["errors"] += 1
            print(f"[STREAM:{self.pipeline_id}] ERROR: {e}")
            return None
        finally:
            self.stats["last_duration"] = time.time() - start


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process(self, data: Any) -> Any:
        result = data
        for pipeline in self.pipelines:
            result = pipeline.process(result)
        return result

    def stats(self) -> List[Dict[str, Any]]:
        return [p.stats for p in self.pipelines]


if __name__ == "__main__":
    input_stage = InputStage()
    transform_stage = TransformStage()
    output_stage = OutputStage()

    json_pipeline = JSONAdapter("A")
    json_pipeline.add_stage(input_stage)
    json_pipeline.add_stage(transform_stage)

    csv_pipeline = CSVAdapter("B")
    csv_pipeline.add_stage(transform_stage)
    csv_pipeline.add_stage(output_stage)

    stream_pipeline = StreamAdapter("C")
    stream_pipeline.add_stage(output_stage)

    nexus = NexusManager()
    nexus.add_pipeline(json_pipeline)
    nexus.add_pipeline(csv_pipeline)
    nexus.add_pipeline(stream_pipeline)

    final_result = nexus.process("enterprise data stream")
    print("FINAL RESULT:", final_result)
    print("STATS:", nexus.stats())
