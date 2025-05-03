def timeInWords(h, m):
    time_words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
                  "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                  "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three",
                  "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight",
                  "twenty nine"]

    if m == 0:
        return f"{time_words[h]} o' clock"
    elif m == 15:
        return f"quarter past {time_words[h]}"
    elif m == 30:
        return f"half past {time_words[h]}"
    elif m == 45:
        return f"quarter to {time_words[h % 12 + 1]}"
    elif m < 30:
        return f"{time_words[m]} minute{'s' if m != 1 else ''} past {time_words[h]}"
    else:
        minutes_to = 60 - m
        return f"{time_words[minutes_to]} minute{'s' if minutes_to != 1 else ''} to {time_words[h % 12 + 1]}"
             
