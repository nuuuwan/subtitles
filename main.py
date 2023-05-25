from utils import SECONDS_IN, TIME_FORMAT_TIME, File, Time


def format_timestamp(t_sec):
    m = int(t_sec / SECONDS_IN.MINUTE)
    s = int(t_sec % SECONDS_IN.MINUTE)
    ms = int((t_sec - int(t_sec)) * 1000)
    return f'00:{m:02d}:{s:02d}.{ms:03d}'


def main():
    VIDEO_LENGTH_SEC = 30
    START_TIME = TIME_FORMAT_TIME.parse('2023-05-25 05:15:00')
    END_TIME = TIME_FORMAT_TIME.parse('2023-05-25 06:15:00')
    SUBTITLES_PER_SEC = 10

    lines = ['WEBVTT', '']

    DT = (
        (END_TIME.ut - START_TIME.ut)
        * 1.0
        / (VIDEO_LENGTH_SEC * SUBTITLES_PER_SEC)
    )

    for i in range(VIDEO_LENGTH_SEC):
        for j in range(SUBTITLES_PER_SEC):
            ut = START_TIME.ut + DT * (i * SUBTITLES_PER_SEC + j)
            caption = TIME_FORMAT_TIME.stringify(Time(ut))

            t_sec = i + j * 1.0 / SUBTITLES_PER_SEC
            ts_caption_start = format_timestamp(t_sec)
            ts_caption_end = format_timestamp(t_sec + 1.0 / SUBTITLES_PER_SEC)

            lines.append(f'{ts_caption_start} --> {ts_caption_end}')
            lines.append(caption)
            lines.append('')

    File('subtitles.vtt').write('\n'.join(lines))


if __name__ == '__main__':
    main()
