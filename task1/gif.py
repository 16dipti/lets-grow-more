import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

class GIFCreatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GIF Creator")

        # Variables
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.start_time = tk.StringVar(value="0")
        self.end_time = tk.StringVar()
        self.fps = tk.StringVar(value="10")

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Input Video
        tk.Label(self.root, text="Input Video:").grid(row=0, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.input_path, width=40).grid(row=0, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_input).grid(row=0, column=2)

        # Output GIF
        tk.Label(self.root, text="Output GIF:").grid(row=1, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.output_path, width=40).grid(row=1, column=1)
        tk.Button(self.root, text="Browse", command=self.browse_output).grid(row=1, column=2)

        # Start Time
        tk.Label(self.root, text="Start Time (sec):").grid(row=2, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.start_time).grid(row=2, column=1)

        # End Time
        tk.Label(self.root, text="End Time (sec):").grid(row=3, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.end_time).grid(row=3, column=1)

        # FPS
        tk.Label(self.root, text="Frames Per Second:").grid(row=4, column=0, sticky=tk.W)
        tk.Entry(self.root, textvariable=self.fps).grid(row=4, column=1)

        # Create GIF Button
        tk.Button(self.root, text="Create GIF", command=self.create_gif).grid(row=5, column=0, columnspan=3)

    def browse_input(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mkv")])
        if file_path:
            self.input_path.set(file_path)

    def browse_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".gif", filetypes=[("GIF Files", "*.gif")])
        if file_path:
            self.output_path.set(file_path)

    def create_gif(self):
        input_path = self.input_path.get()
        output_path = self.output_path.get()
        start_time = float(self.start_time.get())
        end_time = float(self.end_time.get()) if self.end_time.get() else None
        fps = int(self.fps.get())

        try:
            create_gif(input_path, output_path, start_time, end_time, fps)
            tk.messagebox.showinfo("Success", "GIF creation completed successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

def create_gif(video_path, output_path, start_time=0, end_time=None, fps=10):
    video_clip = VideoFileClip(video_path)
    if end_time is not None:
        video_clip = video_clip.subclip(start_time, end_time)
    video_clip = video_clip.set_fps(fps)
    video_clip.write_gif(output_path)
    video_clip.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = GIFCreatorApp(root)
    root.mainloop()
