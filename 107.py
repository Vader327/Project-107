import pandas as pd
import plotly.express as px

px.scatter(
  pd.read_csv("data.csv").groupby(["student_id", "level"], as_index=False)["attempt"].mean(),
  x="student_id", y="level", size="attempt", color="attempt"
).show()