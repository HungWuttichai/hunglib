
import requests
url = 'https://notify-api.line.me/api/notify'


def text(token, text):
    LINE_HEADERS = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
    try:
        session_post = requests.post(url, headers=LINE_HEADERS , data = {'message':text})
        print(session_post.text)
    except:
        print("Network is not connected")


def image(token, text, path_img):
    file_img = {'imageFile': open(path_img, 'rb')}
    LINE_HEADERS = {"Authorization": "Bearer "+ token}
    try:
        session_post = requests.post(url, headers=LINE_HEADERS, files=file_img, data= {'message': text})
        print(session_post.text)
    except:
        print("Internet is not connected")

if __name__ == '__main__':
    token = 'your token'
    text(token, "Hello")
    image(token, "Oh!", "imageName.jpg")