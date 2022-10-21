import os
import subprocess
import json
import ffmpeg


# 出力ファイル
OUTPUT_DIR = './output'
OUTPUT_FILE = 'output.mp3'

# オーディオファイルのパス一覧
path_json = open('./main_gate/data/audioFile.json', 'r')
path_data = json.load(path_json)

# 元の音源を削除
def deleteAudio():
    if os.listdir(OUTPUT_DIR):
        os.remove(OUTPUT_DIR + '/' + OUTPUT_FILE)

# 音源取得
def getAudio(name):
    name_data = list(filter(lambda data: data['name'] == name, path_data['02_name']))

    # 登録済みの名前か判定
    if name_data:
        audio_name = ffmpeg.input(name_data[0]['path'])
        audio_aff_data = list(filter(lambda data: data['name'] == name_data[0]['aff'], path_data['03_aff']))
        audio_aff = ffmpeg.input(audio_aff_data[0]['path'])

        # 音源結合
        generateAudio('name', audio_name, audio_aff)
    elif name.startswith('id'):
        audio_name_0_data = list(filter(lambda data: data['name'] == name[2], path_data['02_id']))
        audio_name_1_data = list(filter(lambda data: data['name'] == name[3], path_data['02_id']))
        audio_name_2_data = list(filter(lambda data: data['name'] == name[4], path_data['02_id']))

        audio_name_id = ffmpeg.input(path_data['02_id'][0]['path'])
        audio_name_0 = ffmpeg.input(audio_name_0_data[0]['path'])
        audio_name_1 = ffmpeg.input(audio_name_1_data[0]['path'])
        audio_name_2 = ffmpeg.input(audio_name_2_data[0]['path'])

        # 音源結合
        generateAudio('id', audio_name_id, audio_name_0, audio_name_1, audio_name_2)
    else:
        print('[Error] 登録されていない名前です')

# 音源結合
def generateAudio(type, *audio):

    # 元の音源を削除
    deleteAudio()

    # 音源入力
    audio_auth = ffmpeg.input(path_data['01_auth'][0]['path'])
    audio_success = ffmpeg.input(path_data['04_success'][0]['path'])
    audio_open = ffmpeg.input(path_data['05_open'][0]['path'])

    if type == 'name':
        (
            ffmpeg
            .concat(audio_auth, audio[0], audio[1], audio_success, audio_open, v=0, a=1)
            .output(OUTPUT_DIR + '/' + OUTPUT_FILE)
            .run()
        )
    else:
        (
            ffmpeg
            .concat(audio_auth, audio[0], audio[1], audio[2], audio[3], audio_success, audio_open, v=0, a=1)
            .output(OUTPUT_DIR + '/' + OUTPUT_FILE)
            .run()
        )

    playAudio()

# 音源再生
def playAudio():
    subprocess.Popen(['start', OUTPUT_DIR + '/' + OUTPUT_FILE], shell=True)
