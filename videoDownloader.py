# For Future Dorian: Usage -- Put YouTube url into line 12
# Convert the saved MP4 to MP3
# Save to iCloud Drive
# Sync to Spotify on phone
# QED

from pytube import YouTube

def printStreamsIn(stream):
    for i in stream:
        print(i)

# Put link in the quotes
# test = YouTube("https://www.youtube.com/watch?v=odVTDeSU42Y")
# test = YouTube("https://www.youtube.com/watch?v=LSIOcCcEVaE")
test = YouTube(" ")

print("Title: ", test.title)
print("Views: ", test.views)

# CURRENTLY - audio only mode
to_download = test.streams.get_audio_only()

to_download.download("C:\\Users\\dory\\Desktop", "test.mp4")

print("Download Complete!")
