import pandas as pd
 
 
def encode_binary_ordinal(train, test):
    binary_map = {"Yes": 1, "No": 0}
    ordinal_map = {"Low": 0, "Medium": 1, "High": 2}
 
    binary_cols = ["Subsidy_Available", "Home_Charging_Possible"]
    ordinal_cols = ["Range_Anxiety_Level"]
 
    for df in [train, test]:
        for col in binary_cols:
            df[col] = df[col].map(binary_map)
        for col in ordinal_cols:
            df[col] = df[col].map(ordinal_map)
 
        df["Subsidy_HomeCharging"] = df["Subsidy_Available"] * df["Home_Charging_Possible"]
        df["Subsidy_EnvConcern"] = df["Subsidy_Available"] * df["Environmental_Concern_Level"]
        df["Anxiety_EnvConcern"] = df["Range_Anxiety_Level"] * df["Environmental_Concern_Level"]
        df["Anxiety_HomeCharging"] = df["Range_Anxiety_Level"] * df["Home_Charging_Possible"]
        df["Subsidy_Anxiety_Home"] = df["Subsidy_Available"] * df["Home_Charging_Possible"] * (df["Range_Anxiety_Level"] == 0).astype(int)
 
    return train, test
 
 
def add_features(train, test):
    for df in [train, test]:
        df["Charging_Station_Diff"] = df["Charging_Stations_Near_Home"] - df["Charging_Stations_Near_Work"]
        df["Charging_Station_Ratio"] = df["Charging_Stations_Near_Home"] / (df["Charging_Stations_Near_Work"] + 1)
        df["Cars_Per_ChargingHome"] = df["Number_of_Cars_Owned"] / (df["Charging_Stations_Near_Home"] + 1)
        df["Commute_Per_ChargingWork"] = df["Daily_Commute_km"] / (df["Charging_Stations_Near_Work"] + 1)
        df["Income_Per_Car"] = df["Annual_Income_USD"] / df["Number_of_Cars_Owned"].replace(0, 1)
        df["Commute_Per_Car"] = df["Daily_Commute_km"] / df["Number_of_Cars_Owned"].replace(0, 1)
        df["Income_Per_Commute"] = df["Annual_Income_USD"] / (df["Daily_Commute_km"] + 1)
        df["High_EnvConcern"] = (df["Environmental_Concern_Level"] >= 4).astype(int)
        df["High_Income"] = (df["Annual_Income_USD"] > df["Annual_Income_USD"].median()).astype(int)
        df["Long_Commute"] = (df["Daily_Commute_km"] > df["Daily_Commute_km"].median()).astype(int)
        df["Age_Group"] = pd.cut(df["Age"], bins=[0, 35, 50, 100], labels=["Young", "Mid", "Senior"]).astype(str)
        df["Multi_Car"] = (df["Number_of_Cars_Owned"] > 1).astype(int)
        df["Is_Urban"] = (df["City_Type_Urban"] == 1).astype(int) if "City_Type_Urban" in df.columns else 0
        df["Total_Charging_Access"] = df["Charging_Stations_Near_Home"] + df["Charging_Stations_Near_Work"]
        df["ChargingHome_x_Subsidy"] = df["Charging_Stations_Near_Home"] * df["Subsidy_Available"]
        df["ChargingWork_x_Subsidy"] = df["Charging_Stations_Near_Work"] * df["Subsidy_Available"]
 
    return train, test