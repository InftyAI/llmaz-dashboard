from console.serve.serve import Serve


class Engine:
    def __init__(self) -> None:
        self.serve = Serve()
        self.__model_loaded = False

    def model_loaded(self) -> bool:
        return self.__model_loaded

    def preload_model(self, model_name_or_path, task, temperature, stream) -> None:
        if model_name_or_path is None or model_name_or_path == "":
            raise Exception("no model_name_or_path provided")

        self.serve.preload_model(model_name_or_path, task, temperature, stream)
        self.__model_loaded = True

    def offload_model(self) -> None:
        self.serve.offload_model()
        self.__model_loaded = False
