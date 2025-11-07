import tkinter as tk

def create_column_widgets(column, date_text, weather_text, weather_emoji, temperature):
    date_label = tk.Label(column, text=date_text, font=("Helvetica", 18), bg=column.cget("bg")) # so it has the same bg as the column
    weather_emoji_label= tk.Label(column, text=weather_emoji, font=("Helvetica", 40), bg=column.cget("bg"))
    weather_label= tk.Label(column, text=weather_text, font=("Helvetica", 18), bg=column.cget("bg"))
    temperature_label = tk.Label(column, text=temperature, font=("Helvetica", 18), bg=column.cget("bg"))
    
    date_label.pack(side=tk.TOP, expand=True, pady=10)
    weather_emoji_label.pack(side=tk.TOP, expand=True, pady=10)
    weather_label.pack(side=tk.TOP, expand=True, pady=10)
    temperature_label.pack(side=tk.TOP, expand=True, pady=10)

def main():
    window = tk.Tk()
    window.title("COSC 117 Weather Forecast")
    window.geometry("800x400")

    # Create a frame to hold all the columns
    column_container = tk.Frame(window)
    column_container.pack(fill=tk.BOTH, expand=True)

    # Create the four column frames
    yesterday_frame = tk.Frame(column_container, borderwidth=1, relief="sunken")
    today_frame = tk.Frame(column_container, bg="lightgrey", borderwidth=1, relief="sunken")
    tomorrow_frame = tk.Frame(column_container, borderwidth=1, relief="sunken")
    day_after_tomorrow_frame = tk.Frame(column_container, borderwidth=1, relief="sunken")

    # Pack the columns side-by-side
    yesterday_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    today_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    tomorrow_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    day_after_tomorrow_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    #create_column_widgets(today_frame, "2025-11-01", "Rainy", "🌧", "-2.0 C")

    window.mainloop()    


if __name__ == "__main__":
    main()