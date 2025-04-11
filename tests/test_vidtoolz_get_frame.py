import pytest
import vidtoolz_get_frame as w

from argparse import ArgumentParser

import pytest
from moviepy import ColorClip
import os


def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(["hello.mp4"])
    assert result.fname == "hello.mp4"
    assert result.num == 10
    assert result.outdir is None
    assert result.times is None


def test_plugin(capsys):
    w.getframe_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``vidtoolz`` plugin." in captured.out


# Helper to create a dummy video file
@pytest.fixture(scope="module")
def dummy_video(tmp_path_factory):
    tmpdir = tmp_path_factory.mktemp("videos")
    video_path = os.path.join(tmpdir, "test_video.mp4")

    # Create a 5-second video, 640x480, red screen
    clip = ColorClip(size=(640, 480), color=(255, 0, 0), duration=5)
    clip.write_videofile(video_path, fps=24, codec="libx264", audio=False, logger=None)
    return video_path


def test_random_frames_extraction(tmp_path, dummy_video):
    outdir = tmp_path / "frames_random"
    w.get_and_save_frames(fname=dummy_video, num=5, outdir=str(outdir))

    files = list(outdir.glob("*.png"))
    assert len(files) == 5
    for file in files:
        assert file.exists()


def test_specific_times_extraction(tmp_path, dummy_video):
    outdir = tmp_path / "frames_times"
    times = [0.5, 1.0, 2.5, 3.7]
    w.get_and_save_frames(fname=dummy_video, times=times, outdir=str(outdir))

    files = list(outdir.glob("*.png"))
    assert len(files) == len(times)
    for file in files:
        assert file.exists()


def test_no_outdir_creates_frames(tmp_path, dummy_video):
    current_files = set(os.listdir())
    w.get_and_save_frames(fname=dummy_video, num=3, outdir=None)

    # Check new files in CWD
    new_files = set(os.listdir()) - current_files
    pngs = [f for f in new_files if f.endswith(".png")]
    assert len(pngs) == 3

    # Cleanup
    for f in pngs:
        os.remove(f)


def test_invalid_times_ignored(tmp_path, dummy_video):
    outdir = tmp_path / "frames_invalid"
    times = [-1, 0.5, 10, 1.2]  # -1 and 10 should be ignored (video is 5s)
    w.get_and_save_frames(fname=dummy_video, times=times, outdir=str(outdir))

    files = list(outdir.glob("*.png"))
    assert len(files) == 2  # only 0.5 and 1.2 are valid
