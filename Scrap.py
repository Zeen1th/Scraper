import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def scrape_and_save():
    url = url_entry.get()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        text_content = soup.find("div", class_="entry-content").get_text()

        with open("extracted_text.txt", "w", encoding="utf-8") as file:
            file.write(text_content)

        messagebox.showinfo("Success", "Text has been successfully extracted and saved to 'extracted_text.txt'.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


root = tk.Tk()
root.title("Web Scraping App")


url_label = tk.Label(root, text="Enter URL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()


scrape_button = tk.Button(root, text="Scrape and Save", command=scrape_and_save)
scrape_button.pack()


root.mainloop()
