import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of rows to generate
rows_per_chunk = 10**5  # Number of rows per chunk
num_chunks = 10  # Number of chunks

# Define column names
columns = ['fullname', 'firstname', 'lastname']

# Initialize a set to keep track of unique full names across chunks
unique_full_names = set()

def create_chunk(chunk_size, unique_full_names):
    data = []
    while len(data) < chunk_size:
        firstname = fake.first_name()
        lastname = fake.last_name()
        fullname = f"{firstname} {lastname}"
        if fullname not in unique_full_names:
            unique_full_names.add(fullname)
            data.append({
                'fullname': fullname,
                'firstname': firstname,
                'lastname': lastname
            })
    return pd.DataFrame(data, columns=columns)

# Create and save CSV chunks
for i in range(num_chunks):
    chunk_df = create_chunk(rows_per_chunk, unique_full_names)
    chunk_df.to_csv(f'names_part_{i+1}.csv', index=False)
    print(f'Chunk {i+1} saved.')

print('CSV files created.')
