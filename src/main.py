from configparser import ConfigParser
import requests


def main():
    config = ConfigParser()
    config.read('src/resources/application.properties')
    api_properties = config['API']
    
    response = get_image(api_properties, 420)
    print(response.status_code)
    print(response.json())
    return


def get_image(api, index):
    host = api['host']
    image_path = api['image_path']
    url = host + image_path + str(index)
    return requests.get(url)
 

if __name__ == '__main__':
    main()
