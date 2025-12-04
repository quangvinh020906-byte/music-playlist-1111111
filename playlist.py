songs = [
    {
        'title': 'Lạc Trôi',
        'artist': 'Sơn Tùng MTP',
        'duration': 240
    },
    {
        'title': 'Nơi Này Có Anh',
        'artist': 'Sơn Tùng MTP',
        'duration': 221
    },
    {
        'title': 'Có Chơi Có Chịu',
        'artist': 'Karik',
        'duration': 200
    },
    {
        'title': 'Chạy Ngay Đi',
        'artist': 'Sơn Tùng MTP',
        'duration': 250
    },
    {
        'title': '3107',
        'artist': 'W/n',
        'duration': 180
    }
]
def add_song():
    title = input("Nhập tên bài hát: ")
    artist = input("Nhập tên ca sĩ: ")
    duration = int(input("Nhập thời lượng (giây): "))

    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }

    songs.append(song)
    print("✔ ĐÃ THÊM BÀI HÁT:", song)
def view_playlist():
    if len(songs) == 0:
        print("Playlist đang trống.")
        return

    print("\n--- DANH SÁCH PHÁT ---")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['title']} - {song['artist']} ({song['duration']}s)")
def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        choice = input("Chọn: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")
if __name__ == "__main__":
    main()

