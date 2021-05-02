from tkinter import *
import csv

root = Tk()
root.title('IMDB')

movies_li = []

with open('movies.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        movies_li.append(row)

def info(movie):
    print(movie)

row = 0
for data in movies_li:
    movie = data[0]
    cur_btn = 'btn'+str(row)
    #command=lambda: info(movie)
    cur_btn = Button(root, text=movie,relief="sunken", width=50, command=lambda: info(movie)).grid(row=row, column=0)
    row += 1
print(btn0)
root.mainloop()
