"""Basic spaCy-backed pipeline adapter for the NLP registry."""

from typing import Any

from hiperhealth.nlp.registry import BasePipeline, register_pipeline


class SpacyBasicPipeline(BasePipeline):
	"""Tokenize text using a configurable spaCy model."""

	def __init__(self, model_name: str = "en_core_web_sm") -> None:
		self.name = "spacy_basic"
		self._model_name = model_name
		self._nlp: Any = None
		self.initialized = False

	def initialize(self) -> None:
		"""Load spaCy model lazily and mark pipeline initialized."""
		if self._nlp is not None:
			self.initialized = True
			return

		import spacy

		self._nlp = spacy.load(self._model_name)
		self.initialized = True

	def process(self, text: str) -> list[str]:
		"""Tokenize input text into a list of token strings."""
		if self._nlp is None:
			self.initialize()
		doc = self._nlp(text)
		return [token.text for token in doc]

	def shutdown(self) -> None:
		"""Release model resources and reset initialization state."""
		self._nlp = None
		self.initialized = False

	def health_check(self) -> bool:
		"""Return True when the spaCy model is currently loaded."""
		return self._nlp is not None


@register_pipeline("spacy_basic")
def _make_spacy_basic() -> SpacyBasicPipeline:
	return SpacyBasicPipeline()
