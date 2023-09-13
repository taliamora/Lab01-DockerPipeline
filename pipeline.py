#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import argparse

def get_data(DataSource):
    return pd.read_csv(DataSource)

def split_data(data):
    new_df = data.copy()

    new_df['Gender'].replace("FEMALE", "F", inplace=True)
    new_df['Gender'].replace("MALE", "M", inplace=True)

    df_F = new_df[new_df['Gender']=="F"].drop("Gender", axis=1)
    df_M = new_df[new_df['Gender']=="M"].drop("Gender", axis=1)
    return df_F, df_M

def save_data(data1, data2, FileName1, FileName2):
    data1.to_csv(FileName1)
    data2.to_csv(FileName2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('DataSource', help="Link to data csv")
    parser.add_argument('FileName1', help="Name of csv for first half of split data")
    parser.add_argument('FileName2', help="Name of csv for second half of split data")
    args = parser.parse_args()

    print("Starting...")
    df = get_data(args.DataSource)
    df1, df2 = split_data(df)
    save_data(df1, df2, args.FileName1, args.FileName2)
    print("The data has been split. \nComplete.")






