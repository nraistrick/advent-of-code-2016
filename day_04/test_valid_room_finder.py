import unittest
from day_04.day_4 import get_encrypted_room_name, get_sector_id, get_hash_value


class TestValidRoomFinder(unittest.TestCase):
    valid_room_1 = "aaaaa-bbb-z-y-x-123[abxyz]"
    valid_room_1_encrypted_name = "aaaaa-bbb-z-y-x"
    valid_room_1_sector_id = 123
    valid_room_1_hash_value = "abxyz"

    valid_room_2 = "a-b-c-d-e-f-g-h-987[abcde]"
    valid_room_2_encrypted_name = "a-b-c-d-e-f-g-h"
    valid_room_2_sector_id = 987
    valid_room_2_hash_value = "abcde"

    valid_room_3 = "not-a-real-room-404[oarel]"
    valid_room_3_encrypted_name = "not-a-real-room"
    valid_room_3_sector_id = 404
    valid_room_3_hash_value = "oarel"

    invalid_room_1 = "totally-real-room-200[decoy]"
    invalid_room_1_encrypted_name = "totally-real-room"
    invalid_room_1_sector_id = 200
    invalid_room_1_hash_value = "decoy"

    invalid_room_input = "notavalidroomidentifier"

    def test_get_encrypted_name(self):
        self.assertEqual(get_encrypted_room_name(self.valid_room_1),
                         self.valid_room_1_encrypted_name)

        self.assertEqual(get_encrypted_room_name(self.valid_room_2),
                         self.valid_room_2_encrypted_name)

        self.assertEqual(get_encrypted_room_name(self.valid_room_3),
                         self.valid_room_3_encrypted_name)

        self.assertEqual(get_encrypted_room_name(self.invalid_room_1),
                         self.invalid_room_1_encrypted_name)

        with self.assertRaises(ValueError):
            get_encrypted_room_name(self.invalid_room_input)

    def test_get_sector_id(self):
        self.assertEqual(get_sector_id(self.valid_room_1),
                         self.valid_room_1_sector_id)

        self.assertEqual(get_sector_id(self.valid_room_2),
                         self.valid_room_2_sector_id)

        self.assertEqual(get_sector_id(self.valid_room_3),
                         self.valid_room_3_sector_id)

        self.assertEqual(get_sector_id(self.invalid_room_1),
                         self.invalid_room_1_sector_id)

        with self.assertRaises(ValueError):
            get_sector_id(self.invalid_room_input)

    def test_get_hash_value(self):
        self.assertEqual(get_hash_value(self.valid_room_1),
                         self.valid_room_1_hash_value)

        self.assertEqual(get_hash_value(self.valid_room_2),
                         self.valid_room_2_hash_value)

        self.assertEqual(get_hash_value(self.valid_room_3),
                         self.valid_room_3_hash_value)

        self.assertEqual(get_hash_value(self.invalid_room_1),
                         self.invalid_room_1_hash_value)

        with self.assertRaises(ValueError):
            get_hash_value(self.invalid_room_input)


if __name__ == '__main__':
    unittest.main()
