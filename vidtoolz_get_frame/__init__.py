import vidtoolz
import moviepy as mpy
import numpy as np
import os


def get_and_save_frames(fname, num=10, outdir=None, times=None):
    """
    Extract frames from a video file.

    Parameters:
        fname (str): Path to the video file.
        num (int): Number of random frames to extract (ignored if `times` is provided).
        outdir (str): Directory to save the extracted frames.
        times (list): Specific times (in seconds) to extract frames. Overrides `num`.
    """
    vid = mpy.VideoFileClip(fname, audio=False)
    dur = vid.duration

    if times:
        sec = sorted([t for t in times if 0 <= t <= dur])
    else:
        sec = sorted(np.random.randint(0, int(dur), size=num))

    if outdir and not os.path.exists(outdir):
        os.makedirs(outdir)

    for i, t in enumerate(sec, 1):
        frame_name = f"{i}_frame_{t:.2f}.png"
        if outdir:
            frame_name = os.path.join(outdir, frame_name)
        vid.save_frame(frame_name, t)
    vid.close()


def create_parser(subparser):
    parser = subparser.add_parser(
        "getframe", description="Get frame out of a video for thumbnail"
    )
    # Add subprser arguments here.
    parser.add_argument(
        "fname", type=str, help="MOV Mp4 file from which frames has to be extracted"
    )
    parser.add_argument(
        "-n", "--num", type=int, default=10, help="No of frames to collect"
    )
    parser.add_argument("-o", "--outdir", type=str, default=None, help="Output dir")
    parser.add_argument(
        "-t",
        "--times",
        type=float,
        nargs="*",
        help="Specific times in seconds to extract frames.",
    )
    return parser


class ViztoolzPlugin:
    """Get frame out of a video for thumbnail"""

    __name__ = "getframe"

    @vidtoolz.hookimpl
    def register_commands(self, subparser):
        self.parser = create_parser(subparser)
        self.parser.set_defaults(func=self.run)
    
    def run(self, args):
        get_and_save_frames(args.fname, num=args.num, outdir=args.outdir, times=args.times)

    def hello(self, args):
        # this routine will be called when "vidtoolz "getframe is called."
        print("Hello! This is an example ``vidtoolz`` plugin.")


getframe_plugin = ViztoolzPlugin()
