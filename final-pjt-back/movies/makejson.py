import requests
import json

datalist = {}

def fetch_tmdb_data():
    # TMDB API 요청 URL 및 매개변수 설정
    # for page in range(1, 31):
    page = 10
        # print(page)
    response = requests.get(f'https://api.themoviedb.org/3/movie/top_rated?api_key=40a69d93e84171e666e3a8b8cfd8acb4&language=ko-KR&page={page}')
    # 응답 데이터를 JSON으로 변환
    json_data = response.json()
        # datalist.get(json_data['results'])
        # for k in range(20):
        #     datalist += json_data['results'][k]
        # print(json_data['results'][1])

    return json_data

# datalist = [0]*30
i = fetch_tmdb_data()

def save_to_json(json_data):
    file_path = "file10.json"
    # .json 파일로 데이터 저장
    with open(file_path, 'w', encoding='utf-8') as json_file1:
        json.dump(json_data, json_file1, indent=4, ensure_ascii=False)

# save_to_json(i)

aa = ['file.json','file.json2','file.json3','file.json4','file.json5', 'file.json6', 'file.json7', 'file.json8', 'file.json9', 'file.json10']


# json 파일 병합하기
def merge_json_files(file_paths, output_file):
    merged_data = []
    
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
            merged_data.extend(data)

    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(merged_data, output, indent=4)
merge_json_files(aa, 'last.json')