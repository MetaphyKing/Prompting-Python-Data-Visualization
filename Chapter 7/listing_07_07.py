# Example with a generator (flexible, can “stream”)
def frame_gen():
    for i in range(1, len(x) + 1):
        yield i  # number of points to show (see update above)

ani = FuncAnimation(
    fig, update,
    frames=frame_gen,
    init_func=init,
    blit=True,
    save_count=len(x),            # helps when saving; avoids generator-related warnings
    cache_frame_data=False        # make caching behavior explicit (Matplotlib may disable it anyway)
)
