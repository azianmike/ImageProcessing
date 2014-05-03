from gcm import GCM

API_KEY = 'AIzaSyD7pWKO8wqOGwD6nNIYqR43mJU3Ro56qGY'

gcm = GCM(API_KEY)
data = {'param1': 'value1', 'param2': 'value2'}

# Plaintext request
reg_id ="APA91bFWbHDaTUQBiKAxnakVySWj296FhT9ZULOeq4Pm0VcN72dtNOwIVzfKL534Bj4xEHvnbWmn7FObBVuNgv-3AB19ifgLz7WOeA6pjBw8JEb4kBHuQn8oGLLUhTN2itfoQTbuospDmV6pT3o6JcDblfjjYAnrWw"

returned = gcm.plaintext_request(registration_id=reg_id, data=data)

print returned