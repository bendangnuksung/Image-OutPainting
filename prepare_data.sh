cd data/raw_data
echo "Downloading Dataset:"
sudo wget http://cvcl.mit.edu/scenedatabase/coast.zip
sudo apt-get install unzip
unzip coast.zip -d ./
sudo rm coast.zip
cd ../../
echo "Preparing Data:"
python3 prepare_data.py
echo "completed"