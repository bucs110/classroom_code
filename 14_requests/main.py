import urllib.request

def main():
    """https://opentdb.com/api.php?amount=1&category=18"""
    with urllib.request.urlopen("http://icanhazip.com") as netref:
        trivia_question = netref.read()
        print(trivia_question.decode('utf-8'))
main()
