import streamlit as st
import json
import os


def get_zodiac_sign(day, month):
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    else:
        return "Please enter a valid date or month!"

def main():
    st.title("Zodiac Sign Finder")
    st.write("Enter your name & birth date to find out your zodiac sign.")

    personName = st.text_input("Enter your name: ").capitalize()
    birthdate = st.text_input("Enter you birth date: ")
    birthmonth = st.text_input("Enter you birth month: ")
    button = st.button("Check")
    if button:
        day = int(birthdate)
        month = int(birthmonth)
        zodiac_sign = get_zodiac_sign(day, month)
        st.subheader("Your Zodiac Sign:")
        st.write(zodiac_sign)

        database = {
        "name": personName,
        "birth_date": day,
        "birth_month": month,
        "zodiac_sign": zodiac_sign
        }

        if not os.path.exists('./database'):
            os.mkdir('./database')
            with open(f"database/{personName}.json", "w") as file:
                data = json.dumps(database)
                file.write(data)
                st.success("File created successfully!")
        else:
            with open(f"database/{personName}.json", "w") as file:
                data = json.dumps(database)
                file.write(data)
                st.success("File updated successfully!")


if __name__ == "__main__":
    main()