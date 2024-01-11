import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_tbl = project.merge(employee, on='employee_id', how='left')
    result = merged_tbl.groupby('project_id')['experience_years'].mean().round(2).rename('average_years').reset_index()
    return result