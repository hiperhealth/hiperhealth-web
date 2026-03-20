"""Tests for the optional spaCy NLP adapter registration and lifecycle."""

import importlib

import pytest

pytest.importorskip('spacy')


def test_spacy_basic_pipeline_registration_and_lazy_init():
    """Ensure registration occurs and initialization is lazy."""
    importlib.import_module('hiperhealth_web.nlp.pipelines.spacy_basic')
    from hiperhealth_web.nlp import get_pipeline

    pipeline = get_pipeline('spacy_basic')
    assert not pipeline.initialized

    tokens = pipeline.process('Hello world, this is spaCy.')
    assert pipeline.initialized is True
    assert isinstance(tokens, list)
    assert any(token.lower() == 'hello' for token in tokens)


def test_spacy_basic_health_check():
    """Verify health status transitions after first processing call."""
    importlib.import_module('hiperhealth_web.nlp.pipelines.spacy_basic')
    from hiperhealth_web.nlp import get_pipeline

    pipeline = get_pipeline('spacy_basic')
    assert pipeline.health_check() is False

    pipeline.process('Checking health.')
    assert pipeline.health_check() is True
