import torch


class Chatbot:
    def __init__(self, model_name_or_path, task, **kwargs) -> None:
        # self.__chat = ChatLLM(model_name_or_path=model_name_or_path, task=task)
        pass

    def completion(self, messages) -> str:
        """
        Chat completion.
        """
        return "self.chat.completion(messages=messages)"
        return self.__chat.completion(messages=messages)

    def torch_gc(self) -> None:
        """
        Reclaim GPU memory.
        """
        #  FIXME: will this lead to memory leakage?
        self.__chat = None
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
