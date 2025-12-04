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
def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")
        choice = input("Chọn chức năng: ")
    if choice == '4':
        print('kết thúc')
if __name__ == "__main__":
    main()
