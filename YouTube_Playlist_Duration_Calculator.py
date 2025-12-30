import yt_dlp
from datetime import timedelta
import math

# ------------------ Helpers ------------------

def format_duration(seconds):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)

    if h > 0:
        return f"{h}h {m}m {s}s"
    else:
        return f"{m}m {s}s"


def get_playlist_data_with_videos(playlist_url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "extract_flat": True,
        "force_ipv4": True,
        "socket_timeout": 30,
        "nocheckcertificate": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(playlist_url, download=False)

    playlist_name = info.get("title", "Unknown Playlist")
    entries = info.get("entries", [])

    videos = []

    for idx, video in enumerate(entries, start=1):
        if video and video.get("duration"):
            videos.append({
                "index": idx,
                "duration": video["duration"]
            })

    if not videos:
        raise Exception("No valid videos found")

    total_duration = sum(v["duration"] for v in videos)

    return {
        "name": playlist_name,
        "videos": videos,
        "count": len(videos),
        "total": total_duration
    }

# ------------------ Modes ------------------

def length_calculation_mode():
    url = input("\nPaste playlist link: ").strip()

    try:
        data = get_playlist_data_with_videos(url)
    except Exception as e:
        print("\n❌ Error:", e)
        return

    durations = [v["duration"] for v in data["videos"]]

    print("\n📌 Playlist Name:", data["name"])
    print("🎥 Total Videos:", data["count"])
    print("⏱ Total Duration:", format_duration(data["total"]))
    print("📊 Avg Video Duration:", format_duration(data["total"] / data["count"]))
    print("⬆ Longest Video:", format_duration(max(durations)))
    print("⬇ Shortest Video:", format_duration(min(durations)))


def course_comparison_mode():
    url_a = input("\nPaste Course A playlist link: ").strip()
    url_b = input("Paste Course B playlist link: ").strip()

    try:
        a = get_playlist_data_with_videos(url_a)
        b = get_playlist_data_with_videos(url_b)
    except Exception as e:
        print("\n❌ Error:", e)
        return

    print(f"\nCourse A: {a['name']} → {format_duration(a['total'])}")
    print(f"Course B: {b['name']} → {format_duration(b['total'])}")

    diff = abs(a["total"] - b["total"])

    if a["total"] > b["total"]:
        print(f"\n🏆 Winner: {b['name']} is shorter by {format_duration(diff)}")
    elif b["total"] > a["total"]:
        print(f"\n🏆 Winner: {a['name']} is shorter by {format_duration(diff)}")
    else:
        print("\n🤝 Both courses have same duration")


def study_plan_mode():
    url = input("\nPaste playlist link: ").strip()
    days = int(input("How many days do you have? ").strip())

    try:
        data = get_playlist_data_with_videos(url)
    except Exception as e:
        print("\n❌ Error:", e)
        return

    daily_target = data["total"] / days

    print(f"\n📌 Playlist: {data['name']}")
    print(f"🎯 Target per day: {format_duration(daily_target)}\n")

    current_day = 1
    current_time = 0
    start_video = data["videos"][0]["index"]

    for i, video in enumerate(data["videos"]):
        current_time += video["duration"]

        if current_time >= daily_target or i == len(data["videos"]) - 1:
            end_video = video["index"]
            print(f"Day {current_day} → Video {start_video} to {end_video}")
            current_day += 1
            current_time = 0

            if i + 1 < len(data["videos"]):
                start_video = data["videos"][i + 1]["index"]

            if current_day > days:
                break

# ------------------ Main ------------------

def main():
    print("\n📺 YouTube Playlist Duration Calculator")
    print("1. Length Calculation")
    print("2. Course Comparison Mode")
    print("3. Study Plan (Day-wise videos)")

    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        length_calculation_mode()
    elif choice == "2":
        course_comparison_mode()
    elif choice == "3":
        study_plan_mode()
    else:
        print("❌ Invalid choice")

if __name__ == "__main__":
    main()
    