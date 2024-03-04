import pandas as pd

# def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
#     return person.merge(address, on = "personId",how = "left")[["firstName","lastName","city","state"]]


 # OR

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    combined = pd.merge(person, address, how='left', on='personId')
    return combined[['firstName', 'lastName', 'city', 'state']]   