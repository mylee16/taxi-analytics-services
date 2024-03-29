import s2cell


def data_preprocessing(df, s2id_level=16):
    """Feature engineering and dropping of unused columns, including:
    1. Creating YYYY-MM-DD date column
    2. Creating s2id from s2cell package
    3. dropping all unused columns
    """
    # create date
    df["date"] = df["trip_start_timestamp"].dt.strftime("%Y-%m-%d")

    # create s2id from s2cell
    df["s2id"] = df[["pickup_latitude", "pickup_longitude"]].apply(
        lambda x: s2cell.lat_lon_to_cell_id(
            x.pickup_latitude, x.pickup_longitude, s2id_level
        )
        if x.notnull().all()
        else 0,
        axis=1,
    )
    df["s2id"] = df["s2id"].astype(str)

    # drop all unused columns
    df = df[["unique_key", "date", "s2id", "trip_miles", "trip_seconds", "fare"]]

    return df
