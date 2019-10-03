
def main():
    states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York': 'NY',
        'Michigan': 'MI'
    }
    cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Jacksonville'
    }
    cities['AK'] = 'Fairbanks'
    cities['NY'] = 'Binghamton'
    print(cities[states['California']])

    print(states.values())

    for i in states:
        print(s[i])

    print(states.get('Alaska', 'Not Found'))
main()
