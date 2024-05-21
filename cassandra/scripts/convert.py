import pandas as pd


def transform_date(date_str):
    return pd.to_datetime(date_str).strftime('%Y-%m-%d %H:%M:%S')


def transform_cast(cast_str):
    # Handle cases where the cast value is not a string (e.g., NaN)
    if isinstance(cast_str, str):
        return "(" + ", ".join(cast_str.split(', ')) + ")"
    else:
        return cast_str


if __name__ == '__main__':
    # Input and output file paths
    input_file = 'netflix_shows.csv'
    output_file = 'output.csv'

    df = pd.read_csv('netflix_shows.csv')

    df['date_added'] = df['date_added'].apply(transform_date)
    df['cast'] = df['cast'].apply(transform_cast)
    df['listed_in'] = df['listed_in'].apply(transform_cast)

    df.to_csv("output.csv", index=False, mode="w")

    print("CSV transformation complete. Output written to", output_file)

