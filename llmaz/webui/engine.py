from llmaz.serves.serve import Serve


class Engine:
    def __init__(self) -> None:
        self.__serve = Serve()

    def preload_model(self, model_name_or_path, task, temperature, stream) -> None:
        self.__serve.preload_model(model_name_or_path, task, temperature, stream)

    def offload_model(self) -> None:
        self.__serve.offload_model()

    def completion(self, messages) -> str:
        return self.__serve.completion(messages)
