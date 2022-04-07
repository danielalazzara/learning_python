import pandas as pd


data = pd.read_csv('data/study_data.csv', sep=';')


def sanitized_col_names(col_names: list) -> list:
    new_col_names = []
    for column in col_names:
        column = column.replace(' ', '_')
        column = column.lower()
        new_col_names.append(column)
    return new_col_names


def replace_null_data(col_names: list) -> None:
    for col in col_names:
        data[col] = data[col].fillna(value=0)


def process_time():
    pass


def main():
    print("Loading data")
    data.columns = sanitized_col_names(data.columns)
    print(data.head())
    replace_null_data(['date', 'difficulty', 'time_start', 'time_end'])
    print(data.head())


if __name__ == "__main__":
    main()


