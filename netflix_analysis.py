import pandas as pd
import matplotlib.pylab as plt

df=pd.read_csv("netflix/netflix_data.csv")

print(df.info())
#Columns
print("\nColumns:\n",df.columns)
#Shape
print("Rows and columns in Data:\n",df.shape)
#Describe
print("Description:\n",df.describe())
#Null values in each column
print("Null Count:\n",df.isnull().sum())
#duplicate rows
print("Duplicated Rows:\n",df.duplicated().sum())

#Drop Missing Values
df=df.dropna(subset=["date_added","rating","duration"])

df.columns=df.columns.str.strip().str.title()
print(df.columns)

#Date Parsing
df["Date_Added"]=pd.to_datetime(df["Date_Added"],format='mixed')
print(df["Date_Added"].head(10))

#Movies and TV show count
Count=(df.groupby("Type")["Title"].count())
print(Count)

#Visualization
plt.figure(figsize=(8,6))
Count.plot(kind="bar",label="Movie Vs TV ",color="green")
plt.title("Movies Vs TV Shows Count",size=12)
plt.xlabel("Type Of Show",size=12)
plt.ylabel("Show Count",size=12)
plt.grid(True,linestyle="--",color="grey")
plt.tight_layout()
plt.savefig("netflix/type_compare.png",dpi=300,bbox_inches="tight")

plt.close()

#Content Rating Distribution
rating_count=df.groupby("Rating")["Title"].count()
rating_count.plot(kind="bar",color="purple",label="Rating Distribution")
plt.title("Content Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Number of Titles")
plt.grid(True,linestyle="--",color="grey")
plt.legend()
plt.tight_layout()
plt.savefig("netflix/ratings.png",dpi=300,bbox_inches="tight")

plt.close()

#Top 10 Country
top10_country=df["Country"].str.split(',').explode().str.strip().value_counts().head(10)
print(top10_country)
#Visualization
plt.figure(figsize=(10,6))

top10_country.plot(kind="bar", color="orange")
plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.grid(True,linestyle="--",color="grey")
plt.tight_layout()
plt.savefig("netflix/topcountry.png",dpi=300,bbox_inches="tight")
plt.close()

#TOP 10 Directors
top10_direct=df.groupby("Director")["Title"].count().sort_values(ascending=False).head(10)
print(top10_direct)

#Bar Chart
top10_direct.plot(kind="bar", color="green")
plt.title("Top 10 Directors by Netflix Content")
plt.xlabel("Directors")
plt.ylabel("Number of Titles")
plt.xticks(rotation=40)
plt.grid(True,linestyle="--",color="grey")
plt.tight_layout()
plt.savefig("netflix/topdirector.png",dpi=300,bbox_inches="tight")
plt.close()

#Most common Genres
common_genre=df["Listed_In"].str.split(",").explode().str.strip().value_counts().head(5)

#Bar Chart
plt.figure(figsize=(7,4))
common_genre.plot(kind="bar", color="red")
plt.title("Most Common Genres")
plt.xlabel("Genres")
plt.ylabel("Number of Titles")
plt.grid(True,linestyle="--",color="grey")
plt.tight_layout()
plt.savefig("netflix/genre.png",dpi=300,bbox_inches="tight")
plt.close()

#Content Added Each Year
df["Added_Year"]=df["Date_Added"].dt.year

Content_each_yr=df.groupby("Added_Year")["Title"].count()


Content_each_yr.plot(kind='bar',color='pink')
plt.title("Content Added Each Year")
plt.xlabel("Content Added Year ")
plt.ylabel("Number of Titles")
plt.grid(True,linestyle="--",color="grey")
plt.tight_layout()
plt.savefig("netflix/content_year.png",dpi=300,bbox_inches="tight")

plt.close()

#Releases by Year
release_year=df.groupby("Release_Year")["Title"].count()
print("\nReleases per Year:\n",release_year)



extracted = df["Duration"].str.extract(r"(\d+)")
print(extracted.head())
print(extracted.isna().sum())

#Longest Movie
df["Duration_num"] = df["Duration"].str.extract(r"(\d+)")[0].astype(int)

print(df[["Duration", "Duration_num"]].head())
max_time=(df[df["Type"]=="Movie"]["Duration_num"]).max()
print("Longest Duration of Movie:",max_time)
max_movie=df.loc[(df["Duration_num"]==max_time)&(df["Type"]=="Movie"),"Title"].tolist()
print("Longest Duration Movie Name:",max_movie)

#Longest TV Show
df["Duration_num"] = df["Duration"].str.extract(r"(\d+)")[0].astype(int)

max_time=(df[df["Type"]=="TV Show"]["Duration_num"]).max()
print("Longest Duration of TV Show:",max_time)
max_movie=df.loc[(df["Duration_num"]==max_time)&(df["Type"]=="TV Show"),"Title"].tolist()
print("Longest Duration TV Show Name:",max_movie)

#oldest Movie
old=df[df["Type"]=="Movie"]["Release_Year"].min()
title=df.loc[(df["Type"]=="Movie") & (df["Release_Year"]==old),"Title"]
print("Oldest Movie Title:\n",title.tolist()) 
print("Year of Release:",old)

# Find the number of titles added in each month.
df["Month_Name"]=df["Date_Added"].dt.month_name()
added_count=df.groupby("Month_Name")["Show_Id"].count()
months=[
"January","February","March",
"April","May","June",
"July","August","September",
"October","November","December"
]

added_count=added_count.reindex(months)
print("Month with most Addition of Content:",added_count.idxmax())
print("Month with least Addition of Content:",added_count.idxmin())

#Visualization of  addition of movies over month
added_count.plot(kind="bar",color="y")
plt.title("Titles Added over Months")
plt.xlabel("Months")
plt.ylabel("Content Added")
plt.grid(True,linestyle="--")
plt.tight_layout()
plt.savefig("netflix/movie_add.png",dpi=300,bbox_inches="tight")

plt.close()

#Top Actors
top_actors=df["Cast"].str.split(',').explode().str.strip().value_counts().sort_values(ascending=False).head(10)
print(top_actors)

#Duration Distribution(Movies)
movie_duration=df[df["Type"]=="Movie"]["Duration_num"]
plt.figure(figsize=(10,6))  
plt.hist(movie_duration,bins=20,color="purple",edgecolor="black")
plt.title("Distibution of Time Duration of Movies")
plt.xlabel("Time Duration (mins)")
plt.ylabel("Number of Title")
plt.tight_layout()
plt.savefig("netflix/movie_distribution.png",dpi=300,bbox_inches="tight")
plt.close()

#Duration Distribution(TV Shows)
show_duration=df[df["Type"]=="TV Show"]["Duration_num"]
plt.figure(figsize=(10,6))  
plt.hist(show_duration,bins=15,color="purple",edgecolor="black")
plt.title("Distibution of Time Duration of TV Shows")
plt.xlabel("Number Of Seasons")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.savefig("netflix/show_distribution.png",dpi=300,bbox_inches="tight")

plt.close()

#Missing Value Visualization
missing_values=df.isnull().sum()
missing_values[missing_values>0].plot(kind="bar",color="y",figsize=(7,4))
plt.title("Missing Values")
plt.xlabel("Columns")
plt.ylabel("Missing Value Count")
plt.grid(True)
plt.tight_layout()
plt.savefig("netflix/Missing.png",dpi=300,bbox_inches="tight")

plt.close()

