import unittest
import requests

class DogAPITests(unittest.TestCase):

    base_url = "https://dog.ceo/api"

    def test_get_all_breeds(self):
        response = requests.get(f"{self.base_url}/breeds/list/all")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_get_breed_info(self):
        breed = "labrador"
        response = requests.get(f"{self.base_url}/breed/{breed}/list")
        self.assertEqual(response.status_code, 200)
        self.assertIn(breed, response.json()["message"])

    def test_get_random_breed_image(self):
        response = requests.get(f"{self.base_url}/breeds/image/random")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_get_nonexistent_breed(self):
        nonexistent_breed = "nonexistent"
        response = requests.get(f"{self.base_url}/breed/{nonexistent_breed}/list")
        self.assertEqual(response.status_code, 404)
        self.assertIn("message", response.json())
        self.assertIn("not found", response.json()["message"].lower())

    def test_get_limited_images(self):
        limit = 3
        response = requests.get(f"{self.base_url}/breeds/image/random/{limit}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["message"]), limit)

if __name__ == "__main__":
    unittest.main()



# Отчет о проведенном тестировании:

#     Тестирование на получение списка всех пород:
#         Результат: Проверка пройдена успешно, получен код ответа 200 и список пород.

#     Тестирование на получение информации о конкретной породе:
#         Результат: Проверка пройдена успешно, получен код ответа 200 и информация о выбранной породе.

#     Тестирование на получение изображения случайной породы:
#         Результат: Проверка пройдена успешно, получен код ответа 200 и URL изображения.

#     Тестирование на случай, когда порода не существует:
#         Результат: Проверка пройдена успешно, получен код ответа 404 и информация об ошибке.

#     Тестирование на ограничение по количеству получаемых изображений:
#         Результат: Проверка пройдена успешно, получено ограниченное количество изображений.