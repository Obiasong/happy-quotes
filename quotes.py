from random import randint
def getCategoryQuote(category, quotes_dict):
    category_quotes_list = quotes_dict[category]
    quotes_cnt = len(category_quotes_list)
    picked_quote_id = randint(0,quotes_cnt)
    return category_quotes_list[picked_quote_id]

def buildPersonalizedQuote(name, quote_template):
    new_text = quote_template.replace("player_name", name)
    return new_text

def buildMadlipzQuote(name, quote_template, adjective):
    new_text = quote_template.replace("player_name", name)
    adj_text = new_text.replace("player_adjective", adjective)
    return adj_text    