# Easy links

Simple terminal tool to shorten your links.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Requirements

````
pip install python-dotenv
````
### Install token
You need to generate your [Bitlink-token](https://app.bitly.com/settings/api/) and pass it in a file `.env ` in a root folder of your project folder:
````
BITLINK_ACCESS_TOKEN=[your token]
````
### Demo

Past your link in terminal window after starting script:
```
% python3 main.py
Your link: https://www.youtube.com/watch?v=Z0VBygPj_VM&t=1935s
Bitlink:  https://bit.ly/3GXtE4x
```
If you past shorten link - script shows you the number of visits for this link:
````
% python3 main.py
Your link: https://bit.ly/3GXtE4x
This link has 0 clicks

````

## Versions
Python 3.11.1

## Authors

**Nik Bez ** - *Initial works* - [NkiBez](https://github.com/NikBez)

See also the list of [requirements](https://github.com/NikBez/easyLinks/blob/main/requirements.txt) who participated in this project.

