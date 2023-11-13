from llmaz.serves.chatbot import Chatbot


class Serve:
    def __init__(self) -> None:
        self.__model = None

    def preload_model(self, model_name_or_path, task, temperature, stream) -> None:
        if self.__model is not None:
            self.offload_model()

        self.__model = Chatbot(
            model_name_or_path=model_name_or_path,
            task=task,
            temperature=temperature,
            stream=stream,
        )

    def offload_model(self) -> None:
        if self.__model is not None:
            self.__model.torch_gc()
            self.__model = None

    def completion(self, messages) -> str:
        if self.__model is None:
            raise Exception("No model preloaded")
        return self.__model.completion(messages)
