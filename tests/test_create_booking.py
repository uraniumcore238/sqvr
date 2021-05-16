import requests
from self import self


class TestCreateBooking():

    url='https://restful-booker.herokuapp.com/booking'

    def test_positive_booking_creation(self):

        parameters = {"firstname": "Jim", "lastname": "Brown", "totalprice": 111, "depositpaid": True, "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}

        response=requests.post(TestCreateBooking.url, json=parameters)
        assert response.status_code==200
        dict_json_data=response.json()
        total_price=dict_json_data['booking']['totalprice']
        total_price_original = parameters['totalprice']
        assert total_price==total_price_original
        print('Test was finished successfully')


    def test_negative_booking_creation(self):

        param_dict = {"firstname": "Jim", "lastname": "Brown", "totalprice": 1111122222333334444455555, "depositpaid": True, "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"}, "additionalneeds": "Breakfast"}

        response=requests.post(TestCreateBooking.url, json=param_dict)
        assert response.status_code == 200
        dict_json_data = response.json()
        total_price=dict_json_data['booking']['totalprice']
        total_price_original = param_dict['totalprice']
        assert total_price==total_price_original
        print('Test was finished successfully')


TestCreateBooking.test_positive_booking_creation(self)
TestCreateBooking.test_negative_booking_creation(self)