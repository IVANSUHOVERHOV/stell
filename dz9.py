import requests
res_para_list = []
response = requests.get("https://coinmarketcap.com/")

response_text = response.text
response_parse = response_text.split("<span>")
for elem_1 in response_parse:
    if elem_1.startswith("$"):
        for elem_2 in elem_1.split("</span>"):
            if elem_2.startswith("$") and elem_2[1].isdigit():
                res_para_list.append(elem_2)
                for elem_3 in elem_1.split("</span>"):
                    if elem_3.startswith("€") and elem_3[1].isdigit():
                        res_para_list.append(elem_3)


print(res_para_list[0])