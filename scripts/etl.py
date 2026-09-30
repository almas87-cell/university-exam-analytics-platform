import pandas as pd 
from sqlalchemy import create_engine

students = pd.read_csv("data/students.csv")
marks = pd.read_csv("data/marks.csv")

df = pd.merge(students, marks, on="student_id")

df = df.drop_duplicates()

#data quality check
df = df[
    (df["internal"] <= 30)
    &
    (df["external"] <=70)
]

#business transformation

df["total"] = (
    df["internal"]
    +
    df["external"]
)

df["status"] = df["total"].apply(
    lambda x: "Pass" if x>=40 else "Fail"
)

#postgreSQL Connection

engine = create_engine(
    "postgresql+psycopg2://postgres:admin123@localhost:5432/examdb"
)

df.to_sql(
    "fact_exam_results",
    engine,
    if_exists="replace",
    index=False
)

print("data Loaded Successfully")

print(df.head())

print("\nData Quality Report")
print("----------------------")
print("Total Rors:", len(df))
print("Null Values:\n")
print(df.isnull().sum())