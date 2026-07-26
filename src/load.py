from sqlalchemy import create_engine


def load(df):

    engine = create_engine(
    "postgresql://postgres:libertycity@localhost:5432/weathers_db"
)


    df.to_sql(
        "weather_data",
        engine,
        if_exists="append",
        index=False
    )