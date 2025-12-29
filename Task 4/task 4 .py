import gradio as gr
from deep_translator import GoogleTranslator

# --- 1. Backend Logic ---
def translate_text(text, target_lang):
    if not text or len(text.strip()) == 0:
        return ""
    try:
        translator = GoogleTranslator(source="auto", target=target_lang)
        return translator.translate(text)
    except Exception as e:
        return f"❌ Error: {str(e)}"

# --- 2. Custom CSS ---
custom_css = """
#header { 
    text-align: center; 
    padding: 1.5rem; 
    background: linear-gradient(90deg, #3b82f6, #8b5cf6);
    border-radius: 12px;
    margin-bottom: 20px;
    color: white;
}
.input-card, .output-card {
    border-radius: 12px !important;
}
"""

# --- 3. UI Construction ---
# Note: theme and css moved to demo.launch() for Gradio 6.0 compatibility
with gr.Blocks(title="Aryan's AI Translator") as demo:
    
    with gr.Column(elem_id="header"):
        gr.Markdown("# 🚀 Aryan's Neural Translator")
        gr.Markdown("### Professional Language Processing Interface")

    with gr.Row():
        # Left Panel
        with gr.Column():
            source_input = gr.Textbox(
                label="Source Text",
                placeholder="Enter text here...",
                lines=8,
                elem_classes="input-card"
            )
            
            target_lang = gr.Dropdown(
                label="Target Language",
                choices=[
                    ("Spanish", "es"), ("French", "fr"), ("German", "de"), 
                    ("Hindi", "hi"), ("Gujarati", "gu"), ("Japanese", "ja")
                ],
                value="es"
            )

        # Right Panel
        with gr.Column():
            output_display = gr.Textbox(
                label="Translation Result",
                lines=8,
                interactive=False,
                elem_classes="output-card"
            )
            
            with gr.Row():
                clear_btn = gr.Button("🗑️ Clear")
                manual_btn = gr.Button("✨ Translate", variant="primary")

    # Interaction Logic
    manual_btn.click(
        fn=translate_text, 
        inputs=[source_input, target_lang], 
        outputs=output_display
    )
    
    clear_btn.click(lambda: ["", ""], None, [source_input, output_display])

    gr.Markdown(
        "<div style='text-align: center; padding: 20px; color: grey;'>"
        "Developed by <b>Aryan Patel</b> | CodeAlpha Internship 2025"
        "</div>"
    )

# --- 4. Run App ---
if __name__ == "__main__":
    # Pass theme and css here to avoid the UserWarning
    demo.launch(
        theme=gr.themes.Soft(primary_hue="blue"),
        css=custom_css
    )