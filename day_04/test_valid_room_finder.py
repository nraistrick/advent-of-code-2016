import unittest
from day_04.day_4 import get_encrypted_room_name


class TestValidRoomFinder(unittest.TestCase):
    valid_room_1 = "aaaaa-bbb-z-y-x-123[abxyz]"
    valid_room_1_encrypted_name = "aaaaa-bbb-z-y-x"

    valid_room_2 = "a-b-c-d-e-f-g-h-987[abcde]"
    valid_room_2_encrypted_name = "a-b-c-d-e-f-g-h"

    valid_room_3 = "not-a-real-room-404[oarel]"
    valid_room_3_encrypted_name = "not-a-real-room"

    invalid_room_1 = "totally-real-room-200[decoy]"
    invalid_room_1_encrypted_name = "totally-real-room"

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


if __name__ == '__main__':
    unittest.main()
