from tkinter import *
from PIL import Image, ImageTk
import pickle
import pandas as pd
import webbrowser

def open_github(event):
    webbrowser.open("https://github.com/Fen1Xcz?tab=repositories")


with open('Recomm_Model.data', 'rb') as file:
    loaded_model = pickle.load(file)

app = Tk()
app.title("Game Recommendator")
app.geometry("1400x800")
app.resizable(False, False)  # Zakáže rozšíření nebo zmenšení okna

background_photo = Image.open("galaxy_background.jpg")
background_photo = ImageTk.PhotoImage(background_photo)  # Convert na PhotoImage

main_window_canvas = Canvas(app, width=1400, height=800)
main_window_canvas.pack(fill=BOTH, expand=True)
main_window_canvas.create_image(0, 0, image=background_photo, anchor=NW)

about_text = main_window_canvas.create_text(700, 600,
                                              text="So, this is my program for giving you recommendations for games.\nClick one of these "
                                                   "buttons and choose where you want to go first, \nthough I'd recommend you to go first to"
                                                   " the Explanation of Terms.\nDon't worrry, this page will stay here and won't dissapear "
                                                   "once you \nclick one of the buttons above :D ",
                                              font=("Comic Sans MS", 20), fill="#ff008f")

welcome_text = main_window_canvas.create_text(700, 100, text="Welcome to Game Recommendator (:",
                                              font=("Comic Sans MS", 32), fill="crimson")
author_text_link = Label(main_window_canvas, text="Made by Michal Charvát", font=("Comic Sans MS", 12), fg="white", bg="midnightblue")
author_text_link.place(x=575, y=750)
author_text_link.bind("<Button-1>", open_github) #<"Button-1"> left mouse button click

def on_enter3(event):
    author_text_link.config(fg="#00d1ff")

def on_leave3(event):
    author_text_link.config(fg="white")

author_text_link.bind("<Enter>", on_enter3)
author_text_link.bind("<Leave>", on_leave3)

logo_image = Image.open("GR_logo_background.jpg")
logo_photo = ImageTk.PhotoImage(logo_image)
app.iconphoto(False, logo_photo)

logo_in_app = Image.open("GR_logo.png")
logo_in_app_photo = ImageTk.PhotoImage(logo_in_app)
photo_label = main_window_canvas.create_image(700, 325, image=logo_in_app_photo)

def open_page_1():
    app_page_1 = Toplevel(app)
    app_page_1.title("Explanation of Terms")
    app_page_1.geometry("850x500")
    app_page_1.iconphoto(False, logo_photo)
    app_page_1.resizable(False, False)
    page_1_canvas = Canvas(app_page_1, width=1000, height=600)
    page_1_canvas.pack(fill=BOTH, expand=True)
    page_1_canvas.create_image(0, 0, image=background_photo, anchor=NW)
    the_app = page_1_canvas.create_image(425, 250, image=logo_in_app_photo)
    explanation_of_words = page_1_canvas.create_text(425, 50, text="Explanation of Terms", font=("Comic Sans MS", 20),fill="crimson")
    user_rating_label = Label(page_1_canvas, text="User Rating: The average from all the people that rated this game.", font=("Comic Sans MS", 18), fg="white",
                              bg="midnightblue")
    user_rating_label.place(x=50, y=100)

    total_ratings_label = Label(page_1_canvas, text="Total Ratings: The number of people that rated this game.", font=("Comic Sans MS", 18), fg="white",
                                bg="midnightblue")
    total_ratings_label.place(x=50, y=150)

    metacritic_score_label = Label(page_1_canvas, text="Metacritic Score: Rating from professional critics.", font=("Comic Sans MS", 18), fg="white",
                                   bg="midnightblue")
    metacritic_score_label.place(x=50, y=200)

    price_label = Label(page_1_canvas, text="Price: How much does the game cost.", font=("Comic Sans MS", 18), fg="white", bg="midnightblue")
    price_label.place(x=50, y=250)

    release_year_label = Label(page_1_canvas, text="Release Year: The year, when the game was released to the public. "
                                                   "\n(As in the full version, pre-versions doesn't count.)", font=("Comic Sans MS", 18), fg="white",
                               bg="midnightblue")
    release_year_label.place(x=50, y=300)


def open_page_2():
    app_page_2 = Toplevel(app)
    app_page_2.title("Recommendation Calculator")
    app_page_2.geometry("850x500")
    app_page_2.iconphoto(False, logo_photo)
    app_page_2.resizable(False, False)
    page_2_canvas = Canvas(app_page_2, width=1000, height=500)
    page_2_canvas.pack(fill=BOTH, expand=True)
    page_2_canvas.create_image(0, 0, image=background_photo, anchor=NW)
    the_app = page_2_canvas.create_image(425, 250, image=logo_in_app_photo)

    Label(app_page_2, text="→User Rating → Accepts only number from 0 to 5", font=("Comic Sans MS", 14), fg="cyan", bg="midnightblue").place(x=295, y=50)
    user_rating_entry = Entry(app_page_2, font=("Comic Sans MS", 14), fg="magenta", bg="midnightblue")
    user_rating_entry.place(x=50, y=50)

    Label(app_page_2, text="→Total Ratings → Accepts only number from 0 to 100,000", font=("Comic Sans MS", 14), fg="cyan", bg="midnightblue").place(x=295, y=100)
    total_ratings_entry = Entry(app_page_2, font=("Comic Sans MS", 14), fg="magenta", bg="midnightblue")
    total_ratings_entry.place(x=50, y=100)

    Label(app_page_2, text="→Metacritic Score → Accepts only number from 0 to 100", font=("Comic Sans MS", 14), fg="cyan", bg="midnightblue").place(x=295, y=150)
    metacritic_score_entry = Entry(app_page_2, font=("Comic Sans MS", 14), fg="magenta", bg="midnightblue")
    metacritic_score_entry.place(x=50, y=150)

    Label(app_page_2, text="→Price → Accepts only number from 0 to 1000", font=("Comic Sans MS", 14), fg="cyan", bg="midnightblue").place(x=295, y=200)
    price_entry = Entry(app_page_2, font=("Comic Sans MS", 14), fg="magenta", bg="midnightblue")
    price_entry.place(x=50, y=200)

    Label(app_page_2, text="→Release Year → Accepts only number from 1900 to 2025", font=("Comic Sans MS", 14), fg="cyan", bg="midnightblue").place(x=295, y=250)
    release_year_entry = Entry(app_page_2, font=("Comic Sans MS", 14), fg="magenta", bg="midnightblue")
    release_year_entry.place(x=50, y=250)

    error_label = Label(app_page_2, text="", font=("Comic Sans MS", 14), fg="red", bg="black")
    error_label.place(x=50, y=300)

    def on_enter2(event):
        event.widget.config(bg="#00758c")

    def on_leave2(event):
        event.widget.config(bg="midnightblue")

    user_rating_entry.bind("<FocusIn>", on_enter2)
    user_rating_entry.bind("<FocusOut>", on_leave2)
    total_ratings_entry.bind("<FocusIn>", on_enter2)
    total_ratings_entry.bind("<FocusOut>", on_leave2)
    metacritic_score_entry.bind("<FocusIn>", on_enter2)
    metacritic_score_entry.bind("<FocusOut>", on_leave2)
    price_entry.bind("<FocusIn>", on_enter2)
    price_entry.bind("<FocusOut>", on_leave2)
    release_year_entry.bind("<FocusIn>", on_enter2)
    release_year_entry.bind("<FocusOut>", on_leave2)
    def calculate_recommendation():
        error_label.config(text="")
        result_label.config(text="")

        try:
            user_rating = float(user_rating_entry.get())
            if user_rating < 0 or user_rating > 5:
                error_label.config(text="User Rating must be between 0 and 5.")
                return

            total_ratings = int(total_ratings_entry.get())
            if total_ratings < 0 or total_ratings > 100000:
                error_label.config(text="Total Ratings must be between 0 and 100,000.")
                return

            if  user_rating == 0 and total_ratings != 0:
                error_label.config(text="If User Rating is 0, Total Ratings must also be 0.")
                return
            if total_ratings == 0 and user_rating != 0:
                error_label.config(text="If Total Ratings is 0, User Rating must also be 0.")
                return

            metacritic_score = int(metacritic_score_entry.get())
            if metacritic_score < 0 or metacritic_score > 100:
                error_label.config(text="Metacritic Score must be between 0 and 100.")
                return

            price = float(price_entry.get())
            if price < 0 or price > 1000:
                error_label.config(text="Price must be between 0 and 1000.")
                return

            release_year = int(release_year_entry.get())
            if release_year < 1900 or release_year > 2025:
                error_label.config(text="Release Year must be between 1900 and 2025.")
                return

            features = pd.DataFrame({'User Rating': [user_rating], 'Total Ratings': [total_ratings], 'Metacritic Score': [metacritic_score], 'Price': [price], 'Release Year': [release_year]})

            recommendation = loaded_model.predict(features)

            result_label.config(text=f"Recommendation: {recommendation[0]}")

        except ValueError:
            error_label.config(text="Please enter valid numbers.", font=("Comic Sans MS", 14))

    calculate_button = Button(app_page_2, text="Calculate!", command=calculate_recommendation, font=("Comic Sans MS", 16), fg="cyan", bg="midnightblue")
    calculate_button.place(x=50, y=350)

    result_label = Label(app_page_2, text="", font=("Comic Sans MS", 16), fg="blue", bg="magenta")
    result_label.place(x=50, y=400)


def on_enter(event):
    event.widget.config(bg="midnightblue")

def on_leave(event):
    event.widget.config(bg="cyan")


button1 = Button(main_window_canvas, text="Explanation \nof Terms", command=open_page_1, bg="cyan", fg="black",
                 font=("Comic Sans MS", 14), relief="groove", width=18, height=5)
button1.bind("<Enter>", on_enter)
button1.bind("<Leave>", on_leave)
main_window_canvas.create_window(200, 300, window=button1)

button2 = Button(app, text="Recommendation \nCalculator", command=open_page_2, bg="cyan", fg="black", # fg je písmo, bg je background toho buttonu
                 font=("Helvetica", 16), relief="ridge", width=18, height=5)
button2.bind("<Enter>", on_enter)
button2.bind("<Leave>", on_leave)
main_window_canvas.create_window(1200, 300, window=button2)

app.mainloop()