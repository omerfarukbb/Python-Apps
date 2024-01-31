from pytube import YouTube

class YoutubeVideoDownloader:
    def __init__(self, video_url):
        self.yt = YouTube(video_url)
        self.video_streams = self.yt.streams
        self.resolutions = [str(s)+'p' for s in sorted(set(int(stream.resolution[0:-1]) for stream in self.video_streams if stream.resolution))]

    def download_video(self, resolution, output_path):
        try: 
            video_stream = self.video_streams.get_by_resolution(resolution=resolution)
            video_stream.download(output_path)
            return True
        except:
            return False

