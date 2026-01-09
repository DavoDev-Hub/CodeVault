from city_functions import city_function

def test_city_country():
    city = city_function('Santiago', 'Chile')
    assert city == 'Santiago, Chile'

def test_city_country_population():
    city = city_function('santiago', 'chile', population=500000)
    assert city == 'Santiago, Chile - Population 500000'