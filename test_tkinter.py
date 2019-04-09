from tkinter import *

class GUI_Cat:
    '''Represents a software for managing record collections'''


    #Constructs the object that holds the tkinter's frames and the widgets
    def __init__(self, master):
        self.master = master
        master.title('Records Catalogue')

        #Creates the top frame
        topframe = Frame(master, width = 2500,
                                      height = 400, bg = 'lightgrey')
        topframe.pack()

        #Creates the bottom frame
        bottomframe = Frame(master, width = 2500,
                                            height= 600, bg='darkgrey')
        bottomframe.pack(side=BOTTOM)


        #creates labels and entries to the top frame
        artist_label = Label(topframe, text='Artist:')
        artist_entry = Entry(topframe)
        ep_lp_label = Label(topframe, text='EP/LP:')
        ep_lp_entry = Entry(topframe)
        rec_lab_label = Label(topframe, text='Lable:')
        rec_lab_entry = Entry()
        date_release_label = Label(topframe, text='Date of Release:')
        date_release_entry = Entry()
        date_purchase_label = Label(topframe, text='Date of Purchase:')
        date_purchase_entry = Entry()
        condition_label = Label(topframe, text='Condition:')
        condition_entry = Entry()
        cover_label = Label(topframe, text='Cover:')
        cover_entry = Entry()

        #Creates a list to store Lables and Entries
        labels = [artist_label, ep_lp_label, rec_lab_label, date_release_label, date_purchase_label,
                       condition_label, cover_label]

        entries = [artist_entry, rec_lab_entry, date_release_entry,
                        date_purchase_entry, condition_entry, cover_entry]


        count = 0

        






root = Tk()
Rec_Cat = GUI_Cat(root)
root.mainloop()
