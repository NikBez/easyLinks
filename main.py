import os, sys
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    token = os.environ['BITLINK_ACCESS_TOKEN']
    user_link = input('Your link: ')

    if is_bitlink(user_link, token):
        try:
            click_count = count_clicks(user_link, token)
        except requests.exceptions.HTTPError:
            print("Can't find number of clicks for this link(")
            sys.exit()
        print(f'This link has {click_count} clicks')

    else:
        try:
            bitlink = shorten_link(user_link, token)
        except requests.exceptions.HTTPError:
            print("Link is invalid. ")
            sys.exit()

        print('Bitlink: ', bitlink)


def shorten_link(link, token):
    url = "https://api-ssl.bitly.com/v4/bitlinks"
    headers = {"Authorization": f"Bearer {token}"}
    link_params = {
        "long_url": link,
    }

    bitlink = requests.post(url, json=link_params, headers=headers)
    bitlink.raise_for_status()
    return bitlink.json()['link']


def count_clicks(bitlink, token):
    bitlink_parts = urlparse(bitlink)
    bitlink = bitlink_parts.netloc + bitlink_parts.path

    url = f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "unit": "day",
        "units": -1,
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()["total_clicks"]


def is_bitlink(link, token):

    link_parts = urlparse(link)
    link = link_parts.netloc + link_parts.path

    headers = {"Authorization": f"Bearer {token}"}
    url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}"

    response = requests.get(url, headers=headers)
    return response.ok


if __name__ == "__main__":
    main()
