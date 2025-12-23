import unittest
from labs2025_2026.rk1 import orchestras, conductors, conductors_orchestras
from labs2025_2026.rk1 import get_one_to_many, get_many_to_many
from labs2025_2026.rk1 import solve_b1, solve_b2, solve_b3

class TestRk2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.one_to_many = get_one_to_many(orchestras, conductors)
        cls.many_to_many = get_many_to_many(orchestras, conductors_orchestras, conductors)

    def test_b1_filter_by_name(self):
        result = solve_b1(self.one_to_many)
        for item in result:
            self.assertTrue(item[0].startswith('А'), f"Фамилия {item[0]} не начинается на 'А'")
        
        expected_surnames = ['Антонов', 'Алексеев', 'Андреев']
        actual_surnames = [item[0] for item in result]
        self.assertEqual(actual_surnames, expected_surnames)

    def test_b2_min_salary(self):
        result = solve_b2(self.one_to_many, orchestras)
        
        expected = [
            ('Филармонический оркестр', 45000),
            ('Симфонический оркестр', 50000),
            ('Камерный оркестр', 70000)
        ]
        self.assertEqual(result, expected)
        
        salaries = [r[1] for r in result]
        self.assertEqual(salaries, sorted(salaries), "Список не отсортирован по зарплате")

    def test_b3_sort_by_name(self):
        result = solve_b3(self.many_to_many)
        names = [item[0] for item in result]
        self.assertEqual(names, sorted(names), "Список не отсортирован по фамилиям")

if __name__ == '__main__':
    unittest.main()
