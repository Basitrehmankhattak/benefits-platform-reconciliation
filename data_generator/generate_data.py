import pandas as pd
from faker import Faker
import random
print("Generator Started")

N_USERS  = 300
programs = [
          {"program_id":"P01","client_name":"Credit Agricole","cashback_rate":0.03},
          {"program_id":"P02","client_name":"AXA","cashback_rate":0.07},
          {"program_id":"P03","client_name":"Fnac","cashback_rate":0.01}
]


programs_df = pd.DataFrame(programs)
print(programs_df)
programs_df.to_csv("data/programs.csv", index = False)
print("Saved Programs.csv")


fake = Faker("fr_FR") # French-style data
Faker.seed(42) # always generate the same fake people
random.seed(42)

users = []
program_ids = programs_df["program_id"].tolist() # ['P01','P02','P03']
for i in range(N_USERS ):
    user = {
            "user_id":f"U{i+1:04d}",
            "program_id":random.choice(program_ids),
            "first_name":fake.first_name(),
            "last_name":fake.last_name(),
            "email":fake.email(),
            "iban":fake.iban(),
            "city":fake.city(),
            "created_at":fake.date_time_between(start_date="-2y",end_date="-60d")
    }
    users.append(user)

users_df = pd.DataFrame(users)
print(users_df.head())
users_df.to_csv("data/users.csv",index = False)
print("Saved users.csv")