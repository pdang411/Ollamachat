
#import os
import gradio as gr
import openai
import ollama

from openai import OpenAI

client = OpenAI(base_url="http://192.168.1.14:11434/v1", api_key="not-needed")

def get_local_models():
    try:
        models = client.models.list().data
        return [m.id for m in models]
    except Exception as e:
        return ["Error loading models"]


def chat_with_model(model_name, user_message, history):
    if history is None:
        history = []
    # Ensure history is a list of dicts with 'role' and 'content'
    history = [msg for msg in history if isinstance(msg, dict) and "role" in msg and "content" in msg]
    # Add the new user message
    history.append({"role": "user", "content": user_message})
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=history,
            temperature=0.7
        )
        reply = response.choices[0].message.content
        history.append({"role": "assistant", "content": reply})
        return history, history
    except Exception as e:
        history.append({"role": "assistant", "content": f"Error: {str(e)}"})
        return history, history

model_list = get_local_models()

with gr.Blocks() as demo:
    gr.Markdown("# 💬 Ollama Chat Interface")
    model_dropdown = gr.Dropdown(choices=model_list, label="Choose Model", value=model_list[0])
    chatbot = gr.Chatbot(label="Chat History", type="messages")
    msg = gr.Textbox(label="Your Message", lines=4, max_lines=20)
    submit_btn = gr.Button("Send")
    clear_btn = gr.Button("Clear Chat")

    history_state = gr.State([])

    submit_btn.click(
        chat_with_model,
        inputs=[model_dropdown, msg, history_state],
        outputs=[chatbot, history_state]
    )

    clear_btn.click(lambda: ([], []), None, [chatbot, history_state])



demo.launch(server_name="0.0.0.0",server_port=8383,debug=True)
