
def getGain(s):
    return s[3] * s[1] - s[0] * s[1]

def highestGain(portfolio):
    highest = getGain(portfolio[0])
    symbol = portfolio[0][2]
    for stock in portfolio[1:]:
        if highest < getGain(stock):
            highest = getGain(stock)
            symbol = stock[2]
    return highest, symbol

def main():

main()
