from bs4 import BeautifulSoup
import requests
import csv

link='http://www.nari.nic.in/schemes?field_age_group_value%5B%5D=2&field_age_group_value%5B%5D=3&field_age_group_value%5B%5D=4&field_age_group_value%5B%5D=5&field_area_value%5B%5D=2&field_area_value%5B%5D=3&field_area_value%5B%5D=4&field_area_value%5B%5D=5&field_area_value%5B%5D=6&field_area_value%5B%5D=7&field_area_value%5B%5D=8&field_area_value%5B%5D=9&field_state_value%5B%5D=2'

csv_file=open('scheme_women.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Scheme Name','About the Scheme'])

for j in range(1,9):

    src=requests.get(link).text

    soup=BeautifulSoup(src,'lxml')

    headlines=soup.find('div',class_='container-fluid').find('div',class_='view-content').find_all('h3')
    desc = soup.find('div', class_='container-fluid').find('div', class_='view-content').find_all('div',class_='col-xs-12 col-sm-6 col-md-6')

    schemes_names=[sc.text for sc in headlines]
    schemes_names=[s.strip('\n') for s in schemes_names]
    schemes_names = [s.strip(' ') for s in schemes_names]



    schemes_desc = [ds.text for ds in desc]
    schemes_desc = [s.strip('\n') for s in schemes_desc]
    schemes_desc = [s.replace('\n', '') for s in schemes_desc]
    schemes_desc = [s.replace("\xa0", '') for s in schemes_desc]

    #print(len(schemes_names))
    #print(len(schemes_desc))


    if j==3:
        schemes_names = list(dict.fromkeys(schemes_names))
        schemes_desc = list(dict.fromkeys(schemes_desc))

    if j==4:
        t=0
        only_four = soup.find('div', class_='container-fluid').find('div', class_='view-content').find('div',class_='col-xs-12 co-sm-6 col-md-6').text
        only_four=only_four.strip('\n')
        only_four=only_four.replace('\n','')
        only_four=only_four.replace("\xa0",'')
        csv_writer.writerow([schemes_names[0], only_four])
        print(str(t) + " " + schemes_names[0] + " " + only_four)
        for p in range(1, min((len(schemes_names)),len(schemes_desc))):
            csv_writer.writerow([schemes_names[p], schemes_desc[p-1]])
            print(str(p) + " " + schemes_names[p] + " " + schemes_desc[p-1])
    else:
        t=0
        for t in range(0,min((len(schemes_names)),len(schemes_desc))):
            csv_writer.writerow([schemes_names[t],schemes_desc[t]])
            print(str(t)+" "+schemes_names[t]+" "+schemes_desc[t])

    print()

    if(j<8):
        i=j+1
        nxt='Go to page '+str(i)
        nxt_pg=soup.find('div',class_='container-fluid').find('div',class_='item-list').find('a',title=nxt)['href']
        link='http://nari.nic.in'+nxt_pg

csv_file.close
