from console.serve.chatbot import Chatbot


class Serve:
    def __init__(self) -> None:
        self.__model = None

    def preload_model(self, model_name_or_path, task, temperature, stream) -> None:
        # TODO: Because gradio can not maintain state like page refresh, so we'll not offload model here.
        # See https://github.com/gradio-app/gradio/issues/3106.
        # So if user wants to load a different model, he/she should offload the model first.
        if self.__model is not None:
            return

        self.__model = Chatbot(
            model_name_or_path=model_name_or_path,
            task=task,
            temperature=temperature,
            stream=stream,
        )

    def offload_model(self) -> None:
        if self.__model is None:
            return

        self.__model.torch_gc()
        self.__model = None

    def completion(self, messages) -> str:
        if self.__model is None:
            raise Exception("No model preloaded")
        return self.__model.completion(messages)
