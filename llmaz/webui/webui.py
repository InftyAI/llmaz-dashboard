# TODO: Using logging once ready
# import logging

import gradio as gr

from llmlite.apis import ChatMessage


def predict(message, history, system_prompt):
    # TODO: Support loading models
    # chat = ChatLLM(model_name_or_path="TODO")
    messages = []
    for i in range(0, len(history)):
        messages.append(ChatMessage(role="user", content=history[i][0]))
        messages.append(ChatMessage(role="assistant", content=history[i][1]))

    messages.append(ChatMessage(role="user", content=message))

    # TODO: https://github.com/InftyAI/llmlite/issues/31
    if system_prompt != "":
        messages = [ChatMessage(role="system", content=system_prompt)] + messages

    print("messages: ", messages)
    return messages[-1].content + "-this-is-a-fake-message"
    # return chat.completion(messages=messages)


board = gr.ChatInterface(
    predict,
    additional_inputs=[
        gr.Textbox("You are a helpful AI.", label="System Prompt"),
    ],
)

if __name__ == "__main__":
    board.queue().launch()
