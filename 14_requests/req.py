import requests
def main():
    r = requests.get('https://opentdb.com/api.php?amount=1&category=18')
    trivia = r.json() #converts the data to a dictionary
    trivia = trivia['results'][0]
    for q in trivia:
        print(q, ':', trivia.get(q))
main()
