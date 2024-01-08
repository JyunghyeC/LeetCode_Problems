import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    students_cnt = courses.groupby('class')['student'].count().reset_index()
    five_mask = students_cnt[students_cnt['student'] >= 5]
    return five_mask[['class']]