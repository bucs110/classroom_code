import requests

def main():
    try:
        contents = requests.get("http://api.ipify.org?format=json")
        data = contents.json()
    except:
        print("Resource not available")
    else:
        print(data)
main()
