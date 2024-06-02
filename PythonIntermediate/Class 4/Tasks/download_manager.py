import threading
import requests


def download_file(url, filename):
    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        downloaded = 0
        total_length = int(total_length)
        with open(filename, 'wb') as file:
            for data in response.iter_content(chunk_size=4096):
                downloaded += len(data)
                file.write(data)
                progress = downloaded * 100 / total_length
                print(f'{filename}: {progress}%')


def main():
    urls = [
        'https://file-examples.com/wp-content/storage/2018/04/file_example_AVI_480_750kB.avi',
        'https://file-examples.com/storage/fef545ae0b661d470abe676/2017/11/file_example_MP3_700KB.mp3',
        'https://file-examples.com/wp-content/storage/2017/02/file_example_XLSX_5000.xlsx',
        # Add more URLs as needed
    ]

    threads = []
    for i, url in enumerate(urls):
        filename = f'file{i + 1}.txt'
        thread = threading.Thread(target=download_file, args=(url, filename))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
