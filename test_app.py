import unittest
from datetime import datetime
from app import app

class TestTinhTuoiApp(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.current_year = datetime.now().year

    # 1. Năm sinh hợp lệ
    def test_valid_birth_year(self):
        response = self.client.post("/", data={"birth_year": "1995"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tu", response.data)  # có kết quả

    # 2. Năm sinh = năm hiện tại
    def test_current_year(self):
        response = self.client.post("/", data={"birth_year": str(self.current_year)})
        self.assertIn(b"0", response.data)

    # 3. Biên dưới hợp lệ (1950)
    def test_min_valid_year(self):
        response = self.client.post("/", data={"birth_year": "1950"})
        self.assertIn(b"1950", response.data)

    # 4. Dưới biên (1949)
    def test_below_range(self):
        response = self.client.post("/", data={"birth_year": "1949"})
        self.assertIn(b"1950", response.data)

    # 5. Trên biên (năm sau)
    def test_above_range(self):
        response = self.client.post("/", data={"birth_year": str(self.current_year + 1)})
        self.assertIn(b"1950", response.data)

    # 6. Ký tự chữ
    def test_character_input(self):
        response = self.client.post("/", data={"birth_year": "abcd"})
        self.assertIn(b"kh", response.data)

    # 7. Ký tự đặc biệt
    def test_special_characters(self):
        response = self.client.post("/", data={"birth_year": "!@#$"})
        self.assertIn(b"kh", response.data)

    # 8. Dữ liệu trống
    def test_empty_input(self):
        response = self.client.post("/", data={"birth_year": ""})
        self.assertIn(b"kh", response.data)

    # 9. Số âm
    def test_negative_year(self):
        response = self.client.post("/", data={"birth_year": "-1980"})
        self.assertIn(b"1950", response.data)

    # 10. Số thực
    def test_decimal_input(self):
        response = self.client.post("/", data={"birth_year": "2000.5"})
        self.assertIn(b"kh", response.data)

    # 11. Số + chữ
    def test_mixed_input(self):
        response = self.client.post("/", data={"birth_year": "2000abcd"})
        self.assertIn(b"kh", response.data)

    # 12. Có khoảng trắng
    def test_whitespace_input(self):
        response = self.client.post("/", data={"birth_year": " 2002 "})
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
