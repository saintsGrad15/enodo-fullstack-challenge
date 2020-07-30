import logging
import sqlite3
import pandas as pd


logger = logging.getLogger(__name__)

COLUMN_LIST = [
    "index",
    "Full Address",
    "CLASS_DESCRIPTION",
    "selected"
]


def get_database_connection():
    return sqlite3.connect("enodo.db")


def create_database():
    """
    Load spreadsheet data from disk and standup the SQLite DB.

    :return: None
    """

    connection = get_database_connection()

    with connection:
        db_data = get_database_data_as_df()
        create_table_from_df(db_data, connection)


def get_database_data_as_df():
    """
    Load spreadsheet data from disk as a Pandas DataFrame.

    :return: A Pandas DataFrame of spreadsheet data.
    :rtype: DataFrame
    """

    logger.info("Loading DB data from .xlsx file...")

    df = pd.read_excel("Enodo_Skills_Assessment_Data_File.xlsx")

    logger.info("DB data loaded.")

    return df


def create_table_from_df(df, connection):
    """

    :param df: A DataFrame of the data from which to create the table.
    :type df: DataFrame

    :param connection: An instance of a database connection.
    :type connection: Connection

    :return: None
    """

    logger.info("Inserting DB data...")

    df["selected"] = 0

    df.to_sql(name="properties", con=connection, if_exists="replace")

    logger.info("DB data inserted.")


def get_properties_by_address_or_description_fragment(fragment):
    """
    Query the database for 15 rows whose "Full Address" or "CLASS_DESCRIPTION" columns
    contain substring 'fragment." The search is case insensitive.

    :param fragment: A substring for which to search the "Full Address" or "CLASS_DESCRIPTION" columns.
    :type fragment: str

    :return: A list of dicts representing the matching properties.
    :rtype: list
    """

    connection = get_database_connection()

    with connection:
        cursor = connection.cursor()

        cursor.execute(
            '''
            SELECT "{}"
            FROM properties
            WHERE "{}" LIKE :fragment
            OR "{}" LIKE :fragment
            '''.format(
                '", "'.join(COLUMN_LIST),
                COLUMN_LIST[1],
                COLUMN_LIST[2]
            ),
            {"fragment": "%{}%".format(fragment)}
        )

        response = cursor.fetchmany(15)

    return get_property_dicts_from_response(response)


def get_selected_properties():
    """
    Query the database for all rows whose "selected" column = 0.

    :return: A list of dicts representing the matching properties.
    :rtype: list
    """

    connection = get_database_connection()

    with connection:
        cursor = connection.cursor()

        cursor.execute('''
            SELECT "{}"
            FROM properties
            WHERE selected = 1
            '''.format('", "'.join(COLUMN_LIST)))

        response = cursor.fetchall()

        return get_property_dicts_from_response(response)


def set_property_selected_true(index):
    """
    Set "selected" column of the property with index 'index' to 1.

    :param index: The index of property to select.
    :type index: int

    :return: None
    """

    connection = get_database_connection()

    with connection:
        cursor = connection.cursor()

        cursor.execute('''
            UPDATE properties
            SET selected = 1
            WHERE "index" = :index
            ''', {"index": index})

        connection.commit()


def set_property_selected_false(index):
    """
    Set "selected" column of the property with index 'index' to 0.

    :param index: The index of property to deselect.
    :type index: int

    :return: None
    """

    connection = get_database_connection()

    with connection:
        cursor = connection.cursor()

        cursor.execute('''
            UPDATE properties
            SET selected = 0
            WHERE "index" = :index
            ''', {"index": index})

        connection.commit()


def get_property_dicts_from_response(response):
    property_dicts = []

    for property_ in response:
        property_dict = {}

        for column_index, column in enumerate(COLUMN_LIST):
            property_dict[column] = property_[column_index]

        property_dicts.append(property_dict)

    return property_dicts
