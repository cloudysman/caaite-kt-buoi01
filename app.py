import os


def doc_khoa():
    return os.environ.get('API_KEY', '')


def main():
    print('xin chao', doc_khoa())


if __name__ == '__main__':
    main()
