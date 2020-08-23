def make_dictionary():
    # Create using an iterable of 2-pair values.
    countries_to_capitals = dict([
        ('United Kingdom', 'London'),
        ('Japan', 'Tokyo'),
        ('Russia', 'Moscow')
    ])

    # Literal.
    countries_to_capitals = {
        'United Kingdom': 'London',
        'Japan': 'Tokyo',
        'Russia': 'Moscow'
    }

    # Zipping two parallel arrays.
    # Note that the ordering is important.
    countries = ['United Kingdom', 'Japan', 'Russia']
    capitals = ['London', 'Tokyo', 'Moscow']

    countries_to_capitals = dict(zip(countries, capitals))

    return countries_to_capitals


def dictionary_usage():
    countries_to_capitals = make_dictionary()

    # Looping.
    for country_name in countries_to_capitals:
        print(f'{countries_to_capitals[country_name]} is the capital of {country_name}')

    # Membership.
    isFrance = 'France' in countries_to_capitals

    # Delete key value pair.
    del countries_to_capitals['Japan']

    dictionary_size = len(countries_to_capitals)

    # Contains a bunch of methods. See reference.
