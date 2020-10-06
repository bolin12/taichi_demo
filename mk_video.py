import taichi as ti

ti.init()

pixels = ti.var(ti.u8, shape=(1920, 960))

@ti.kernel
def paint():
    for i, j, k in pixels:
        pixels[i, j] = ti.random() * 255

result_dir = "./mp4_folder"
video_manager = ti.VideoManager(output_dir=result_dir, framerate=60, automatic_build=False)

for i in range(400):
    paint()

    pixels_img = pixels.to_numpy()
    video_manager.write_frame(pixels_img)
    print(f'\rFrame {i+1}/50 is recorded', end='')

print()
print('Exporting .mp4 and .gif videos...')
video_manager.make_video(gif=True, mp4=True)
print(f'MP4 video is saved to {video_manager.get_output_filename(".mp4")}')
print(f'GIF video is saved to {video_manager.get_output_filename(".gif")}')