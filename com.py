import pickle
import gzip

# Sample data to pickle
data = {"name": "Abhishek", "projects": ["Tourism Website", "Supermarket Data Analysis"]}

# Function to compress and save pickle file
def compress_pickle(file_name, data):
    with gzip.open(file_name, 'wb') as compressed_file:
        pickle.dump(data, compressed_file)
    print(f"Data compressed and saved to {file_name}")

# Function to decompress and load pickle file
def decompress_pickle(file_name):
    with gzip.open(file_name, 'rb') as compressed_file:
        data = pickle.load(compressed_file)
    print(f"Data loaded from {file_name}")
    return data

# File name for compressed pickle
compressed_file_name = "data.pkl.gz"

# Compress and save
compress_pickle(similarity
                
                
                ok, data)

# Decompress and load
loaded_data = decompress_pickle(compressed_file_name)

# Display the loaded data
print("Decompressed Data:", loaded_data)
