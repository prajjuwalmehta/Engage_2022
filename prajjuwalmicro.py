import warnings
warnings.simplefilter(action='ignore', category=Warning)
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(page_title="Cars Data Analysis",
                  layout="wide")
st.title("Cars4U")
st.text("")
st.header('Welcome to our website')
st.markdown("***In this website we will provide you with some data analysis as well as we will help you to choose a perfect car for yourself***")

# Creating a selectbox
data_name=st.selectbox("Select Your Requirement", ("Data Analysis  ","Car Buying Guide"))
st.subheader(data_name)

# Checking the selection made 
if data_name=="Car Buying Guide":
    
        df=pd.read_csv(r"C:\Users\HP\cars_dataset\cars2_ds_final_2021.csv")
        st.write("We will help you to find a perfect car according to your requirements")
    # Making filters for user
        st.write("Select the Filter to buy a car")
        filters=st.selectbox("",("Make","Fuel Type","Body Type","Seating Capacity","Transmission Type","Drive Terrain"))
        if filters=="Make":
                 comp=st.radio("Select the company",(df["Make"].unique()))
                 st.write("The company you have chosen is ")
                 st.write(comp)
                 st.text("")
                 st.write("Use filters for further search")
                 fil=st.selectbox("",("Fuel Type","Body Type","Seating Capacity","Transmission Type","Drive Terrain"))
                 if fil=="Body Type":
                     bt=st.radio("Select the Body Type", (df.loc[df["Make"]==comp,'Body_Type'].unique()))
                     st.dataframe(df.loc[(df["Make"]==comp)&(df["Body_Type"]==bt)])
                 elif fil=="Fuel Type":
                     bt=st.radio("Select the Fuel Type", (df.loc[df["Make"]==comp,'Fuel_Type'].unique()))
                     st.dataframe(df.loc[(df["Make"]==comp)&(df["Fuel_Type"]==bt)])
                 elif fil=="Seating Capacity":
                     bt=st.radio("Select the Seating Capacity", (df.loc[df["Make"]==comp,'Seating_Capacity'].unique()))
                     st.dataframe(df.loc[(df["Make"]==comp)&(df["Seating_Capacity"]==bt)])
                 elif fil=="Transmission Type":
                     bt=st.radio("Select the Transmission TYpe", (df.loc[df["Make"]==comp,'Type'].unique()))
                     st.dataframe(df.loc[(df["Make"]==comp)&(df["Type"]==bt)])
                 elif fil=="Drive Terrain":
                     bt=st.radio("Select the Drive Terrain", (df.loc[df["Make"]==comp,'Drivetrain'].unique()))
                     st.dataframe(df.loc[(df["Make"]==comp)&(df["Drivetrain"]==bt)])
        elif filters=="Body Type":
                 bt=st.radio("Select the Body Type", (df["Body_Type"].unique()))
                 st.dataframe(df.loc[df["Body_Type"]==bt])
        elif filters=="Fuel Type":
                 ft=st.radio('Select the Fuel Type',(df["Fuel_Type"].unique()))
                 st.dataframe(df.loc[df["Fuel_Type"]==ft])
        elif filters=="Seating Capacity":
                 sc=st.radio("Select seating capacity",(df["Seating_Capacity"].unique()))
                 st.dataframe(df.loc[df["Seating_Capacity"]==sc])
        elif filters=="Transmission Type":
                 tt=st.radio("Select Transmission type",(df["Type"].unique()))
                 st.dataframe(df.loc[df["Type"]==tt])
        elif filters=="Drive Terrain":
                dt=st.radio("Select Your Drive Terrain",(df["Drivetrain"].unique()))
                st.dataframe(df.loc[df["Drivetrain"]==dt])
        st.write("use the sliders to see the details")
    
else:
    # Data Analysis
      
        st.markdown("**We will provide some insights that will be useful for your business**")  
        st.text("")
    # Reading some data
        df4=pd.read_csv(r"C:\Users\HP\cars_dataset\cleaned_autos (Recovered).csv",low_memory=False)
        df1=pd.read_csv(r"C:\Users\HP\cars_dataset\total_sales.csv")
        df2=pd.read_csv(r"C:\Users\HP\cars_dataset\consumer_behaviour.csv")
        colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
    
        st.subheader("Price Predictions ,Factor Dependency and Other Analysis")
    
    # sales in regions dataframe
        st.markdown("***Firstly let's take a look at the sales for different regions***")
        st.text("")
        
        r=st.selectbox("Select the region",(df1["Regions"].unique()))
        st.table(df1.loc[df1["Regions"]==r])
        st.text("")
        st.text("")
    
    
    
        
        #counting number of cars
        @st.experimental_memo
        def plot1():
            sns.set_style("whitegrid")
            g = sns.factorplot(y="brand", data=df4, kind="count",
                           palette="Reds_r", size=7, aspect=1.5)
            g.ax.set_title("Count of vehicles by Brand",fontdict={'size':18})
            g.ax.xaxis.set_label_text("Count of Vehicles",fontdict= {'size':16})
            g.ax.yaxis.set_label_text("Brand of Vehicles",fontdict= {'size':16})
            return g
            plt.savefig('figure.png')
        st.pyplot(plot1())
        st.write("With this graph we can see the number of cars available by each brand in our data.This graph shows that volkswagen has the highest number of cars")
        st.write("After Volkswagen there is Opel ,BMW ,Audi")    
        st.text("")
        
        
        #Average price of vehicles by vehicle type and gearbox type
        @st.experimental_memo
        def plot2():
            fig, ax = plt.subplots(figsize=(8,5))
            colors = ["#00e600", "#ff8c1a","#a180cc"]
            sns.barplot(x="vehicleType", y="price",hue="gearbox", palette=colors, data=df4)
            ax.set_title("Average price of vehicles by vehicle type and gearbox type",fontdict= {'size':12})
            ax.xaxis.set_label_text("Type Of Vehicle",fontdict= {'size':12})
            ax.yaxis.set_label_text("Average Price",fontdict= {'size':12})
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot2())
        st.write("With this Bar graph we can clearly see that automatic gearbox is costly than other type in every vehicle type")
        st.write("We can also conclude that suv cars are also costly than other vehicle types")
        st.text("")
        
        
        #Average price of vehicles by fuel type and gearbox type
        @st.experimental_memo
        def plot3():
            fig, ax = plt.subplots(figsize=(8,3))
            sns.barplot(x="fuelType", y="price",hue="gearbox", palette="husl",data=df4)
            ax.set_title("Average price of vehicles by fuel type and gearbox type",fontdict= {'size':12})
            ax.xaxis.set_label_text("Type Of Fuel",fontdict= {'size':14})
            ax.yaxis.set_label_text("Average Price",fontdict= {'size':14})
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot3())
        st.write("In this graph we can see that 'Automatic' transmission is costly in every fuel category and 'Benzin' is the costly in the fuel type and their combination makes the most expensive pair ")
        st.text("")
        
        #Average power of vehicles by vehicle type and gearbox type
        @st.experimental_memo
        def plot4():
            colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
            fig, ax = plt.subplots(figsize=(8,5))
            sns.set_palette(sns.xkcd_palette(colors))
            sns.barplot(x="vehicleType", y="powerPS",hue="gearbox",data=df4)
            ax.set_title("Average power of vehicles by vehicle type and gearbox type",fontdict= {'size':12})
            ax.xaxis.set_label_text("Type Of Vehicle",fontdict= {'size':14})
            ax.yaxis.set_label_text("Average Power",fontdict= {'size':14})
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot4())
        st.write("In this graph we can see automatic gearbox provides more power to the vehicle")
        st.write("We can also conclude that 'coupe' and 'suv' are the two vehicle types with higher power")
        st.text("")
        
        #Count of Registrations in a month
        @st.experimental_memo
        def plot5():
            sns.set_style("whitegrid")
            g = sns.catplot(y="monthOfRegistration", data=df4, kind="count",
                           palette="Blues_d", size=5, aspect=1.5)
            g.ax.set_title("Count of Registrations in a month",fontdict={'size':18})
            g.ax.xaxis.set_label_text("Count of Vehicles",fontdict= {'size':16})
            g.ax.yaxis.set_label_text("Months",fontdict= {'size':16})
            plt.savefig('figure.png')
            return g
        st.pyplot(plot5())   
        st.write("From this graph we can get the month with the highest count of car registrations ")
        st.write("'January' and 'November' are the months with highest count of registrations ")
        st.text("")
       
            
        #Finding Average Price
        
        trial = pd.DataFrame()
        for b in list(df4["brand"].unique()):
            for v in list(df4["vehicleType"].unique()):
                z = df4[(df4["brand"] == b) & (df4["vehicleType"] == v)]["price"].mean()
                trial = trial.append(pd.DataFrame({'brand':b , 'vehicleType':v , 'avgPrice':z}, index=[0]))
        trial = trial.reset_index()
        del trial["index"]
        trial["avgPrice"].fillna(0,inplace=True)
        trial["avgPrice"].isnull().value_counts()
        trial["avgPrice"] = trial["avgPrice"].astype(int)
        
        #Average price of vehicles of each brand
        @st.experimental_memo
        def plot6():
            colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
            fig, ax = plt.subplots(figsize=(8,5))
            sns.set_palette(sns.xkcd_palette(colors))
            sns.barplot(x="avgPrice", y="brand",data=trial)
            ax.set_title("Average price of vehicles of each brand",fontdict= {'size':12})
            ax.xaxis.set_label_text("Average price",fontdict= {'size':14})
            ax.yaxis.set_label_text("Brands",fontdict= {'size':14})
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot6())
        st.write("In this graph we can see the average price of each brands in our dataset and see which all brands are on the expensive side and which all brands are on the cheaper side")
        
        st.write("")
        
        #rice vs Fuel TypeP
        @st.experimental_memo
        def plot7():
            fig = plt.figure(figsize = (10,5))
            sns.barplot(x ='fuelType', y ='price', data  = df4)
            plt.title('Price vs Fuel Type',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot7())
        st.write("In this graph we can see that the cars with fuel type as 'Benzin' are priced more than other fuel types ")
        st.text("")
        
        #Power vs Gear Transmission
        @st.experimental_memo
        def plot8():
            fig = plt.figure(figsize = (10,5))
            sns.barplot(x ='gearbox', y ='powerPS', data  = df4)
            plt.title('Power vs Gear Transmission',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot8())
        st.write("From this graph it is clearly evident that automatic gearbox provides more power")
        st.text("")
        
        #Count of different types of vehicles
        @st.experimental_memo
        def plot9():
            fig = plt.figure(figsize = (20,9))
            sns.countplot(y ='vehicleType', data  = df4)
            plt.title('Count of different types of vehicles',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot9())
        st.write("From this graph we can conclude that 'Limousine','Kleinwagen' and 'Kombi' are the three most prominent types of cars")
        st.text("")
        
        
        #Average price of vehicles by vehicle type and brand
        @st.experimental_memo
        def plot10():
            tri = trial.pivot("brand","vehicleType", "avgPrice")
            fig, ax = plt.subplots(figsize=(15,15))
            sns.heatmap(tri,linewidths=1,cmap="YlGnBu",annot=True, ax=ax, fmt="d")
            ax.set_title("Average price of vehicles by vehicle type and brand",fontdict={'size':20})
            ax.xaxis.set_label_text("Type Of Vehicle",fontdict= {'size':20})
            ax.yaxis.set_label_text("Brand",fontdict= {'size':20})
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot10())
        st.write("This Graph shows average price of each car-type of all the brands")
        st.write("With the help of this brands can price their cars accordingly")
        st.text("")
        
        
        
        st.subheader("Indian car consumer behaviour Analysis")
        
        #Age , Profession and price of car
        @st.experimental_memo
        def plot11():
            colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
            fig, ax = plt.subplots(figsize=(8,5))
            sns.set_palette(sns.xkcd_palette(colors))
            sns.barplot(x="Age", y="Price",hue="Profession",data=df2)
            ax.set_title("Age , Profession and price of car",fontdict= {'size':12})
            ax.xaxis.set_label_text("Age",fontdict= {'size':14})
            ax.yaxis.set_label_text("Price",fontdict= {'size':14})
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot11())
        
        st.write("In this graph at a number of age ,the person who is salaried has purchased a car expensive than a business person")
        st.text("")
        
        
        #Total Salary and Price
        @st.experimental_memo
        def plot12():
            colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
            fig, ax = plt.subplots(figsize=(8,5))
            sns.set_palette(sns.xkcd_palette(colors))
            sns.barplot(x="Total Salary", y="Price",hue="Wife Working",data=df2)
            ax.set_xticklabels(ax.get_xticklabels(),rotation = 45)
            ax.set_title("Total Salary and Price",fontdict= {'size':12})
            ax.xaxis.set_label_text("Total Salary",fontdict= {'size':14})
            ax.yaxis.set_label_text("Price",fontdict= {'size':14})
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot12())
        st.write("From this graph we can conclude that total salary of the person increases as if that person's wife is working")
        st.write("But despite the increase in total salary of a person there is no such increase in the price of the car that person buys")
        st.text("")
        
        
        
        #Price vs Home Loan
        @st.experimental_memo
        def plot13():
            fig = plt.figure(figsize = (10,5))
            sns.barplot(x ='House Loan', y ='Price', data  = df2)
            plt.title('Price vs Home Loan',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot13())    
        st.write("With the help of this graph we can clearly se that a person which is not having a Home loan is tend to buy a car more expensive than the person who have a Home loan")
        st.text("") 
        
        #Price vs Personal loan
        @st.experimental_memo
        def plot14():
            fig = plt.figure(figsize = (10,5))
            sns.barplot(x ='Personal loan', y ='Price', data  = df2)
            plt.title('Price vs Personal loan',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot14())
        st.write("With the help of this graph we can clearly se that a person which is not having a Personal loan is tend to buy a car more expensive than the person who have a Personal loan")
        st.text("") 
        
        #Price vs Marrital
        @st.experimental_memo
        def plot15():
            fig = plt.figure(figsize = (10,5))
            sns.barplot(x ='Marrital Status', y ='Price', data  = df2)
            plt.title('Price vs Marrital Status',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot15())
        st.write("With the help of this graph we can conclude that a person who is married buys a more expensive car than a person who is single")
        st.text("")
        
        #Price vs Wife Working or no
        @st.experimental_memo
        def plot16():
            fig = plt.figure(figsize = (10,5))
            sns.barplot(x ='Wife Working', y ='Price', data  = df2)
            plt.title('Price vs Wife Working or not',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot16())
        st.write("With the help of this graph we can conclude that if a person's wife working than that person buys a more expensive car ")
        st.text("")
        
        #Price vs Education
        @st.experimental_memo
        def plot17():
            fig = plt.figure(figsize = (10,5))
            sns.barplot(x ='Education', y ='Price', data  = df2)
            plt.title('Price vs Education',fontsize  =25)
            plt.savefig('figure.png')
            return fig
        st.pyplot(plot17())
        st.write("From this graph we can conclude that a person who is 'Post Graduate' buys a more expensive car than a person who is 'Graduate'")
        st.write("")
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    