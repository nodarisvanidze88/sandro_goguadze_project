import csv
from tabulate import tabulate
def main():
    data = readFiel('TOPSYS.csv')
    print(data)
    all_headers = list(data[0].keys())
    parmeter_headers = all_headers[1:]
    sum_params = get_sum_parameters(data,parmeter_headers)
    first_result = get_first_result(data, sum_params, all_headers)
    print(tabulate(first_result, headers='keys'))
    weights = get_waights(parmeter_headers)
    second_result = get_second_result(first_result, weights, all_headers)
    print(tabulate(second_result, headers='keys'))
    more_less = get_more_or_less(parmeter_headers)
    third_result = get_third_result(second_result,more_less)
    print(tabulate(third_result, headers='keys'))
    # get_fourth_result(second_result,third_result)

def get_fourth_result(res2,res3):
   print(res2)
   print(res3)


def get_third_result(data, more_less):
    result = []
    temp = get_min_max(data, more_less,"<")
    result.append(temp)
    temp2 = get_min_max(data, more_less,">")
    result.append(temp2)
    return result

def get_min_max(data, more_less,value):
    temp = {}
    for key, val in more_less.items():
        numbers = get_value_list(data,key)
        if val == value:
            temp[key] = min(numbers)
        else:
            temp[key] = max(numbers)
    return temp

def get_value_list(data,header):
    result = []
    for item in data:
        result.append(item[header])
    return result

def get_more_or_less(parameters):
    result = {}
    for item in parameters:
        while True:
            user = input(f"Add parameter for {item} ")
            if user == ">" or user == "<":
                result[item]=user
                break
    return result

def get_waights(parameters):
    total = 0
    counter = 0
    result = {}
    for item in parameters:
        while True:
            try:
                user = int(input(f"Add percentage for {item} "))
                result[item]=user/100
                total+=user
                print(f"{100-total} left")
                break
            except:
                pass
        counter+= 1

    if counter == len(parameters) and total == 100:
        return result
    else:
        print("100 left")
        return get_waights(parameters)

def get_second_result(first_result,weights, headers):
    result = []
    for item in first_result:
        temp = {}
        for i, v  in item.items():
            for j in weights.items():
                param, val = j
                if i not in temp and i == headers[0]:
                    temp[i] = v
                if i == param and i not in temp:
                    temp[i] = round(v*val,10)
        result.append(temp)
    return result
    
def get_first_result(data, param_sum, headers):
    result = []
    for item in data:
        temp = {}
        for i, v  in item.items():
            for j in param_sum:
                param, val = list(j.items())[0]
                if i not in temp and i == headers[0]:
                    temp[i] = v
                if i == param and i not in temp:
                    temp[i] = round(float(v)/(val*2)*0.5,10)
        result.append(temp)
    return result

def readFiel(fileName):
    with open(fileName, 'r') as file:
        data = csv.DictReader(file)
        return list(data)

def get_sum_parameters(data,headers):
    result = []
    for header in headers:
        temp = {header: sum(float(item[header]) for item in data)}
        result.append(temp)
    return result

if __name__ =="__main__":
    main()