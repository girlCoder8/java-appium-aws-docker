
from faker import Faker
import csv

fake = Faker()

def generate_data(output_csv, num_records=10):
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['name', 'email', 'address', 'text']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_records):
            writer.writerow({
                'name': fake.name(),
                'email': fake.email(),
                'address': fake.address().replace('\n', ', '),
                'text': fake.text()
            })

if __name__ == "__main__":
    generate_data("generated_test_data.csv")
