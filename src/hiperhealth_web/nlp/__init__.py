"""NLP pipeline registry API for hiperhealth-web."""

from hiperhealth_web.nlp.registry import (
    BasePipeline,
    get_pipeline,
    register_pipeline,
)

__all__ = [
    'BasePipeline',
    'get_pipeline',
    'register_pipeline',
]
