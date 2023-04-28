import pygal
A1, B1, C1 = map(int, input("Facebookni yilning boshidagi har 4 ta oyda ishlatgan odamlar sonini yozing: ").split())
A2, B2, C2 = map(int, input("Instagramni yilning boshidagi har 4 ta oyda ishlatgan odamlar sonini yozing: ").split())
A3, B3, C3 = map(int, input("Youtubeni yilning boshidagi har 4 ta oyda ishlatgan odamlar sonini yozing: ").split())

line_chart = pygal.Line()
line_chart.title = 'Satatistika'
line_chart.x_labels = ['Yanvar','Fevral', 'Mart', 'Aprel']
line_chart.add('Facebook', [A1, B1, C1])
line_chart.add('Instagram', [A2, B2, C2])
line_chart.add('Youtube', [A3, B3, C3])
line_chart.render_in_browser()