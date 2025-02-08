from llmchat.webui.webui import launch_webui

if __name__ == "__main__":
    webui = launch_webui()
    webui.queue().launch()
