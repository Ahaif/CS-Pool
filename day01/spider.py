#!/usr/bin/env python3

import os
import argparse
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup



def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)


def extract_images(url, max_depth, save_path, depth=0):
    if depth > max_depth:
        return

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    image_tags = soup.find_all('img')
    for image_tag in image_tags:
        image_url = urljoin(url, image_tag['src'])
        if image_url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
            image_name = os.path.basename(image_url)
            save_file_path = os.path.join(save_path, image_name)
            print(f'Downloading: {image_url}')
            download_image(image_url, save_file_path)

    if depth < max_depth:
        link_tags = soup.find_all('a')
        for link_tag in link_tags:
            link_url = urljoin(url, link_tag['href'])
            extract_images(link_url, max_depth, save_path, depth + 1)


def main():
    parser = argparse.ArgumentParser(description='Web Spider - Extract Images')
    parser.add_argument('url', help='URL to start spidering')
    parser.add_argument('-r', action='store_true', help='Recursively download images')
    parser.add_argument('-l', type=int, default=5, help='Maximum depth level for recursive download')
    parser.add_argument('-p', default='./data/', help='Path to save downloaded files')

    args = parser.parse_args()
    url = args.url
    recursive = args.r
    max_depth = args.l
    save_path = args.p

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    if recursive:
        extract_images(url, max_depth, save_path)
    else:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Add this line to raise an exception for non-200 status codes
            soup = BeautifulSoup(response.text, 'html.parser')

            image_tags = soup.find_all('img')
            for image_tag in image_tags:
                image_url = urljoin(url, image_tag['src'])
                if image_url.startswith('javascript:') or image_url == 'javascript:void(0)':
                    continue
                if image_url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                    image_name = os.path.basename(image_url)
                    save_file_path = os.path.join(save_path, image_name)
                    print(f'Downloading: {image_url}')
                    download_image(image_url, save_file_path)

        except requests.exceptions.RequestException as e:
            print(f"Error occurred while accessing URL: {url}")
            print(e)


    

if __name__ == '__main__':
    main()
