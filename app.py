import google.generativeai as genai
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import scrolledtext, END
from tkinter import ttk

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure AI model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

# GUI Setup
root = tk.Tk()
root.title("Zakyouse's Gemini Chatbot")
root.geometry("650x520")
root.configure(bg="#252525")  # Light background

# Style setup
style = ttk.Style()
style.theme_use("clam")  # Use 'clam' for more modern look

style.configure("TEntry", padding=(10, 12), font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12), padding=6)

# Chat history display
chat_display = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, font=("Segoe UI", 12), bg="#c3c3c3", relief=tk.FLAT, bd=0
)
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_display.insert(END, "🤖 Gemini Chat is ready!\n\n")
chat_display.config(state='disabled')

# Input field frame
input_frame = tk.Frame(root, bg="#f0f2f5")
input_frame.pack(fill=tk.X, padx=10, pady=5)

# Input field
input_field = ttk.Entry(input_frame, style="TEntry")
input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

# Send button
send_button = ttk.Button(input_frame, text="Send", command=lambda: send_message())
send_button.pack(side=tk.RIGHT)

# Send message function
def send_message(event=None):
    user_input = input_field.get()
    if not user_input.strip():
        return

    chat_display.config(state='normal')
    chat_display.insert(END, f"You: {user_input}\n")
    input_field.delete(0, END)

    try:
        response = chat.send_message(user_input)
        chat_display.insert(END, f"Gemini: {response.text}\n\n")
    except Exception as e:
        chat_display.insert(END, f"⚠️ Error: {e}\n\n")

    chat_display.config(state='disabled')
    chat_display.see(END)

# Bind Enter key
input_field.bind("<Return>", send_message)

# Run the app
root.mainloop()
