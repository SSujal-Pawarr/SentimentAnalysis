import tkinter as tk
from tkinter import ttk
from textblob import TextBlob


#  Function to analyze sentiment
def analyze_sentiment():
    text = text_entry.get("1.0", tk.END).strip()  # Get text from textbox
    if not text:
        result_label.config(text=" Please enter some text!", foreground="orange")
        return

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        result = "Positive 😊"
        color = "green"
    elif polarity == 0:
        result = "Neutral 😐"
        color = "blue"
    else:
        result = "Negative 😞"
        color = "red"

    result_label.config(
        text=f"Sentiment: {result}\nPolarity Score: {polarity:.2f}",
        foreground=color
    )
    status.set(f"Text analyzed | Words: {len(text.split())}") #count words


#  Function to clear text and reset
def clear_text():
    text_entry.delete("1.0", tk.END) #delete start to end
    result_label.config(text="Sentiment: ", foreground="black")
    status.set("Cleared | Ready")


#  Fullscreen toggle functions
def toggle_fullscreen(event=None):
    state = not root.attributes("-fullscreen")
    root.attributes("-fullscreen", state)


def exit_fullscreen(event=None):
    root.attributes("-fullscreen", False)


#  Root window setup
root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("800x500")
root.minsize(600, 400)
root.configure(bg="#f4f6f9")

#  Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Arial", 12), padding=6)
style.configure("TLabel", font=("Arial", 12), background="#f4f6f9")

#  Title Label
title_label = ttk.Label(
    root,
    text="📝 Sentiment Analyzer",
    font=("Arial", 20, "bold"),
    background="#f4f6f9"
)
title_label.pack(pady=15)

#  Input Frame
input_frame = ttk.Frame(root, padding=10)
input_frame.pack(fill="x", padx=20, pady=10)

ttk.Label(input_frame, text="Enter your text below:").pack(anchor="w")

text_entry = tk.Text(
    input_frame,
    height=5,
    font=("Arial", 12),
    wrap="word",
    relief="solid",
    borderwidth=1
)
text_entry.pack(fill="x", pady=8)

#  Buttons Frame
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=5)

analyze_button = ttk.Button(btn_frame, text="Analyze", command=analyze_sentiment)
analyze_button.grid(row=0, column=0, padx=10)

clear_button = ttk.Button(btn_frame, text="Clear", command=clear_text)
clear_button.grid(row=0, column=1, padx=10)

#  Result Section
result_label = ttk.Label(root, text="Sentiment: ", font=("Arial", 16, "bold"))
result_label.pack(pady=20)

#  Status Bar
status = tk.StringVar()
status.set("Ready")

status_bar = ttk.Label(root, textvariable=status, relief="sunken", anchor="w")
status_bar.pack(side="bottom", fill="x")

#  Fullscreen key bindings
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_fullscreen)

#  Run the app
root.mainloop()
