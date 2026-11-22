import pandas as pd
print("Generator Started")


programs = [
          {"program_id":"P01","client_name":"Credit Agricole","cashback_rate":0.03},
          {"program_id":"P02","client_name":"AXA","cashback_rate":0.07},
          {"program_id":"P03","client_name":"Fnac","cashback_rate":0.01}
]


programs_df = pd.DataFrame(programs)
print(programs_df)
programs_df.to_csv("data/programs.csv", index = False)
print("Saved Programs.csv")