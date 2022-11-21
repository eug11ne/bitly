import requests
from dotenv import load_dotenv
from urllib.parse import urlparse
import os
import argparse


def shorten_link(token, url):

  header = {'Authorization': f'Bearer {token}'}
  response = requests.post('https://api-ssl.bitly.com/v4/bitlinks',
                           headers=header,
                           json={'long_url': url})
  response.raise_for_status()
  return response.json()['link']


def count_clicks(token, bitlink):

  header = {'Authorization': f'Bearer {token}'}
  parsed_bitlink = urlparse(bitlink)
  formatted_bitlink = f'{parsed_bitlink.netloc}{parsed_bitlink.path}'
  full_address = f'https://api-ssl.bitly.com/v4/bitlinks/{formatted_bitlink}/clicks/summary'
  response = requests.get(full_address, headers=header)
  response.raise_for_status()
  return response.json()['total_clicks']


def is_bitlink(token, url):

  header = {'Authorization': f'Bearer {token}'}
  parsed_url = urlparse(url)
  formatted_url = f'{parsed_url.netloc}{parsed_url.path}'
  full_address = f'https://api-ssl.bitly.com/v4/bitlinks/{formatted_url}'
  response = requests.get(full_address, headers=header)
  return response.ok


def main():

  load_dotenv()
  token = os.getenv('BITLY_TOKEN')
  parser = argparse.ArgumentParser()
  parser.add_argument("link", type=str, help="link to process")
  args = parser.parse_args()
  link = args.link
  try:
    if is_bitlink(token, link):
      print("Number of clicks: ", count_clicks(token, link))
    else:
      print("Short link: ", shorten_link(token, link))
  except requests.exceptions.HTTPError:
    print("Invalid link or token.")


if __name__ == '__main__':
  main()

  '''    
    if is_bitlink(token, link):
    try:
      clicks = count_clicks(token, link)
      print('Number of clicks: ', clicks)
    except requests.exceptions.HTTPError as e:
      print('Something went wrong. Error: ', e)
  else:
    try:
      short_link = shorten_link(token, link)
      print('Short link: ', short_link)
    except requests.exceptions.HTTPError as e:
      print('Something went wrong. Error: ', e)

    
    
    
    
    if is_bitlink(link):
        try:
            clicks = count_clicks('cf87faf4c139a1c59f4ea8535fbebb83d0dc8878', link)
            print("Number of clicks: ", clicks)
        except requests.exceptions.HTTPError as e:
            print("Something went wrong. Error: ", e)
    else:
        try:
            short_link = shorten_link('cf87faf4c139a1c59f4ea8535fbebb83d0dc8878', link)
            print("Short link: ", shorten_link('cf87faf4c139a1c59f4ea8535fbebb83d0dc8878', link))
        except requests.exceptions.HTTPError as e:
            print("Something went wrong. Error: ", e)


    #is_bitlink('https://bit.ly/3Ebcyhk')

#    try:
#        clicks = count_clicks('cf87faf4c139a1c59f4ea8535fbebb83d0dc8878', 'https://bit.ly/3Ebcyhk')
#        print(clicks)
#    except requests.exceptions.HTTPError as e:
#        print("Something went wrong. Error: ", e)
    #link = input("Please input your link: ")

#    try:
#        user = shorten_link('cf87faf4c139a1c59f4ea8535fbebb83d0dc8878', link)
#        print(user)
#    except requests.exceptions.HTTPError as e:
#        print("Something went wrong. Error: ", e)



#print('Битлинк', shorten_link('cf87faf4c139a1c59f4ea8535fbebb83d0dc8878', 'https://mail.ru'))
    #print('user ', user_link('cf87faf4c139a1c59f4ea8535fbebb83d0dc8878'))
'''



