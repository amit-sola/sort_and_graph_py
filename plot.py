import re

from operator import itemgetter, attrgetter, methodcaller

import matplotlib.pyplot as plt

freq = []
volt = []

freq_line = []

volt_line = []

#clean_lines = []

to_sort = []

final_data = []

''' Code for sorting the data according to Die location'''

with open('silicon_data.txt','r+') as file_in:
    with open('sorted_data.txt','w') as file_out:

        data = file_in.readlines()
        for line in data:
            if ((line[0] != '#') and (line[0] != ' ')):


                clean_lines = re.split('\s+',line)
                x,y = re.split(',',clean_lines[3])

                final_data.append([int(x),int(y),float(clean_lines[1]),int(clean_lines[2]),int(clean_lines[0])])

                print(final_data)

        sorted_data = sorted(final_data, key=itemgetter(0, 1, 2, 3))

        file_out.write("(x)\t\t (y)\t voltage\t\t frequency\t id\n")

        for line in sorted_data:
            for x in line:
                file_out.write(str(x))
                file_out.write("\t\t")
            file_out.write("\n")



''' Code for sorting the data according to Die location'''






''' ######### Code for plotting the frequency VS voltage graph ######### '''
with open('silicon_data.txt','r') as file_in:

    data = file_in.readlines()

    for line in data:
            if ((line[0] != '#') and (line[0] != ' ')):
                freq_line = re.sub(r'^[0-9]+[ \t]+[01][.]*[0-9]*[ \t]+', "", line)
                freq_line = re.sub(r'[ \t]+[0-9][,][0-9][ \t]*$', "", freq_line)

                volt_line = re.sub(r'^[0-9]+[ \t]+', "", line)
                volt_line = re.sub(r'[ \t]+[0-9]+[ \t]+[0-9][,][0-9][ \t]*$',"",volt_line)


                freq_line = re.sub(r'\n$',"",freq_line)
                freq.append(float(freq_line))

                volt_line = re.sub(r'\n$',"",volt_line)
                volt.append(float(volt_line))


            else:
                print("commented line")



plt.plot(volt, freq,'-xg')
plt.axis([0.7, 1.3, 1500, 2500])
plt.ylabel('F (frequency)')
plt.xlabel('V (voltage)')
plt.show()

''' ######### Code for plotting the frequency VS voltage graph ######### '''





