#!/usr/bin/env bash
mkdir data/prepared_data
mkdir data/prepared_data/train
mkdir data/prepared_data/test
cd data/raw_data

echo "Downloading Dataset:"
fileid="1hKIn-Z8Uf3voESbJZVsapLHESPabjjrb"
filename="scrap_beach_image.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}

sudo apt-get install unzip
unzip scrap_beach_image.zip -d ./
sudo rm scrap_beach_image.zip
cd ../../
echo "Preparing Data:"
python3 prepare_data.py
echo "completed"