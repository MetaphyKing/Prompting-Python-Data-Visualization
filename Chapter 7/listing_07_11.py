from matplotlib.animation import PillowWriter, FFMpegWriter

# Suppose you already have ani
# GIF:
ani.save("demo.gif", writer=PillowWriter(fps=25))

# MP4 (requires FFmpeg):
writer = FFMpegWriter(fps=30, codec="libx264", bitrate=1800,
                      metadata={"artist": "Author"})
ani.save("demo.mp4", writer=writer, dpi=150)
