import gradio as gr

from .chat_model import chat

def build_app():

	return gr.ChatInterface(
		fn= chat
	)

def main():
	build_app().launch(inbrowser=True)

if __name__ == "___main__":
	main()