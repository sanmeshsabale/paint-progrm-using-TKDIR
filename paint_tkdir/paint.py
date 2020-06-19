from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
from tkinter import messagebox


root = Tk()
root.title('Paint Program by me')
root.geometry("800x800")

brush_color= 'black'

def paint(e):
    #Starting Position
    x1 =e.x - 1
    y1 =e.y - 1

    # Ending Position
    x2 =e.x + 1
    y2 =e.y + 1

    # Brush Parameters
    brush_width='%0.0f' % float(my_slider.get())
    #brush_color='red'
    #Brush types BUTT, ROUND, PROJECTING
    brush_type2= brush_type.get()

    # Draw on the  Canvas
    my_canvas.create_line(x1, y1, x2, y2, fill=brush_color,width=brush_width, capstyle=brush_type2, smooth=True)
#change the size of brush_type
def change_brush_size(thing):
    slider_label.config(text='%0.0f' % float(my_slider.get()))

def change_brush_color():
    global brush_color
    brush_color = 'black'
    brush_color = colorchooser.askcolor(color=brush_color)[1]

def change_canvas_color():
    global bg_color
    bg_color = 'black'
    bg_color = colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg=bg_color)

def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg='white')

def save_as_image():
    result= filedialog.asksaveasfilename(initialdir='C:/Users/Admin/Desktop/paint_tkdir/Images', filetypes=(("png files","*.png"),("all files","*.*")))
    if result.endswith('.png'):
        pass
    else:
        result = result + '.png'
    if result:
        x=root.winfo_rootx()+my_canvas.winfo_x()
        y=root.winfo_rooty()+my_canvas.winfo_y()
        x1=x+my_canvas.winfo_width()
        y1=y+my_canvas.winfo_height()
        ImageGrab.grab().crop((x,y,x1,y1)).save(result)

        #pop up messagebox
        messagebox.showinfo("image Saved","Your Image has been Saved")


#create our canvas
w = 600
h = 400
my_canvas=Canvas(root, width=w, height=h, bg='white')
my_canvas.pack(pady=20)

# my_canvas.create_line(0, 100, 300, 100, fill='red')
# my_canvas.create_line(150, 0, 150, 200, fill='blue')

my_canvas.bind('<B1-Motion>', paint)

#create brush option frame
brush_option_frame = Frame(root)
brush_option_frame.pack(pady=20)

#bruash size
brush_size_frame = LabelFrame(brush_option_frame, text='Brush Size')
brush_size_frame.grid(row=0, column=0, padx=100)
# brush slider
my_slider=ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient= VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

#brush slider LabelFrame
slider_label=Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# brush types
brush_type_frame = LabelFrame(brush_option_frame, text='Brush Type', height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type=StringVar()
brush_type.set("round")

#create radio button for brush type
brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change color
change_colors_frame = LabelFrame(brush_option_frame, text='Change Color')
change_colors_frame.grid(row=0, column=2)

#change brush color button
brush_color_button = Button(change_colors_frame, text='Brush Color', command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

#change canvas background Color
canvas_color_button = Button(change_colors_frame, text='Background Color', command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)

# program Option frame
option_frame = LabelFrame(brush_option_frame, text= 'Program Option')
option_frame.grid(row=0, column=3, padx=50)

#clear Screen Buttoon
clear_button = Button(option_frame, text='Clear Screen', command= clear_screen)
clear_button.pack(padx=10, pady=10)

#save image
save_image_button= Button(option_frame, text='Save to Image', command=save_as_image)
save_image_button.pack(pady=10, padx=10)





root.mainloop()
