from serpapi import GoogleSearch
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def compare(med_name):
    params = {
    "engine": "google_shopping",
    "q": "med_name",
    "api_key": "68185e77c5e65e4e7fa3c280f5140494cdbd1851a32837bff6e4e2531ba98104"
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results['shopping_results']
    return shopping_results



c1,c2 = st.columns(2)
with c1:
    st.image("e_pharmacy.png",width=200)
with c2:
    st.header("E-pharmacy price comparison system")

# """___________________________________________________________"""

st.sidebar.title("Enter name of medicine:")
med_name = st.sidebar.text_input("Enter name here:")
number = st.sidebar.text_input("Enter number of options here:")
medcine_comp = []
med_price = []


if med_name is not None:
    if st.sidebar.button("price compare"):
        shopping_results = compare(med_name)
        lowest_price =float ((shopping_results[0].get('price'))[1:])
        print(lowest_price)
        lowest_price_index = 0
        st.sidebar.image(shopping_results[0].get('thumbnail'))


        for i in range(int(number)):
            current_price = float ((shopping_results[i].get('price'))[1:])
            medcine_comp.append(shopping_results[i].get('source'))
            med_price.append(float((shopping_results[i].get('price'))[1:]))

            #_____________________________________________________________________

            st.title(f"option {i+1}")
            c1,c2 = st.columns(2)
            c1.write("Company:")
            c2.write(shopping_results[i].get('source'))

            c1.write("Title:")
            c2.write(shopping_results[i].get('title'))

            c1.write("price:")
            c2.write(shopping_results[i].get('price'))

            url = shopping_results[i].get('product_link')

            c1.write("Buy Link:")
            c2.write("[Link](%s)" % url)

            """___________________________________________________________"""
            if (str(current_price)) < (str(lowest_price)):
                lowest_price = current_price
                lowest_price_index = i

        # this is best option
        st.title("best option:")
        c1,c2 = st.columns(2)
        c1.write("Company:")
        c2.write(shopping_results[lowest_price_index].get('source'))

        c1.write("Title:")
        c2.write(shopping_results[i].get('title'))

        c1.write("price:")
        c2.write(shopping_results[i].get('price'))

        url=shopping_results[i].get('product_link')

        c1.write("Buy Link:")
        c2.write("[Link](%s)"%url)

        #________________________
        # grpahs comparision
        df=pd.DataFrame(med_price,medcine_comp)
        st.title("chart comparison:")
        st.bar_chart(df)

        fig,ax=plt.subplots()
        ax.pie(med_price,labels=medcine_comp,shadow= True)
        ax.axis("equal")
        st.pyplot(fig)




