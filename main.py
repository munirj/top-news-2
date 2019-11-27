from helper import *

if __name__ = '__main__':

    country=input('please enter your country:')
    category = input('please enter a category:')

    n = int(input('how many articles?'))
    #task 1
    data = get_top_news(country,category)
    #task 2
    formatted_date = format_data(data)
    #task 3
    write_to_file(formatted_data,n)