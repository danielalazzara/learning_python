import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv('data/study_data.csv', sep=';')


def sanitized_col_names(col_names: list) -> list:
    new_col_names = []
    for column in col_names:
        column = column.replace(' ', '_')
        column = column.lower()
        new_col_names.append(column)
    return new_col_names


def drop_columns():
    col_del = ['difficulty', 'temp1', 'temp2']
    data.drop(columns = col_del, inplace=True)


def replace_null_data(col_names: list) -> None:
    for col in col_names:
        data[col] = data[col].fillna(value=0)


def plot_graphs():
    ax = sns.relplot(x="date", y="units", data=data, kind="line", style="type", hue="type")
    ax.set_xticklabels(rotation=65)
    # plt.show()  # DEBUG
    plt.savefig("data/graphs/graph_1.png")
    plt.close()
    ax = sns.scatterplot(x="date", y="cumulative_units", data=data)
    # ax.set_xticklabels(ax.get_xticklabels(), rotation=65)
    # plt.show()  # DEBUG
    plt.savefig("data/graphs/graph_2.png")
    plt.close()


def main():
    print("Loading data")
    data.columns = sanitized_col_names(data.columns)
    drop_columns()
    replace_null_data(['date', 'time_start', 'time_end'])
    data['date'] = pd.to_datetime(data.date, format='%d/%m/%Y')
    data["cumulative_units"] = data["units"].cumsum()
    plot_graphs()


if __name__ == "__main__":
    main()


