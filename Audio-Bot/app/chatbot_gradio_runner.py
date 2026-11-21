"""Script to run the gradio as code"""

import gradio as gr
from genai_voice.bots.chatbot import ChatBot
from genai_voice.logger.log_utils import log, LogLevels


# poetry run RunChatBotScript
def run():
    """Run Chatbot app"""
    chatbot = ChatBot(enable_speakers=False, threaded=False)
    history = []

    # Updated to use Blocks for better control flow (Audio -> Text -> Edit -> Submit)
    def transcribe(audio):
        """Transcribe audio to text"""
        if not audio:
            return ""
        prompt = chatbot.get_prompt_from_gradio_audio(audio)
        log(f"Transcribed prompt: {prompt}", log_level=LogLevels.ON)
        return prompt

    def get_response(text_input):
        """Get Response from Text Input and generate audio for browser playback"""
        if not text_input or not text_input.strip():
            return "Please enter some text.", None
            
        log(f"Processing prompt: {text_input}", log_level=LogLevels.ON)
        response = chatbot.respond(text_input, history)
        history.append([text_input, response])
        audio_file = chatbot.audio.text_to_audio_file(response)
        return response, audio_file

    with gr.Blocks(title="Wanderwise Travel Assistant") as demo:
        gr.Markdown("# Wanderwise Travel Assistant")
        
        with gr.Row():
            # Audio Input
            audio_input = gr.Audio(sources=["microphone"], type="numpy", label="Speak")
            
            # Text Input (Editable)
            text_input = gr.Textbox(label="Your Request (Edit if needed)", placeholder="Type or record audio...", lines=3)
            
        submit_btn = gr.Button("Submit", variant="primary")
        
        with gr.Row():
            output = gr.Textbox(label="Response", interactive=False)
            audio_output = gr.Audio(label="Voice Response (Browser Playback)", autoplay=True, interactive=False)
        
        # Events
        # 1. When recording stops, transcribe and fill the text box
        audio_input.stop_recording(fn=transcribe, inputs=audio_input, outputs=text_input)
        
        # 2. When submit is clicked, send text to bot and send audio to browser
        submit_btn.click(fn=get_response, inputs=text_input, outputs=[output, audio_output])
        
        # 3. Allow pressing Enter on text box to submit
        text_input.submit(fn=get_response, inputs=text_input, outputs=[output, audio_output])

    demo.launch()


# poetry run RunChatBotScript
def run_with_file_support():
    """Run Chatbot app and save files to disk"""
    chatbot = ChatBot(enable_speakers=False, threaded=False)
    history = []

    def get_response_from_file(file):
        prompt = chatbot.get_prompt_from_file(file)
        response = chatbot.respond(prompt, history)
        history.append([prompt, response])
        audio_file = chatbot.audio.text_to_audio_file(response)
        return response, audio_file

    # Approach that doesn't have the warning but uses temp files
    demo = gr.Interface(
        get_response_from_file,
        gr.Audio(sources="microphone", type="filepath"),
        ["text", gr.Audio(label="Voice Response (Browser Playback)", autoplay=True)],
    )
    demo.launch()
