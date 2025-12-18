import unittest
from app import app

class TestTinhTuoiApp(unittest.TestCase):
    # Thiết lập trước khi chạy các test
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Test case 1: Năm sinh hợp lệ (1995)
    def test_valid_birth_year(self):
        response = self.app.post("/", data={"birth_year": "1995"})
        self.assertIn(b"Tuoi: 30", response.data)  # Kỳ vọng tuổi là 30

    # Test case 2: Năm sinh là năm hiện tại (2025)
    def test_birth_year_current_year(self):
        response = self.app.post("/", data={"birth_year": "2025"})
        self.assertIn(b"Tuoi: 0", response.data)  # Kỳ vọng tuổi là 0

    # Test case 3: Năm sinh nhỏ nhất trong khoảng hợp lệ (1950)
    def test_birth_year_min_range(self):
        response = self.app.post("/", data={"birth_year": "1950"})
        self.assertIn(b"Tuoi: 75", response.data)  # Kỳ vọng tuổi là 75

    # Test case 4: Năm sinh nhỏ hơn khoảng hợp lệ (1949)
    def test_birth_year_below_range(self):
        response = self.app.post("/", data={"birth_year": "1949"})
        self.assertIn(b"Vui l\xf2ng ch\u1ecdn n\u0103m sinh t\u1eeb 1950 \u0111\u1ebfn hi\u1ec7n t\u1ea1i.", response.data)

    # Test case 5: Năm sinh lớn hơn khoảng hợp lệ (2026)
    def test_birth_year_above_range(self):
        response = self.app.post("/", data={"birth_year": "2026"})
        self.assertIn(b"Vui l\xf2ng ch\u1ecdn n\u0103m sinh t\u1eeb 1950 \u0111\u1ebfn hi\u1ec7n t\u1ea1i.", response.data)

    # Test case 6: Dữ liệu chữ (abcd)
    def test_invalid_character_input(self):
        response = self.app.post("/", data={"birth_year": "abcd"})
        self.assertIn(b"D\u1eef li\u1ec7u kh\xf4ng h\u1ee3p l\u1ec7.", response.data)

    # Test case 7: Dữ liệu ký tự đặc biệt (!@#$)
    def test_special_character_input(self):
        response = self.app.post("/", data={"birth_year": "!@#$"})
        self.assertIn(b"D\u1eef li\u1ec7u kh\xf4ng h\u1ee3p l\u1ec7.", response.data)

    # Test case 8: Dữ liệu trống
    def test_empty_input(self):
        response = self.app.post("/", data={"birth_year": ""})
        self.assertIn(b"D\u1eef li\u1ec7u kh\xf4ng h\u1ee3p l\u1ec7.", response.data)

    # Test case 9: Năm sinh âm (-1980)
    def test_negative_birth_year(self):
        response = self.app.post("/", data={"birth_year": "-1980"})
        self.assertIn(b"Vui l\xf2ng ch\u1ecdn n\u0103m sinh t\u1eeb 1950 \u0111\u1ebfn hi\u1ec7n t\u1ea1i.", response.data)

    # Test case 10: Dữ liệu số thực (2000.5)
    def test_decimal_birth_year(self):
        response = self.app.post("/", data={"birth_year": "2000.5"})
        self.assertIn(b"D\u1eef li\u1ec7u kh\xf4ng h\u1ee3p l\u1ec7.", response.data)

    # Test case 11: Năm sinh hợp lệ khác (1967)
    def test_valid_birth_year_1967(self):
        response = self.app.post("/", data={"birth_year": "1967"})
        self.assertIn(b"Tuoi: 58", response.data)  # Kỳ vọng tuổi là 58

    # Test case 12: Dữ liệu kết hợp số và chữ (2000abcd)
    def test_mixed_character_number_input(self):
        response = self.app.post("/", data={"birth_year": "2000abcd"})
        self.assertIn(b"D\u1eef li\u1ec7u kh\xf4ng h\u1ee3p l\u1ec7.", response.data)

    # Test case 13: Năm sinh hợp lệ (1975)
    def test_valid_birth_year_1975(self):
        response = self.app.post("/", data={"birth_year": "1975"})
        self.assertIn(b"Tuoi: 50", response.data)  # Kỳ vọng tuổi là 50

    # Test case 14: Dữ liệu hợp lệ với khoảng trắng (2002)
    def test_input_with_whitespace(self):
        response = self.app.post("/", data={"birth_year": " 2002 "})
        self.assertIn(b"Tuoi: 23", response.data)  # Kỳ vọng tuổi là 23 sau khi xử lý khoảng trắng

if __name__ == "__main__":
    unittest.main()
