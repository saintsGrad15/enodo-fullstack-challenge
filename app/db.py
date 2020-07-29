import logging
import sqlite3
import pandas as pd


logger = logging.getLogger(__name__)

COLUMN_LIST = [
    "index",
    "Full Address",
    "CLASS_DESCRIPTION"
]


def get_database_connection():
    return sqlite3.connect("enodo.db")


def create_database():
    """
    Load spreadsheet data from disk and standup the SQLite DB.

    :return: None
    """

    connection = get_database_connection()

    db_data = get_database_data_as_df()
    create_table_from_df(db_data, connection)

    connection.close()


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
    Query the database for all rows whose "Full Address" or "CLASS_DESCRIPTION" columns
    contain substring 'fragment." The search is case insensitive.

    :param fragment: A substring for which to search the "Full Address" or "CLASS_DESCRIPTION" columns.
    :type fragment: str

    :return: A list of dicts representing the matching properties.
    """

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute(
        '''
        SELECT "{}", "{}", "{}"
        FROM properties
        WHERE "{}" LIKE :fragment
        OR "{}" LIKE :fragment
        '''.format(
            *COLUMN_LIST,
            COLUMN_LIST[1],
            COLUMN_LIST[2]
        ),
        {"fragment": "%{}%".format(fragment)}
    )

    properties = cursor.fetchall()

    property_dicts = []

    for property_ in properties:
        property_dict = {}

        for column_index, column in enumerate(COLUMN_LIST):
            property_dict[column] = property_[column_index]

        property_dicts.append(property_dict)

    connection.close()

    return property_dicts


def get_selected_properties():
    connection = get_database_connection()
    cursor = connection.cursor()


def select_property(index):
    connection = get_database_connection()
    cursor = connection.cursor()


def unselect_property(index):
    connection = get_database_connection()
    cursor = connection.cursor()
