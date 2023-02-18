# EDA-domestic-violence
_*I want to make clear that this project is only for my learning process.*_

The present EDA is based on the dataset provided by DIJIN (Directorate of Criminal Investigation and INTERPOL of the National Police) and National Police from Colombia, which contains updates about data from all over the country on domestic violence reported between 2010 and 2022, the most recent of which was on December 9 (Last update).

[**Source**](https://www.datos.gov.co/Seguridad-y-Defensa/Reporte-Delito-Violencia-Intrafamiliar-Polic-a-Nac/vuyt-mqpw)

----

## This EDA contains three notebooks:
1. data-cleaning, where I did data cleaning process and exported raw and cleaned data
2. Domestic-violenceEDA-v1, where all the great stuff was done, I presented results as answering different questions I had and giving out some insights about the data.
3. data-profile-report, where there is a nice-looking report from pandas_profiling library which shows main aspects of the data, descriptive aspects and the distribution of it.

----

## Here's an overview of what I found analyzing the data:

- _*Insight 1:*_ there is not a common distribution nor a consistent one.

- _*Insight 2:*_ In the date, we can see how 2020 had a great increase on cases, we'll talk about this later in time series analysis.
In the cases, there's a big concentration of 1 to 2 cases per row.

- _*Answer question 1*_: the distribution of cases across the country is concentrated on the center part of the country, as expected thanks to the fact that a great amount of population is located on this region.

- _*Answer question 2:*_ The most common type of gun used in domestic violence cases in Colombia is handgun, followed by unarmed. It's interesting to see how handgun is far more used that the others, specially firearm and scopolamine.

- _*Answer question 3:*_ female (FEMENINO) sex is the most common **victim.**

- _*Answer question 4:*_ As observed here, the majority of affected individuals are adult females, whereas there is little variation in the number of affected minors between males and females.

- _*Definition:*_ What is scopolamine? Scopolamine is a drug used to treat motion sickness and nausea, but it can also be abused to cause amnesia and delirium. It has been used in crimes, including "date rape" due to its ability to be surreptitiously administered in drinks. Scopolamine is a potent drug that should only be used under the guidance of a medical professional. 

- _*Insight 4:*_ It is true that scopolamine usage is concentrated primarily in the central region of the country, with a significant presence observed in Bogotá, the capital of Colombia. This city also has the highest number of cases involving the use of scopolamine in domestic violence incidents, in comparison to other regions.

### Time series analysis conclusions
- We can see how cases by month have a stable tendency except for December, this month has a sharp decrease which may be due to the holidays celebrated during this part of the year.
Likewise, Sundays, which is the day of rest in Colombia, is the day with the highest number of cases of the week.

- We can conclude by the graphs above that every end of December and beginning of January, holidays in colombia, there is an increase on cases reported, every year this happens all over the country.
Pandemic 2020 caused an extreme increase of reports due to the sanitary measures taken by the government in which it was forbidden to leave the house for safety reasons.
