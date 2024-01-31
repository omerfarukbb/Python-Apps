import ttkbootstrap as ttk
from tkinter import filedialog
from downloader import YoutubeVideoDownloader

def main():

    video_downloader = None

    def create_video_downloader():
        global video_downloader
        video_url = ent_url.get()
        try:
            video_downloader = YoutubeVideoDownloader(video_url)
            video_resolutions = video_downloader.resolutions
            combobox_resolutions.config(values=video_resolutions)
            lbl_status.config(text="Video information loaded successfully!", foreground="green")
        except:
            lbl_status.config(text=f"An error occured!", foreground="red")

    def download():
        if video_downloader:
            resolution = combobox_resolutions.get()
            if resolution:
                try:
                    file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4"), ("All files", "*.*")])
                    if file_path:
                        flag = video_downloader.download_video(resolution, file_path)
                        if flag:
                            lbl_status.config(text="Download successful!", foreground="green")
                        else:
                            lbl_status.config(text="Download canceled!", foreground="red")
                    else:
                        lbl_status.config(text="Download canceled!", foreground="red")
                except:
                    lbl_status.config(text=f"An error occured during download!", foreground="red")
            else:
                lbl_status.config(text="Please select a resolution!", foreground="red")
        else:
            lbl_status.config(text="Please enter a valid url!", foreground="red")

    root = ttk.Window(themename='superhero')
    root.geometry('600x400')
    root.resizable(False, False)
    root.iconbitmap('yt_downloader.ico')
    root.title('Youtube Downloader')

    # general design
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=3)
    root.rowconfigure(2, weight=3)
    root.columnconfigure(0, weight=1)

    lbl_title = ttk.Label(root, anchor='center', text='Welcome to YouTube Downloader', font=('Calibri', 20))
    frm_input = ttk.Frame(root)
    frm_output = ttk.Frame(root)

    # widgets
    ent_url = ttk.Entry(frm_input, width=35)
    btn_search = ttk.Button(frm_input, text='Search', command=create_video_downloader)

    resolution = ttk.StringVar()
    combobox_resolutions = ttk.Combobox(frm_output, textvariable=resolution, width=12)
    btn_download = ttk.Button(frm_output, text='Download', command=download)

    lbl_status = ttk.Label(root, text='', font=('Calibri', 12))

    # layout
    lbl_title.grid(row=0, column=0, sticky='nsew')
    frm_input.grid(row=1, column=0)
    frm_output.grid(row=2, column=0)
    lbl_status.grid(row=3, column=0, pady=10)

    ent_url.pack(side='left', padx=5)
    btn_search.pack(side='left')

    combobox_resolutions.pack(side='left', padx=5)
    btn_download.pack(side='left')


    root.mainloop()

if __name__ == '__main__':
    main()
