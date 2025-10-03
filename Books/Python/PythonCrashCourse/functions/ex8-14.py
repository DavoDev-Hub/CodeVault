def make_car(model, manufacturer, **car_info):
    car_info['model'] = model
    car_info['manufacturer'] = manufacturer
    return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)