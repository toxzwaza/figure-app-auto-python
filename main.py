import requests
import os
from PIL import Image  # 画像処理のためにPILをインポート
import sys
from line import line_notify
line_notify(f"図番検索システム ファイル同期実行")
                    
urls = ["http://remacs-app.local/autoInsert?imgCat=%E5%9B%B3%E9%9D%A2TIF", "http://remacs-app.local/autoInsert?imgCat=%E5%9B%B3%E9%9D%A2PDF"]
baseFilePath = "\\\\SV-AP01\\Documents"  # バックスラッシュをエスケープ

for url in urls:
    print(f'{url}')
    response = requests.get(url)
    data = response.json()  # 戻り値を変数に格納

    if data['status'] == 'ok':
        if data['data']:
            for item in data['data']:
                print(item)
                file_name = item['file_name']
                fig_num = item['fig_num']
                doc_name = item['doc_name']
                if 'tif' in file_name:   
                    filePath = f"{baseFilePath}\\{fig_num}\\{doc_name}\\{file_name}"
                    if os.path.exists(filePath):
                        print(f"ファイルが存在します: {filePath}")
                    
                        # tifファイルのパスを取得
                        tif_file_path = filePath

                        # pdfファイルのパスを生成
                        pdf_file_path = tif_file_path.replace('.tif', '.pdf')

                        # tifファイルを開いてpdfに変換して保存
                        with Image.open(tif_file_path) as img:
                            img.save(pdf_file_path, "PDF", resolution=100.0)
                else:
                    print(f"TIFファイルは存在しません。")
