import pandas as pd

df=pd.read_csv("dataset/student_performance_finalscore.csv")

print(df.head(10))
print(df.tail(10))

print(df.columns)
"""
Index(['Student_ID', 'Age', 'Gender', 'Hours_Studied', 'Attendance',
       'Sleep_Hours', 'Stress_Level', 'Screen_Time', 'Previous_GPA',
       'Part_Time_Job', 'Study_Method', 'Diet_Quality', 'Internet_Quality',
       'Extracurricular', 'Tutoring_Sessions_Per_Week', 'Family_Income_Level',
       'Exam_Anxiety_Score', 'Final_Score'],
      dtype='str')"""

print(df.isnull().sum())
"""
Student_ID                    0
Age                           0
Gender                        0
Hours_Studied                 0
Attendance                    0
Sleep_Hours                   0
Stress_Level                  0
Screen_Time                   0
Previous_GPA                  0
Part_Time_Job                 0
Study_Method                  0
Diet_Quality                  0
Internet_Quality              0
Extracurricular               0
Tutoring_Sessions_Per_Week    0
Family_Income_Level           0
Exam_Anxiety_Score            0
Final_Score                   0
dtype: int64
"""
print(df.duplicated().sum()) # 0 --> no repeated row
print(df.info())
"""
<class 'pandas.DataFrame'>
RangeIndex: 8000 entries, 0 to 7999
Data columns (total 18 columns):
 #   Column                      Non-Null Count  Dtype  
---  ------                      --------------  -----  
 0   Student_ID                  8000 non-null   str    
 1   Age                         8000 non-null   int64  
 2   Gender                      8000 non-null   str    
 3   Hours_Studied               8000 non-null   float64
 4   Attendance                  8000 non-null   float64
 5   Sleep_Hours                 8000 non-null   float64
 6   Stress_Level                8000 non-null   float64
 7   Screen_Time                 8000 non-null   float64
 8   Previous_GPA                8000 non-null   float64
 9   Part_Time_Job               8000 non-null   str    
 10  Study_Method                8000 non-null   str    
 11  Diet_Quality                8000 non-null   str    
 12  Internet_Quality            8000 non-null   str    
 13  Extracurricular             8000 non-null   str    
 14  Tutoring_Sessions_Per_Week  8000 non-null   int64  
 15  Family_Income_Level         8000 non-null   str    
 16  Exam_Anxiety_Score          8000 non-null   float64
 17  Final_Score                 8000 non-null   float64
dtypes: float64(8), int64(2), str(8)
memory usage: 1.1 MB
None"""
print(df.describe())
"""
               Age  Hours_Studied   Attendance  Sleep_Hours  Stress_Level  Screen_Time  Previous_GPA  Tutoring_Sessions_Per_Week  Exam_Anxiety_Score  Final_Score
count  8000.000000    8000.000000  8000.000000  8000.000000   8000.000000  8000.000000   8000.000000                 8000.000000         8000.000000  8000.000000
mean     20.494375       4.983845    79.933375     6.989125      5.014175     4.024525      2.992408                    1.700625            4.494238    83.205649
std       2.285962       1.951715     9.656594     1.192898      1.940126     1.481908      0.489530                    1.112836            1.685571    12.756728
min      17.000000       0.020000    43.300000     3.000000      1.000000     0.500000      1.500000                    0.000000            1.000000    22.810000
25%      18.000000       3.680000    73.400000     6.200000      3.700000     3.000000      2.670000                    1.000000            3.300000    75.507500
50%      20.500000       4.980000    80.100000     7.000000      5.000000     4.000000      2.990000                    2.000000            4.400000    86.510000
75%      22.000000       6.312500    86.600000     7.800000      6.300000     5.000000      3.330000                    2.000000            5.600000    93.080000
max      24.000000      12.000000   100.000000    10.000000     10.000000     9.600000      6.700000                    5.000000           10.000000    99.980000"""

print(df.corr(numeric_only=True).to_string())
"""
                                 Age  Hours_Studied  Attendance  Sleep_Hours  Stress_Level  Screen_Time  Previous_GPA  Tutoring_Sessions_Per_Week  Exam_Anxiety_Score  Final_Score
Age                         1.000000      -0.000788   -0.000055    -0.005313     -0.011280     0.002727      0.013405                    0.005456           -0.010126     0.017103
Hours_Studied              -0.000788       1.000000    0.017252     0.019577     -0.010874     0.000189      0.012320                    0.266811           -0.286131     0.591355
Attendance                 -0.000055       0.017252    1.000000     0.003726     -0.007547     0.003384      0.010618                    0.060990           -0.090481     0.168615
Sleep_Hours                -0.005313       0.019577    0.003726     1.000000      0.031963    -0.011176      0.004398                    0.072491           -0.085347     0.151673
Stress_Level               -0.011280      -0.010874   -0.007547     0.031963      1.000000     0.000577     -0.001236                   -0.169636            0.158435    -0.296634
Screen_Time                 0.002727       0.000189    0.003384    -0.011176      0.000577     1.000000      0.008390                   -0.050811            0.069986    -0.135252
Previous_GPA                0.013405       0.012320    0.010618     0.004398     -0.001236     0.008390      1.000000                    0.138943           -0.156278     0.291002
Tutoring_Sessions_Per_Week  0.005456       0.266811    0.060990     0.072491     -0.169636    -0.050811      0.138943                    1.000000           -0.235214     0.471524
Exam_Anxiety_Score         -0.010126      -0.286131   -0.090481    -0.085347      0.158435     0.069986     -0.156278                   -0.235214            1.000000    -0.494940
Final_Score                 0.017103       0.591355    0.168615     0.151673     -0.296634    -0.135252      0.291002                    0.471524           -0.494940     1.000000 """

"""
STRONG CORRELATIONS:
Hours_Studied - Final_Score --> 0.59
Tutoring_Sessions_Per_Week - Final_Score --> 0.47 
"""

df=df[df["Gender"] != "Non-Binary"]
df["Gender"].value_counts()
"""
Gender
Male      3906
Female    3810
Name: count, dtype: int64"""

df["Part_Time_Job"].value_counts()
"""
Part_Time_Job
No     4640
Yes    3076
Name: count, dtype: int64"""

df["Study_Method"].value_counts()
"""
Study_Method
Offline    3063
Online     2370
Hybrid     2283
Name: count, dtype: int64"""

df["Diet_Quality"].value_counts()
"""
Diet_Quality
Average    3834
Poor       1951
Good       1931
Name: count, dtype: int64"""

df["Internet_Quality"].value_counts()
"""
Internet_Quality
Good         3151
Average      2199
Excellent    1577
Poor          789
Name: count, dtype: int64"""

df["Extracurricular"].value_counts()
"""
Extracurricular
No     4238
Yes    3478
Name: count, dtype: int64"""

df["Family_Income_Level"].value_counts()
"""
Family_Income_Level
Middle    3766
Low       1981
High      1969
Name: count, dtype: int64"""

print(df.groupby("Gender")["Hours_Studied"].mean())
"""
Gender
Female    4.992627
Male      4.981165
Name: Hours_Studied, dtype: float64"""
print(df.groupby("Gender")["Attendance"].mean())
"""
Gender
Female    80.035486
Male      79.950998
Name: Attendance, dtype: float64"""
print(df.groupby("Gender")["Sleep_Hours"].mean())
"""
Gender
Female    7.012572
Male      6.975141
Name: Sleep_Hours, dtype: float64"""
print(df.groupby("Gender")["Stress_Level"].mean())
"""
Gender
Female    5.024777
Male      5.012238
Name: Stress_Level, dtype: float64"""
df.groupby("Gender")["Screen_Time"].mean()
"""
Gender
Female    4.027953
Male      4.023169
Name: Screen_Time, dtype: float64"""
df.groupby("Gender")["Previous_GPA"].mean()
"""
Gender
Female    2.986974
Male      2.997220
Name: Previous_GPA, dtype: float64"""
df.groupby("Gender")["Tutoring_Sessions_Per_Week"].mean()
"""
Gender
Female    1.675328
Male      1.730159
Name: Tutoring_Sessions_Per_Week, dtype: float64"""
df.groupby("Gender")["Exam_Anxiety_Score"].mean()
"""
Gender
Female    4.498215
Male      4.483487
Name: Exam_Anxiety_Score, dtype: float64"""
df.groupby("Gender")["Final_Score"].mean()
"""
Gender
Female    83.229362
Male      83.237284
Name: Final_Score, dtype: float64"""

# The genders have done roughly the same things.

print(df.groupby("Gender")["Part_Time_Job"].value_counts())
"""
Gender  Part_Time_Job
Female  No               2323
        Yes              1487
Male    No               2317
        Yes              1589"""
print(df.groupby("Gender")["Diet_Quality"].value_counts())
"""
Female  Average         1874
        Good             987
        Poor             949
Male    Average         1960
        Poor            1002
        Good             944
Name: count, dtype: int64

--------Men generally have worse dietary quality.-----------------"""

print(df.groupby("Part_Time_Job")["Study_Method"].value_counts())
"""
Part_Time_Job  Study_Method
No             Offline         1838
               Hybrid          1403
               Online          1399
Yes            Offline         1225
               Online           971
               Hybrid           880
Name: count, dtype: int64


While online work has become the second choice for part-time employees after offline work, hybrid work has become the second choice for those who are not working."""

print(df.groupby("Part_Time_Job")["Family_Income_Level"].value_counts())
"""
Part_Time_Job  Family_Income_Level
No             Middle                 2253
               Low                    1231
               High                   1156
Yes            Middle                 1513
               High                    813
               Low                     750
Name: count, dtype: int64

Although the majority in both categories have a moderate income, we can say that those working part-time have a better household income."""

print(df.groupby("Study_Method")["Internet_Quality"].value_counts())
"""
Study_Method  Internet_Quality
Hybrid        Good                 927
              Average              650
              Excellent            467
              Poor                 239
Offline       Good                1254
              Average              889
              Excellent            630
              Poor                 290
Online        Good                 970
              Average              660
              Excellent            480
              Poor                 260
Name: count, dtype: int64

We can say that internet quality had little effect on the choice of working method."""

print(df.groupby("Diet_Quality")["Exam_Anxiety_Score"].mean())
"""
Diet_Quality
Average    4.498174 --> 4.5
Good       4.307975 --> 4.3
Poor       4.657099 --> 4.7
Name: Exam_Anxiety_Score, dtype: float64

-------------As diet quality improves, exam anxiety levels decrease.-------------------"""

print(df.groupby("Diet_Quality")["Final_Score"].mean())
"""
Diet_Quality
Average    83.313500
Good       85.318964
Poor       81.011697
Name: Final_Score, dtype: float64

---------------Final scores increased as the quality of the diet improved.------------------"""

import seaborn as sb
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
genders=df["Gender"].value_counts()
sb.barplot(x=genders.index, y=genders.values)
plt.ylim(3500,4000)
plt.title("Distribution of Genders")
plt.xlabel("Genders")
plt.ylabel("Values")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_genders.png")
plt.show()


parttime=df["Part_Time_Job"].value_counts()
plt.figure(figsize=(8,5))
sb.barplot(x=parttime.index, y=parttime.values)
plt.title("Distribution of Part Time Jobs")
plt.xlabel("Part Time Job")
plt.ylabel("Values")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_parttime.png")
plt.show()

dietquality=df["Diet_Quality"].value_counts()
plt.figure(figsize=(8,5))
sb.barplot(x=dietquality.index, y=dietquality.values)
plt.title("Distribution of Diet Quality")
plt.xlabel("Diet Qualities")
plt.ylabel("Values")
plt.tight_layout()
plt.savefig("images/distribution_of_diet.png")
plt.show()

internet=df["Internet_Quality"].value_counts()
plt.figure(figsize=(8,5))
sb.barplot(x=internet.index, y=internet.values)
plt.title("Distribution of Internet Quality")
plt.xlabel("Internet Qualities")
plt.ylabel("Values")
plt.tight_layout()
plt.savefig("images/distribution_of_internet.png")
plt.show()

income=df["Family_Income_Level"].value_counts()
plt.figure(figsize=(8,5))
sb.barplot(x=income.index, y=income.values)
plt.title("Distribution of Family Income Levels")
plt.xlabel("Family Income Levels")
plt.ylabel("Values")
plt.tight_layout()
plt.savefig("images/distribution_of_income.png")
plt.show()

gendervsparttime=df.groupby("Gender")["Part_Time_Job"].value_counts().reset_index(name="counts")
plt.figure(figsize=(8,5))
sb.barplot(data=gendervsparttime,x="Gender", y="counts",hue="Part_Time_Job")
plt.title("Part Time Jobs by Gender")
plt.xlabel("Gender")
plt.tight_layout()
plt.savefig("images/distribution_of_gendervsparttime.png")
plt.show()


gendervsdiet=df.groupby("Gender")["Diet_Quality"].value_counts().reset_index(name="count")
plt.figure(figsize=(8,5))
sb.barplot(data=gendervsdiet,x="Gender", y="count",hue="Diet_Quality")
plt.title("Diet Quality by Gender")
plt.xlabel("Genders")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_gendervsdiet.png")
plt.show()

parttimevsstudy=df.groupby("Part_Time_Job")["Study_Method"].value_counts().reset_index(name="count")
plt.figure(figsize=(8,5))
sb.barplot(data=parttimevsstudy,x="Part_Time_Job", y="count",hue="Study_Method")
plt.title("Study Method by Part Time Jobs")
plt.xlabel("Part Time Job Choice")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_parttimevsstudy.png")
plt.show()

parttimevsincome=df.groupby("Part_Time_Job")["Family_Income_Level"].value_counts().reset_index(name="count")
plt.figure(figsize=(8,5))
sb.barplot(data=parttimevsincome,x="Part_Time_Job", y="count",hue="Family_Income_Level")
plt.title("Family Income Level by Part Time Job")
plt.xlabel("Part Time Job Choice")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_parttimevsincome.png")
plt.show()

dietvsanxiety=df.groupby("Diet_Quality")["Exam_Anxiety_Score"].mean()
plt.figure(figsize=(8,5))
plt.ylim(4,5)
sb.barplot(x=dietvsanxiety.index, y=dietvsanxiety.values)
plt.title("Average Exam Anxiety Score by Diet Quality")
plt.xlabel("Diet Quality")
plt.ylabel("Average Exam Anxiety Score")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_dietvsanxiety.png")
plt.show()

dietvsfinalscore=df.groupby("Diet_Quality")["Final_Score"].mean()
plt.figure(figsize=(8,5))
plt.ylim(80,90)
sb.barplot(x=dietvsfinalscore.index, y=dietvsfinalscore.values)
plt.title("Average Final Score by Diet Quality")
plt.xlabel("Diet Quality")
plt.ylabel("Average Final Score")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_dietvsfinalscore.png")
plt.show()

# Students with better diet quality consistently achieve higher final scores.
# This suggests that lifestyle factors, not just academic effort, play a meaningful role in academic success.

sleepvsfinal=df.groupby("Sleep_Hours")["Final_Score"].mean()
plt.figure(figsize=(8,5))
sb.scatterplot(x=sleepvsfinal.index, y=sleepvsfinal.values)
plt.title("Average Final Score by Sleep Hours")
plt.xlabel("Sleep Hours")
plt.ylabel("Average Final Score")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_sleepvsfinal.png")
plt.show()

agevsscreen=df.groupby("Age")["Screen_Time"].mean().reset_index(name="count")
plt.figure(figsize=(8,5))
sb.lineplot(data=agevsscreen,x="Age", y="count")
plt.title("Average Screen Time by Age")
plt.xlabel("Age")
plt.ylabel("Average Screen Time (hour)")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_agevsscreen.png")
plt.show()

attendencevsfinal=df.groupby("Attendance")["Final_Score"].mean()
plt.figure(figsize=(8,5))
sb.scatterplot(x=attendencevsfinal.index, y=attendencevsfinal.values)
plt.title("Average Final Score by Attendence")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Final Score")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_attendencevsfinal.png")
plt.show()

anxietyvsfinal=df.groupby("Exam_Anxiety_Score")["Final_Score"].mean()
plt.figure(figsize=(8,5))
sb.scatterplot(x=anxietyvsfinal.index, y=anxietyvsfinal.values)
plt.title("Final Score Time by Exam Anxiety Score")
plt.xlabel("Exam Anxiety Score")
plt.ylabel("Final Score")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_anxietyvsfinal.png")
plt.show()


anxietyvspreviousgpa=df.groupby("Exam_Anxiety_Score")["Previous_GPA"].mean()
plt.figure(figsize=(8,5))
sb.scatterplot(x=anxietyvspreviousgpa.index, y=anxietyvspreviousgpa.values)
plt.title("Average Previous GPA by Exam Anxiety Score")
plt.xlabel("Exam Anxiety Score")
plt.ylabel("Previous GPA")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_anxietyvspreviousgpa.png")
plt.show()

hoursstudiedvsfinal=df.groupby("Hours_Studied")["Final_Score"].mean()
plt.figure(figsize=(8,5))
sb.scatterplot(x=hoursstudiedvsfinal.index, y=hoursstudiedvsfinal.values)
plt.title("Final Score Time by Hours Studied")
plt.xlabel("Hours Studied")
plt.ylabel("Final Score")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_hoursstudiedvsfinal.png")
plt.show()



tutorvsfinal=df.groupby("Tutoring_Sessions_Per_Week")["Final_Score"].mean()
plt.figure(figsize=(8,5))
sb.lineplot(x=tutorvsfinal.index, y=tutorvsfinal.values)
plt.title("Final Score Time by Tutoring Sessions Per Week")
plt.xlabel("Tutoring Sessions Per Week")
plt.ylabel("Final Score")
plt.tight_layout()
plt.grid()
plt.savefig("images/distribution_of_tutorvsfinal.png")
plt.show()

plt.figure(figsize=(10,8))
sb.heatmap(df.corr(numeric_only=True),annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


"""
Top factors affecting Final Score:

1. Hours Studied (strong positive correlation: 0.59)
2. Exam Anxiety (strong negative: -0.49)
3. Tutoring Sessions (moderate positive: 0.47)
4. Previous GPA (moderate positive: 0.29)
5. Stress Level (moderate negative: -0.29)

Conclusion:
Academic performance is mostly driven by study effort and psychological factors.

Student success is not determined by a single factor.
It is a combination of effort, mental state, and lifestyle."""