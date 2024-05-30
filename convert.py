# Import Module
import pdftables_api
import pandas as pd
import numpy as np
import datetime
import requests

today = datetime.date.today()

def download_pdf(url, save_path):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the specified file path in binary write mode
            with open(save_path, 'wb') as file:
                # Write the content of the response to the file
                file.write(response.content)
            print(f"PDF downloaded successfully and saved to {save_path}")
        else:
            print(f"Failed to download PDF. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
yesterday = today - datetime.timedelta(days=1)

# Format yesterday's date as a string
yesterday_date = yesterday.strftime('%Y%m%d')
print(yesterday_date)
download_pdf(f'https://www.meteo.gov.lk/images/mergepdf/{yesterday_date}DD.pdf','report.pdf')

# API KEY VERIFICATION
conversion = pdftables_api.Client('d0bc7gnwipoz')

# PDf to CSV
# (Hello.pdf, Hello)
conversion.csv('report.pdf', f'{today}.csv')
# fieldDic = {
#     'Date':[],
#     'Anuradhapura':[],
#     'Badulla':[],
#     'Bandarawela':[],
#     'Batticaloa':[],
#     'Colombo':[],
#     'Galle':[],
#     'Hambanthota':[],
#     'Jaffna':[],
#     'Monaragala':[],
#     'Katugasthota':[],
#     'Katunayake':[],
#     'Kurunegala':[],
#     'Maha Illuppama':[],
#     'Mannar':[],
#     'Polonnaruwa':[],
#     'Nuwara Eliya':[],
#     'Pothuvil':[],
#     'Puttalam':[],
#     'Rathmalana':[],
#     'Rathnapura':[],
#     'Trincomalee':[],
#     'Vavuniya':[],
#     'Mattala':[],
#     'Mullativ':[],
#     'Karagala':[],
#     'Ayagama':[],
#     'Guruluwana':[],
#     'Kotagala Rosita':[],
#     'Maliboda':[],
#     'Benthotawatta':[],
#     'Hiniduma':[],
#     'Helboda North':[],
#     'Elston':[],
#     'Batuwangala':[],
#     'Labugama':[],
#     'Udaradella':[],
#     'Mathugama':[],
#     'Kalatuwawa':[],
#     'Ambewela':[],
#     'Kethendola':[],
#     'Handesa':[],
#     'Kaluthara':[],
#     'Padukka Estate':[],
#     'Thalangaha Estate':[],
#
# }
# dfFull= pd.DataFrame(fieldDic)
# dfFull.to_csv("rainfall.csv", index=False)

df = pd.read_csv(f'{today}.csv')

fieldDic = {
    'Date': [yesterday],
    'Anuradhapura': [df.iloc[1][4]],
    'Badulla': [df.iloc[2][4]],
    'Bandarawela': [df.iloc[3][4]],
    'Batticaloa': [df.iloc[4][4]],
    'Colombo': [df.iloc[5][4]],
    'Galle': [df.iloc[6][4]],
    'Hambanthota': [df.iloc[7][4]],
    'Jaffna': [df.iloc[8][4]],
    'Monaragala': [df.iloc[9][4]],
    'Katugasthota': [df.iloc[10][4]],
    'Katunayake': [df.iloc[11][4]],
    'Kurunegala': [df.iloc[12][4]],
    'Maha Illuppama': [df.iloc[13][4]],
    'Mannar': [df.iloc[14][4]],
    'Polonnaruwa': [df.iloc[15][4]],
    'Nuwara Eliya': [df.iloc[16][4]],
    'Pothuvil': [df.iloc[17][4]],
    'Puttalam': [df.iloc[18][4]],
    'Rathmalana': [df.iloc[19][4]],
    'Rathnapura': [df.iloc[20][4]],
    'Trincomalee': [df.iloc[21][4]],
    'Vavuniya': [df.iloc[22][4]],
    'Mattala': [df.iloc[23][4]],
    'Mullativ': [df.iloc[24][4]],
    'Karagala': [df.iloc[38][2]],
    'Ayagama': [df.iloc[39][2]],
    'Guruluwana': [df.iloc[40][2]],
    'Kotagala Rosita': [df.iloc[41][2]],
    'Maliboda': [df.iloc[42][2]],
    'Benthotawatta': [df.iloc[43][2]],
    'Hiniduma': [df.iloc[44][2]],
    'Helboda North': [df.iloc[45][2]],
    'Elston': [df.iloc[46][2]],
    'Batuwangala': [df.iloc[47][2]],
    'Labugama': [df.iloc[38][5]],
    'Udaradella': [df.iloc[39][5]],
    'Mathugama': [df.iloc[40][5]],
    'Kalatuwawa': [df.iloc[41][5]],
    'Ambewela': [df.iloc[42][5]],
    'Kethendola': [df.iloc[43][5]],
    'Handesa': [df.iloc[44][5]],
    'Kaluthara': [df.iloc[45][5]],
    'Padukka Estate': [df.iloc[46][5]],
    'Thalangaha Estate': [df.iloc[47][5]]

}
dfCreate =pd.DataFrame(fieldDic)
print(dfCreate)
dfFull= pd.read_csv('rainfall.csv')
dfFull= pd.concat([dfFull,dfCreate], axis=0)
dfFull.to_csv("rainfall.csv", index=False)
#dfCreate.to_csv("data.csv", index=False)