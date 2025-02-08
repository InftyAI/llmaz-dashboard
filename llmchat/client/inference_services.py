from dataclasses import dataclass


@dataclass(frozen=True)
class InferenceService:
    name: str
    namespace: str
    model_family_name: str
    model_name: str
