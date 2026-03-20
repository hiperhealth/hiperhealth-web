"""Simple registry for NLP pipelines used by hiperhealth-web."""

from __future__ import annotations

from threading import Lock
from typing import Callable


class BasePipeline:
    """Base interface for NLP pipelines."""

    name: str
    initialized: bool

    def initialize(self) -> None:
        """Initialize the pipeline resources."""
        raise NotImplementedError

    def process(self, text: str) -> list[str]:
        """Process input text and return token strings."""
        raise NotImplementedError

    def shutdown(self) -> None:
        """Release resources and reset state."""
        raise NotImplementedError

    def health_check(self) -> bool:
        """Return True when pipeline is healthy and ready."""
        raise NotImplementedError


_PIPELINE_FACTORIES: dict[str, Callable[[], BasePipeline]] = {}
_REGISTRY_LOCK = Lock()

PipelineFactory = Callable[[], BasePipeline]
PipelineDecorator = Callable[[PipelineFactory], PipelineFactory]


def register_pipeline(name: str) -> PipelineDecorator:
    """Register a pipeline factory under a unique name."""

    def _decorator(factory: PipelineFactory) -> PipelineFactory:
        with _REGISTRY_LOCK:
            _PIPELINE_FACTORIES[name] = factory
        return factory

    return _decorator


def get_pipeline(name: str) -> BasePipeline:
    """Return a new pipeline instance by name."""
    with _REGISTRY_LOCK:
        factory = _PIPELINE_FACTORIES.get(name)
    if factory is None:
        msg = f'Pipeline not registered: {name}'
        raise KeyError(msg)
    return factory()
