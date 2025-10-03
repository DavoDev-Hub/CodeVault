def make_car(model, manufacturer, **car_info):
    car_info['model'] = model
    car_info['manufacturer'] = manufacturer
    return car_info
