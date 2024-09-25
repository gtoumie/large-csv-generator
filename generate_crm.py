import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Define the number of rows to generate
rows_per_chunk = 10**6  # Number of rows per chunk
num_chunks = 8  # Number of chunks to reach around 2GB

# Define column names
columns = ['id', 'name', 'email', 'address', 'phone_number', 'date_of_birth']

def create_chunk(chunk_size):
    data = []
    for _ in range(chunk_size):
        data.append({
            'id': fake.unique.random_number(digits=9),
            'name': fake.name(),
            'email': fake.email(),
            'address': fake.address(),
            'phone_number': fake.phone_number(),
            'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
        })
    return pd.DataFrame(data, columns=columns)

# Create and save CSV chunks
for i in range(num_chunks):
    chunk_df = create_chunk(rows_per_chunk)
    chunk_df.to_csv(f'dummy_customer_data_part_{i+1}.csv', index=False)
    print(f'Chunk {i+1} saved.')

print('CSV files created.')
