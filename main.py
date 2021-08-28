import os
import datafile
import quotes

name = (input("Enter your name to get a quote: ")).title()

quotes_dict = datafile.getQuotesDict()
num_categories = len(quotes_dict)
list_cats = list(quotes_dict.keys())

welcome = f"""
    Hello {name},
     We are happy to welcome you to the positivity center. We currently have {num_categories}
     categories as shown below.  Please enter the category from which you want a quote and press enter to get a random quote
     from your desired category.
    """
print(welcome)
print(*list_cats, sep="\n") 

attempts = 1
attempts_limit = 3
attempts_to_go = 1
while attempts <= attempts_limit:
    selected_quote = input("Enter the category(Enter 'exit' to quit): ").lower()
    attempts_to_go = attempts_limit - attempts
    try:
        if selected_quote == "":
            raise ValueError()
        elif selected_quote == "exit":
            os.abort()
        elif selected_quote in list_cats :
            cat_quotes = quotes.getCategoryQuote(selected_quote, quotes_dict)
            if selected_quote == "madlipz":
                adjective = input("Enter an adjective to describe you: ")
                print(quotes.buildMadlipzQuote(name, cat_quotes, adjective))
            else :
                print(quotes.buildPersonalizedQuote(name, cat_quotes))
            if attempts == attempts_limit:
                print("Hurray!! You have completed your happy center transformation. You are a happy person")
            else :
                print(f"Great!! You can still get {attempts_to_go} quote(s)")
            attempts += 1
            continue
        else :
            if attempts == attempts_limit:
                print(f"""Hey {name}, you entered {selected_quote} which is not a valid category. You have had {attempts_limit} attempt(s) already, the process will end now""")
                break
            else :
                print(f"Hey {name}, you entered {selected_quote} which is not a valid category. You still have {attempts_to_go} attempts to go")
                # selected_quote = input("Enter the category ").lower()
    except ValueError:
        print(f"You entered nothing, You still have {attempts_to_go+1} attempt(s) to go. Please enter a word")
        continue
    except :
        print("Please enter a word")
        pass
    attempts += 1