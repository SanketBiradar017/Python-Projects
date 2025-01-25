from tkinter import *
import random
from tkinter import messagebox
import pandas as pd
import os
from fpdf import FPDF  # Import FPDF for PDF generation

class Bill_App:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#2C3E50")  # Darker background for the main window
        self.root.title("Chaat Billing System")

        title = Label(self.root, text="Chaat Billing System", bd=12, relief=RIDGE, font=("Arial Black", 20),
                      bg="#2980B9", fg="white").pack(fill=X)  # Title color
        # Add Menu Button
        menu_button = Button(self.root, text="Menu", font=("Arial Black", 14), bg="#E5B4F3", fg="#6C3483",
                             command=self.open_menu)
        menu_button.pack(pady=10)

        # Variables for Chaat Items
        self.bhel_puri = IntVar()
        self.pav_bhaji = IntVar()
        self.dahi_puri = IntVar()
        self.pani_puri = IntVar()
        self.sev_puri = IntVar()
        self.aloo_tikki = IntVar()
        self.papdi_chaat = IntVar()
        self.samosa = IntVar()
        self.kachori = IntVar()  # New item
        self.dhokla = IntVar()  # New item

        # Variables for Drinks
        self.coke = IntVar()
        self.sprite = IntVar()
        self.fanta = IntVar()
        self.mountain_dew = IntVar()
        self.thums_up = IntVar()
        self.limca = IntVar()
        self.water = IntVar()

        # Variables for Pizza, Burger, Sandwich, Tacos
        self.pizza = IntVar()
        self.burger = IntVar()
        self.sandwich = IntVar()
        self.tacos = IntVar()

        # Total Variables
        self.total_chaat = StringVar()
        self.total_drinks = StringVar()
        self.total_fast_food = StringVar()  # New variable for fast food
        self.gst = StringVar()
        self.final_total = StringVar()
        self.bill_no = StringVar()
        self.c_name = StringVar()
        self.phone = StringVar()

        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))

        # Customer Details
        details = LabelFrame(self.root, text="Customer Details", font=("Arial Black", 12), bg="#34495E", fg="white",
                             relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)

        Label(details, text="Customer Name", font=("Arial Black", 14), bg="#34495E", fg="white").grid(row=0, column=0,
                                                                                                      padx=15)
        Entry(details, borderwidth=4, width=30, textvariable=self.c_name).grid(row=0, column=1, padx=8)

        Label(details, text="Contact No.", font=("Arial Black", 14), bg="#34495E", fg="white").grid(row=0, column=2,
                                                                                                    padx=10)
        Entry(details, borderwidth=4, width=30, textvariable=self.phone).grid(row=0, column=3, padx=8)

        Label(details, text="Bill No.", font=("Arial Black", 14), bg="#34495E", fg="white").grid(row=0, column=4,
                                                                                                 padx=10)
        Entry(details, borderwidth=4, width=30, textvariable=self.bill_no).grid(row=0, column=5, padx=8)

        # Chaat Menu
        menu_frame = LabelFrame(self.root, text="Chaat Menu", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483",
                                relief=GROOVE, bd=10)
        menu_frame.place(x=5, y=180, height=380, width=325)

        Label(menu_frame, text="Bhel Puri", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0, column=0,
                                                                                                       pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.bhel_puri).grid(row=0, column=1, padx=10)

        Label(menu_frame, text="Pav Bhaji", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1, column=0,
                                                                                                       pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.pav_bhaji).grid(row=1, column=1, padx=10)

        Label(menu_frame, text="Dahi Puri", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2, column=0,
                                                                                                       pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.dahi_puri).grid(row=2, column=1, padx=10)

        Label(menu_frame, text="Pani Puri", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3, column=0,
                                                                                                       pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.pani_puri).grid(row=3, column=1, padx=10)

        Label(menu_frame, text="Sev Puri", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4, column=0,
                                                                                                      pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.sev_puri).grid(row=4, column=1, padx=10)

        Label(menu_frame, text="Aloo Tikki", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=5, column=0,
                                                                                                        pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.aloo_tikki).grid(row=5, column=1, padx=10)

        Label(menu_frame, text="Papdi Chaat", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=6,
                                                                                                         column=0,
                                                                                                         pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.papdi_chaat).grid(row=6, column=1, padx=10)

        Label(menu_frame, text="Samosa", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=7, column=0,
                                                                                                    pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.samosa).grid(row=7, column=1, padx=10)

        Label(menu_frame, text="Kachori", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=8, column=0,
                                                                                                     pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.kachori).grid(row=8, column=1, padx=10)

        Label(menu_frame, text="Dhokla", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=9, column=0,
                                                                                                    pady=11)
        Entry(menu_frame, borderwidth=2, width=15, textvariable=self.dhokla).grid(row=9, column=1, padx=10)

        # Drinks Menu
        drinks_frame = LabelFrame(self.root, text="Drinks Menu", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483",
                                  relief=GROOVE, bd=10)
        drinks_frame.place(x=340, y=180, height=380, width=325)

        Label(drinks_frame, text="Coke", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0, column=0,
                                                                                                    pady=11)
        Entry(drinks_frame, borderwidth=2, width=15, textvariable=self.coke).grid(row=0, column=1, padx=10)

        Label(drinks_frame, text="Sprite", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1, column=0,
                                                                                                      pady=11)
        Entry(drinks_frame, borderwidth=2, width=15, textvariable=self.sprite).grid(row=1, column=1, padx=10)

        Label(drinks_frame, text="Fanta", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2, column=0,
                                                                                                     pady=11)
        Entry(drinks_frame, borderwidth=2, width=15, textvariable=self.fanta).grid(row=2, column=1, padx=10)

        Label(drinks_frame, text="Mountain Dew", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3,
                                                                                                            column=0,
                                                                                                            pady=11)
        Entry(drinks_frame, borderwidth=2, width=15, textvariable=self.mountain_dew).grid(row=3, column=1, padx=10)

        Label(drinks_frame, text="Thums Up", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4, column=0,
                                                                                                        pady=11)
        Entry(drinks_frame, borderwidth=2, width=15, textvariable=self.thums_up).grid(row=4, column=1, padx=10)

        Label(drinks_frame, text="Limca", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=5, column=0,
                                                                                                     pady=11)
        Entry(drinks_frame, borderwidth=2, width=15, textvariable=self.limca).grid(row=5, column=1, padx=10)

        Label(drinks_frame, text="Water", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=6, column=0,
                                                                                                     pady=11)
        Entry(drinks_frame, borderwidth=2, width=15, textvariable=self.water).grid(row=6, column=1, padx=10)

        # Fast Food Menu
        fast_food_frame = LabelFrame(self.root, text="Fast Food Menu", font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483",
                                     relief=GROOVE, bd=10)
        fast_food_frame.place(x=675, y=180, height=380, width=325)

        Label(fast_food_frame, text="Pizza", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0, column=0,
                                                                                                       pady=11)
        Entry(fast_food_frame, borderwidth=2, width=15, textvariable=self.pizza).grid(row=0, column=1, padx=10)

        Label(fast_food_frame, text="Burger", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1, column=0,
                                                                                                        pady=11)
        Entry(fast_food_frame, borderwidth=2, width=15, textvariable=self.burger).grid(row=1, column=1, padx=10)

        Label(fast_food_frame, text="Sandwich", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2, column=0,
                                                                                                          pady=11)
        Entry(fast_food_frame, borderwidth=2, width=15, textvariable=self.sandwich).grid(row=2, column=1, padx=10)

        Label(fast_food_frame, text="Tacos", font=("Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3, column=0,
                                                                                                       pady=11)
        Entry(fast_food_frame, borderwidth=2, width=15, textvariable=self.tacos).grid(row=3, column=1, padx=10)

        # Bill Area
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        billarea.place(x=1000, y=180, width=330, height=380)

        Label(billarea, text="Bill Area", font=("Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3",
              fg="#6C3483").pack(fill=X)

        self.txtarea = Text(billarea)
        self.txtarea.pack(fill=BOTH, expand=1)

        # Billing Summary
        billing_menu = LabelFrame(self.root, text="Billing Summary", font=("Arial Black", 12), relief=GROOVE, bd=10,
                                  bg="#A569BD", fg="white")
        billing_menu.place(x=0, y=570, relwidth=1, height=137)

        Label(billing_menu, text="Total Chaat Price", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=0,
                                                                                                               column=0)
        self.total_chaat_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_chaat)
        self.total_chaat_entry.grid(row=0, column=1, padx=10, pady=7)

        Label(billing_menu, text="Total Drinks Price", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=1,
                                                                                                                column=0)
        self.total_drinks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_drinks)
        self.total_drinks_entry.grid(row=1, column=1, padx=10, pady=7)

        Label(billing_menu, text="Total Fast Food Price", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=2,
                                                                                                                column=0)
        self.total_fast_food_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.total_fast_food)
        self.total_fast_food_entry.grid(row=2, column=1, padx=10, pady=7)

        Label(billing_menu, text="GST (18%)", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=3, column=0)
        self.gst_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.gst)
        self.gst_entry.grid(row=3, column=1, padx=10, pady=7)

        Label(billing_menu, text="Final Total", font=("Arial Black", 11), bg="#A569BD", fg="white").grid(row=4,
                                                                                                         column=0)
        self.final_total_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.final_total)
        self.final_total_entry.grid(row=4, column=1, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#6C3483")
        button_frame.place(x=830, width=500, height=95)

        Button(button_frame, text="Total Bill", font=("Arial Black", 11), pady=10, bg="#E5B4F3", fg="#6C3483",
               command=self.calculate_total).grid(row=0, column=0, padx=12)
        Button(button_frame, text="Print Excel", font=("Arial Black", 11), pady=10, bg="#E5B4F3", fg="#6C3483",
               command=self.print_bill_excel).grid(row=0, column=1, padx=10, pady=6)
        Button(button_frame, text="Print PDF", font=("Arial Black", 11), pady=10, bg="#E5B4F3", fg="#6C3483",
               command=self.print_bill_pdf).grid(row=0, column=2, padx=10, pady=6)
        Button(button_frame, text="Clear Field", font=("Arial Black", 11), pady=10, bg="#E5B4F3", fg="#6C3483",
               command=self.clear).grid(row=0, column=3, padx=10, pady=6)
        Button(button_frame, text="Exit", font=("Arial Black", 11), pady=10, bg="#E5B4F3", fg="#6C3483", width=8,
               command=self.exit_app).grid(row=0, column=4, padx=10, pady=6)

    def open_menu(self):
        # Create a new window for the menu
        menu_window = Toplevel(self.root)
        menu_window.title("Menu Items")
        menu_window.geometry("400x400")
        menu_window.configure(bg="#E5B4F3")

        # Create a canvas and scrollbar
        canvas = Canvas(menu_window, bg="#E5B4F3")
        scrollbar = Scrollbar(menu_window, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#E5B4F3")

        # Configure the canvas
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Pack the canvas and scrollbar
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Add menu items
        menu_items = [
            "Chaat Items:",
            "1. Bhel Puri - 30 Rs",
            "2. Pav Bhaji - 50 Rs",
            "3. Dahi Puri - 40 Rs",
            "4. Pani Puri - 20 Rs",
            "5. Sev Puri - 25 Rs",
            "6. Aloo Tikki - 35 Rs",
            "7. Papdi Chaat - 45 Rs",
            "8. Samosa - 15 Rs",
            "9. Kachori - 20 Rs",
            "10. Dhokla - 25 Rs",
            "",
            "Fast Food Items:",
            "11. Pizza - 100 Rs",
            "12. Burger - 80 Rs",
            "13. Sandwich - 50 Rs",
            "14. Tacos - 60 Rs",
            "",
            "Drinks:",
            "15. Coke - 20 Rs",
            "16. Sprite - 20 Rs",
            "17. Fanta - 20 Rs",
            "18. Mountain Dew - 20 Rs",
            "19. Thums Up - 20 Rs",
            "20. Limca - 20 Rs",
            "21. Water - 10 Rs"
        ]

        # Display menu items in the new window
        for item in menu_items:
            label = Label(scrollable_frame, text=item, font=("Arial Black", 12), bg="#E5B4F3", fg="#6C3483")
            label.pack(anchor='w', padx=20, pady=5)
    def calculate_total(self):
        if self.c_name.get() == "" or self.phone.get() == "":
            messagebox.showerror("Error", "Fill the complete Customer Details!!")
            return

        # Prices for each item
        prices = {
            "bhel_puri": 30,
            "pav_bhaji": 50,
            "dahi_puri": 40,
            "pani_puri": 20,
            "sev_puri": 25,
            "aloo_tikki": 35,
            "papdi_chaat": 45,
            "samosa": 15,
            "kachori": 20,
            "dhokla": 25,
            "coke": 20,
            "sprite": 20,
            "fanta": 20,
            "mountain_dew": 20,
            "thums_up": 20,
            "limca": 20,
            "water": 10,
            "pizza": 100,  # Price for pizza
            "burger": 80,  # Price for burger
            "sandwich": 50,  # Price for sandwich
            "tacos": 60  # Price for tacos
        }

        total_chaat_price = (
                self.bhel_puri.get() * prices["bhel_puri"] +
                self.pav_bhaji.get() * prices["pav_bhaji"] +
                self.dahi_puri.get() * prices["dahi_puri"] +
                self.pani_puri.get() * prices["pani_puri"] +
                self.sev_puri.get() * prices["sev_puri"] +
                self.aloo_tikki.get() * prices["aloo_tikki"] +
                self.papdi_chaat.get() * prices["papdi_chaat"] +
                self.samosa.get() * prices["samosa"] +
                self.kachori.get() * prices["kachori"] +
                self.dhokla.get() * prices["dhokla"]
        )

        total_drinks_price = (
                self.coke.get() * prices["coke"] +
                self.sprite.get() * prices["sprite"] +
                self.fanta.get() * prices["fanta"] +
                self.mountain_dew.get() * prices["mountain_dew"] +
                self.thums_up.get() * prices["thums_up"] +
                self.limca.get() * prices["limca"] +
                self.water.get() * prices["water"]
        )

        total_fast_food_price = (
                self.pizza.get() * prices["pizza"] +
                self.burger.get() * prices["burger"] +
                self.sandwich.get() * prices["sandwich"] +
                self.tacos.get() * prices["tacos"]
        )

        total_price = total_chaat_price + total_drinks_price + total_fast_food_price

        self.total_chaat.set(f"{total_chaat_price} Rs")
        self.total_drinks.set(f"{total_drinks_price} Rs")
        self.total_fast_food.set(f"{total_fast_food_price} Rs")  # Update fast food total

        # Calculate GST (18%)
        gst_amount = total_price * 0.18
        self.gst.set(f"{gst_amount:.2f} Rs")

        # Final total
        final_total_amount = total_price + gst_amount
        self.final_total.set(f"{final_total_amount:.2f} Rs")

        self.show_bill()

    def show_bill(self):
        self.txtarea.delete(1.0, END)
        self.txtarea.insert(END, "\tWELCOME TO CHAAT CORNER\n")
        self.txtarea.insert(END, f"\nBill No. : {self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
        self.txtarea.insert(END, "\n====================================\n")
        self.txtarea.insert(END, "\nProduct\t\tQty\tPrice\n")
        self.txtarea.insert(END, "\n====================================\n")

        if self.bhel_puri.get() != 0:
            self.txtarea.insert(END, f"Bhel Puri\t {self.bhel_puri.get()}\t{self.bhel_puri.get() * 30}\n")
        if self.pav_bhaji.get() != 0:
            self.txtarea.insert(END, f"Pav Bhaji\t {self.pav_bhaji.get()}\t{self.pav_bhaji.get() * 50}\n")
        if self.dahi_puri.get() != 0:
            self.txtarea.insert(END, f"Dahi Puri\t {self.dahi_puri.get()}\t{self.dahi_puri.get() * 40}\n")
        if self.pani_puri.get() != 0:
            self.txtarea.insert(END, f"Pani Puri\t {self.pani_puri.get()}\t{self.pani_puri.get() * 20}\n")
        if self.sev_puri.get() != 0:
            self.txtarea.insert(END, f"Sev Puri\t {self.sev_puri.get()}\t{self.sev_puri.get() * 25}\n")
        if self.aloo_tikki.get() != 0:
            self.txtarea.insert(END, f"Aloo Tikki\t {self.aloo_tikki.get()}\t{self.aloo_tikki.get() * 35}\n")
        if self.papdi_chaat.get() != 0:
            self.txtarea.insert(END, f"Papdi Chaat\t {self.papdi_chaat.get()}\t{self.papdi_chaat.get() * 45}\n")
        if self.samosa.get() != 0:
            self.txtarea.insert(END, f"Samosa\t\t {self.samosa.get()}\t{self.samosa.get() * 15}\n")
        if self.kachori.get() != 0:
            self.txtarea.insert(END, f"Kachori\t\t {self.kachori.get()}\t{self.kachori.get() * 20}\n")
        if self.dhokla.get() != 0:
            self.txtarea.insert(END, f"Dhokla\t\t {self.dhokla.get()}\t{self.dhokla.get() * 25}\n")

        if self.coke.get() != 0:
            self.txtarea.insert(END, f"Coke\t\t {self.coke.get()}\t{self.coke.get() * 20}\n")
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"Sprite\t\t {self.sprite.get()}\t{self.sprite.get() * 20}\n")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"Fanta\t\t {self.fanta.get()}\t{self.fanta.get() * 20}\n")
        if self.mountain_dew.get() != 0:
            self.txtarea.insert(END, f"Mountain Dew\t {self.mountain_dew.get()}\t{self.mountain_dew.get() * 20}\n")
        if self.thums_up.get() != 0:
            self.txtarea.insert(END, f"Thums Up\t {self.thums_up.get()}\t{self.thums_up.get() * 20}\n")
        if self.limca.get() != 0:
            self.txtarea.insert(END, f"Limca\t\t {self.limca.get()}\t{self.limca.get() * 20}\n")
        if self.water.get() != 0:
            self.txtarea.insert(END, f"Water\t\t {self.water.get()}\t{self.water.get() * 10}\n")

        if self.pizza.get() != 0:
            self.txtarea.insert(END, f"Pizza\t\t {self.pizza.get()}\t{self.pizza.get() * 100}\n")
        if self.burger.get() != 0:
            self.txtarea.insert(END, f"Burger\t\t {self.burger.get()}\t{self.burger.get() * 80}\n")
        if self.sandwich.get() != 0:
            self.txtarea.insert(END, f"Sandwich\t {self.sandwich.get()}\t{self.sandwich.get() * 50}\n")
        if self.tacos.get() != 0:
            self.txtarea.insert(END, f"Tacos\t\t {self.tacos.get()}\t{self.tacos.get() * 60}\n")

        self.txtarea.insert(END, "------------------------------------\n")
        self.txtarea.insert(END, f"Total Chaat Price : {self.total_chaat.get()}\n")
        self.txtarea.insert(END, f"Total Drinks Price : {self.total_drinks.get()}\n")
        self.txtarea.insert(END, f"Total Fast Food Price : {self.total_fast_food.get()}\n")  # Show fast food total
        self.txtarea.insert(END, f"GST (18%) : {self.gst.get()}\n")
        self.txtarea.insert(END, f"Final Total : {self.final_total.get()}\n")
        self.txtarea.insert(END, "------------------------------------\n")

    def print_bill_excel(self):
        # Prepare data for Excel
        data = {
            "Bill No": [self.bill_no.get()],
            "Customer Name": [self.c_name.get()],
            "Phone No": [self.phone.get()],
            "Total Chaat Price": [self.total_chaat.get()],
            "Total Drinks Price": [self.total_drinks.get()],
            "Total Fast Food Price": [self.total_fast_food.get()],  # Include fast food total
            "GST (18%)": [self.gst.get()],
            "Final Total": [self.final_total.get()],
        }

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Check if the Excel file exists
        file_name = "billing_data.xlsx"
        if os.path.exists(file_name):
            # Append to the existing file
            with pd.ExcelWriter(file_name, mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
                df.to_excel(writer, sheet_name='Sheet1', index=False, header=False, startrow=writer.sheets['Sheet1'].max_row)
        else:
            # Create a new Excel file
            df.to_excel(file_name, index=False)

        messagebox.showinfo("Success", "Bill saved to Excel successfully!")

    def print_bill_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="WELCOME TO CHAAT CORNER", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Bill No. : {self.bill_no.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Customer Name : {self.c_name.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Phone No. : {self.phone.get()}", ln=True)
        pdf.cell(200, 10, txt="====================================", ln=True)
        pdf.cell(200, 10, txt="Product\t\tQty\tPrice", ln=True)
        pdf.cell(200, 10, txt="====================================", ln=True)

        # Add items to PDF
        if self.bhel_puri.get() != 0:
            pdf.cell(200, 10, txt=f"Bhel Puri\t {self.bhel_puri.get()}\t{self.bhel_puri.get() * 30}", ln=True)
        if self.pav_bhaji.get() != 0:
            pdf.cell(200, 10, txt=f"Pav Bhaji\t {self.pav_bhaji.get()}\t{self.pav_bhaji.get() * 50}", ln=True)
        if self.dahi_puri.get() != 0:
            pdf.cell(200, 10, txt=f"Dahi Puri\t {self.dahi_puri.get()}\t{self.dahi_puri.get() * 40}", ln=True)
        if self.pani_puri.get() != 0:
            pdf.cell(200, 10, txt=f"Pani Puri\t {self.pani_puri.get()}\t{self.pani_puri.get() * 20}", ln=True)
        if self.sev_puri.get() != 0:
            pdf.cell(200, 10, txt=f"Sev Puri\t {self.sev_puri.get()}\t{self.sev_puri.get() * 25}", ln=True)
        if self.aloo_tikki.get() != 0:
            pdf.cell(200, 10, txt=f"Aloo Tikki\t {self.aloo_tikki.get()}\t{self.aloo_tikki.get() * 35}", ln=True)
        if self.papdi_chaat.get() != 0:
            pdf.cell(200, 10, txt=f"Papdi Chaat\t {self.papdi_chaat.get()}\t{self.papdi_chaat.get() * 45}", ln=True)
        if self.samosa.get() != 0:
            pdf.cell(200, 10, txt=f"Samosa\t\t {self.samosa.get()}\t{self.samosa.get() * 15}", ln=True)
        if self.kachori.get() != 0:
            pdf.cell(200, 10, txt=f"Kachori\t\t {self.kachori.get()}\t{self.kachori.get() * 20}", ln=True)
        if self.dhokla.get() != 0:
            pdf.cell(200, 10, txt=f"Dhokla\t\t {self.dhokla.get()}\t{self.dhokla.get() * 25}", ln=True)

        if self.coke.get() != 0:
            pdf.cell(200, 10, txt=f"Coke\t\t {self.coke.get()}\t{self.coke.get() * 20}", ln=True)
        if self.sprite.get() != 0:
            pdf.cell(200, 10, txt=f"Sprite\t\t {self.sprite.get()}\t{self.sprite.get() * 20}", ln=True)
        if self.fanta.get() != 0:
            pdf.cell(200, 10, txt=f"Fanta\t\t {self.fanta.get()}\t{self.fanta.get() * 20}", ln=True)
        if self.mountain_dew.get() != 0:
            pdf.cell(200, 10, txt=f"Mountain Dew\t {self.mountain_dew.get()}\t{self.mountain_dew.get() * 20}", ln=True)
        if self.thums_up.get() != 0:
            pdf.cell(200, 10, txt=f"Thums Up\t {self.thums_up.get()}\t{self.thums_up.get() * 20}", ln=True)
        if self.limca.get() != 0:
            pdf.cell(200, 10, txt=f"Limca\t\t {self.limca.get()}\t{self.limca.get() * 20}", ln=True)
        if self.water.get() != 0:
            pdf.cell(200, 10, txt=f"Water\t\t {self.water.get()}\t{self.water.get() * 10}", ln=True)

        if self.pizza.get() != 0:
            pdf.cell(200, 10, txt=f"Pizza\t\t {self.pizza.get()}\t{self.pizza.get() * 100}", ln=True)
        if self.burger.get() != 0:
            pdf.cell(200, 10, txt=f"Burger\t\t {self.burger.get()}\t{self.burger.get() * 80}", ln=True)
        if self.sandwich.get() != 0:
            pdf.cell(200, 10, txt=f"Sandwich\t {self.sandwich.get()}\t{self.sandwich.get() * 50}", ln=True)
        if self.tacos.get() != 0:
            pdf.cell(200, 10, txt=f"Tacos\t\t {self.tacos.get()}\t{self.tacos.get() * 60}", ln=True)

        pdf.cell(200, 10, txt="------------------------------------", ln=True)
        pdf.cell(200, 10, txt=f"Total Chaat Price : {self.total_chaat.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Total Drinks Price : {self.total_drinks.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Total Fast Food Price : {self.total_fast_food.get()}", ln=True)
        pdf.cell(200, 10, txt=f"GST (18%) : {self.gst.get()}", ln=True)
        pdf.cell(200, 10, txt=f"Final Total : {self.final_total.get()}", ln=True)

        # Save the PDF
        pdf_file_name = f"bill_{self.bill_no.get()}.pdf"
        pdf.output(pdf_file_name)
        messagebox.showinfo("Success", f"Bill saved as PDF: {pdf_file_name}")

    def clear(self):
        self.c_name.set("")
        self.phone.set("")
        self.bill_no.set("")
        self.total_chaat.set("")
        self.total_drinks.set("")
        self.total_fast_food.set("")
        self.gst.set("")
        self.final_total.set("")
        self.txtarea.delete(1.0, END)

        # Reset all item quantities
        self.bhel_puri.set(0)
        self.pav_bhaji.set(0)
        self.dahi_puri.set(0)
        self.pani_puri.set(0)
        self.sev_puri.set(0)
        self.aloo_tikki.set(0)
        self.papdi_chaat.set(0)
        self.samosa.set(0)
        self.kachori.set(0)
        self.dhokla.set(0)
        self.coke.set(0)
        self.sprite.set(0)
        self.fanta.set(0)
        self.mountain_dew.set(0)
        self.thums_up.set(0)
        self.limca.set(0)
        self.water.set(0)
        self.pizza.set(0)
        self.burger.set(0)
        self.sandwich.set(0)
        self.tacos.set(0)

    def exit_app(self):
        self.root.destroy()

if __name__ == "_main_":
    root = Tk()
    app = Bill_App(root)
    root.mainloop()