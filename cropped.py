#!/usr/bin/env python
# coding: utf-8

import pandas as pd


def main():
    csv_name = 'Air_Quality_Continuous.csv'

    df = pd.read_csv(csv_name)

    
    df['Site_ID'] = pd.to_numeric(df['Site_ID'], errors='coerce').astype('Int64')
    columns_to_convert = ['NOx','NO2','NO','PM10','O3','Temperature','NVPM10','VPM10','NVPM2_5','PM2_5','VPM2_5','CO','RH','Pressure','SO2']
    df[columns_to_convert] = df[columns_to_convert].astype(float)
    df['Date_Time'] = pd.to_datetime(df['Date_Time'], errors = 'coerce')
    start_date = pd.to_datetime('2015-01-01').tz_localize('UTC')
    end_date = pd.to_datetime('2023-10-22').tz_localize('UTC')
    df = df.loc[(df['Date_Time'] >= start_date)]
    
    cropped_data = df.to_csv('cropped_data.csv', index=False)
    
    df = df.loc[(df['Date_Time'] >= start_date) & (df['Date_Time'] <= end_date)]
    df = df.dropna(subset=['Site_ID'])
    df['Date_Time'] = pd.to_datetime(df['Date_Time'])
    df['ObjectId'] = pd.to_numeric(df['ObjectId'], errors='coerce').astype('Int64')
    df.fillna(0, inplace=True)
    
    cleansed_data = df.to_csv('cleansed_data.csv', index=False, encoding='utf-8-sig')

if __name__ == '__main__':
    main()
