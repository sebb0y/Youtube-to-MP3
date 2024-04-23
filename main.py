import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_mp3():
    url = youtube_link_entry.get()
    if url:
        try:
            yt = YouTube(url)
            title = yt.title
            artist = yt.author
            print(f"Downloading {title} by {artist}")
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(filename=f"{title} ({artist}).mp3")
            print("Download complete.")
            status_label.config(text="Finished Downloading.. Enjoy your MP3!")
            messagebox.showinfo("Success", "MP3 file downloaded successfully!\nCredit to Sebb0y")
        except KeyError:
            messagebox.showerror("Error", "This video may not be available.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a YouTube link.")

root = tk.Tk()
root.title("YouTube to MP3 Converter")

# YouTube Link Entry
youtube_link_label = tk.Label(root, text="YouTube Link:")
youtube_link_label.grid(row=0, column=0)
youtube_link_entry = tk.Entry(root, width=50)
youtube_link_entry.grid(row=0, column=1, padx=10, pady=5)

# Download Button
download_button = tk.Button(root, text="Download MP3", command=download_mp3)
download_button.grid(row=1, columnspan=2, pady=10)

status_label = tk.Label(root, text="")
status_label.grid(row=2, columnspan=2, pady=5)

root.mainloop()
