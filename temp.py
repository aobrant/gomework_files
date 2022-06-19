# result = {}
# for file_name in lst:
#     with open(file_name) as file_obj:
#         number = sum(1 for line in file_obj)
#         result[file_name] = number
    

def print_in_file(file_name,count):
    f = open('1.txt') 
    data = f.read()
    print(type(data))
    print (data)
    f.close()
    f = open('data1.txt','w')
    f.write(data)
    f.close()
        # for line in f:
        #     prt = f.readline()
        #     print(prt)
        #     st.append(prt)
        

                
        # with open('3.txt') as f:
        #     file_wt.write('111')
        #     for line in f:
        #         prt = f.readline()
        #         print (prt)
        #         file_wt.write('111')
    return
print_in_file('3.txt',2)