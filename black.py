### Add code below, anything here is not executed. Happy cleaning!

import time


def log_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        print(f"Finished '{func.__name__}' in {time.time() - start_time} seconds.")
        return result

    return wrapper


@log_execution
def update_pii(schema: str, table: str, df: object):
    for _, row in df.iterrows():

        sql_query = f"""
    ALTER TABLE `{schema}`.`{table}`
    ALTER COLUMN `{row['Column']}`
    SET TAGS ('pii' = '{row['PIICategory']}')
    """

        print(f"Executing query: {sql_query}")

        try:
            spark.sql(sql_query)
        except Exception as e:
            print(f"Error for column {row['Column']}: {e}")


update_pii(df=pii_df, schema="raw", table="salesforceci_user")
