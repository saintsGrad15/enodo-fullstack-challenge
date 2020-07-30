import unittest

from app.util import get_show_tables_command_string

from app.db import (get_database_connection,
                    create_database,
                    get_properties_by_address_or_description_fragment,
                    get_selected_properties,
                    set_property_selected_true,
                    set_property_selected_false)


IN_MEMORY_DB_NAME = ":memory:"


class TestDB(unittest.TestCase):
    def test_create_database(self):
        connection = get_database_connection(IN_MEMORY_DB_NAME)

        with connection:
            create_database(connection)

            cursor = connection.cursor()

            cursor.execute(get_show_tables_command_string())

            response = cursor.fetchall()

            if len(response) > 0:
                self.assertEqual(response[0][0], "properties", "The correct database table was not created.")
            else:
                self.fail("There appears to be no database tables. This is unexpected.")

    def test_get_properties_by_address_or_description_fragment(self):
        connection = get_database_connection(IN_MEMORY_DB_NAME)

        with connection:
            create_database(connection)

            properties = get_properties_by_address_or_description_fragment(connection, "six")

            self.assertGreater(len(properties), 0, "Zero properties were returned. This is unexpected.")

    def test_get_selected_properties_and_set_property_selected_true(self):
        connection = get_database_connection(IN_MEMORY_DB_NAME)

        with connection:
            create_database(connection)

            set_property_selected_true(connection, 0)

            selected_properties = get_selected_properties(connection)

            self.assertEqual(len(selected_properties), 1, "There was not exactly one selected property. This is unexpected.")
            self.assertEqual(selected_properties[0]["index"], 0, "The selected property's index was not zero. This is unexpected.")

    def test_set_property_selected_false(self):
        connection = get_database_connection(IN_MEMORY_DB_NAME)

        with connection:
            create_database(connection)

            set_property_selected_true(connection, 0)

            selected_properties = get_selected_properties(connection)

            self.assertEqual(len(selected_properties), 1, "There was not exactly one selected property. This is unexpected.")
            self.assertEqual(selected_properties[0]["index"], 0, "The selected property's index was not zero. This is unexpected.")

            set_property_selected_false(connection, 0)

            selected_properties_2 = get_selected_properties(connection)

            self.assertEqual(len(selected_properties_2), 0, "There was not exactly zero selected properties. This is unexpected.")


if __name__ == '__main__':
    unittest.main()
