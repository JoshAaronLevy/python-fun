import pandas as pd
import os
import glob

def add_data_chunk(chunk, final_pivot):
    final_pivot = final_pivot.add(pivot_chunk, fill_value=0)
    return final_pivot

def process_file(file_path):
    chunk_size = 10000
    final_pivot = None

    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        # 2 arrays. First array is 10000 rows of the raw csv data. Second is just an empty array
        # Converting the data to a pivot table and feeding the converted data into the pivot_chunk variable
        pivot_chunk = pd.pivot_table(chunk, values='value_column', index='row_index', columns='column_index', aggfunc='sum')  # Adjust these parameters

        if final_pivot is None:
            final_pivot = pivot_chunk
        else:
            final_pivot = pivot_chunk(pivot_chunk, fill_value=0)

    return final_pivot

def main():
    directory = 'path/to/your/directory'  # Replace with your directory
    pattern = os.path.join(directory, '*.csv')
    csv_files = glob.glob(pattern)

    if not csv_files:
        print("No CSV files found in the directory")
    else
      print ('Files found', len(csv_files))
      for file in csv_files:
          pivot_table = process_file(file)

if __name__ == "__main__":
    main()
