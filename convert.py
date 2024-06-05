# Import Module
import ollama
import pdftables_api
import pandas as pd
import numpy as np
import datetime
import fitz
import requests
import pdfplumber
import pandas as pd

today = datetime.date.today()
today_date = today.strftime("%Y%m%d")
yesterday = today - datetime.timedelta(days=1)

# Format yesterday's date as a string
yesterday_date = yesterday.strftime('%Y%m%d')
print(yesterday_date)
def download_pdf(url, save_path):
    try:
        today = datetime.date.today()
        today_date = today.strftime("%Y%m%d")
        # url =f'https://www.meteo.gov.lk/images/mergepdf/{yesterday_date}DD.pdf'
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Open the specified file path in binary write mode
            with open(save_path, 'wb') as file:
                # Write the content of the response to the file
                file.write(response.content)
            print(f"PDF downloaded successfully and saved to {save_path}")
        elif url == f'https://www.meteo.gov.lk/images/mergepdf/{yesterday_date}DD.pdf':
            url = f'https://www.meteo.gov.lk/images/mergepdf/{today_date}DD.pdf'
            download_pdf(url, save_path)
        elif url == f'https://www.meteo.gov.lk/images/mergepdf/{today_date}DD.pdf':
            today_date = today.strftime("%Y.%m.%d")
            url = f'https://www.meteo.gov.lk/images/{today_date}.pdf'
            download_pdf(url, save_path)
        else:
            print(f"Failed to download PDF. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")



#download_pdf(f'https://www.meteo.gov.lk/images/mergepdf/{yesterday_date}DD.pdf', 'report.pdf')

pdf = pdfplumber.open(r"report.pdf")
page0 = pdf.pages[0]
table = page0.extract_table()
df = pd.DataFrame(table)
print(df)
df.to_csv(f'{today}.csv', index=False)


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
    'Date': [today],
    'Anuradhapura': [df.iloc[4][3]],
    'Badulla': [df.iloc[5][3]],
    'Bandarawela': [df.iloc[6][3]],
    'Batticaloa': [df.iloc[7][3]],
    'Colombo': [df.iloc[8][3]],
    'Galle': [df.iloc[9][3]],
    'Hambanthota': [df.iloc[10][3]],
    'Jaffna': [df.iloc[11][3]],
    'Monaragala': [df.iloc[12][3]],
    'Katugasthota': [df.iloc[13][3]],
    'Katunayake': [df.iloc[14][3]],
    'Kurunegala': [df.iloc[15][3]],
    'Maha Illuppama': [df.iloc[16][3]],
    'Mannar': [df.iloc[17][3]],
    'Polonnaruwa': [df.iloc[18][3]],
    'Nuwara Eliya': [df.iloc[19][3]],
    'Pothuvil': [df.iloc[20][3]],
    'Puttalam': [df.iloc[21][3]],
    'Rathmalana': [df.iloc[22][3]],
    'Rathnapura': [df.iloc[23][3]],
    'Trincomalee': [df.iloc[24][3]],
    'Vavuniya': [df.iloc[25][3]],
    'Mattala': [df.iloc[26][3]],
    'Mullativ': [df.iloc[27][3]],

}

# def extract_text_from_pdf(pdf_path):
#     text = ""
#     with fitz.open(pdf_path) as doc:
#         for page_num in range(len(doc)):
#             page = doc.load_page(page_num)
#             text += page.get_text()
#     return text
#
#
# print(extract_text_from_pdf("report.pdf"))
# x = list(extract_text_from_pdf("report.pdf"))
# print(x)

# def summarize_with_ollama(text, dic):
#     response = ollama.chat(model='llama3', messages=[
#         {
#             'role': 'user',
#             'content': f"Please Structure the following text to a csv to get the daily rainfall of the following cities {dic} in the text: {text}",
#         },
#     ])
#     return response['message']['content']
# print(summarize_with_ollama(extract_text_from_pdf("report.pdf"),fieldDic))

dfCreate =pd.DataFrame(fieldDic)
print(fieldDic)
dfFull= pd.read_csv('rainfall.csv')
dfFull= pd.concat([dfFull,dfCreate], axis=0)
dfFull.to_csv("rainfall.csv", index=False)
# #dfCreate.to_csv("data.csv", index=False)
