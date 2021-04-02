import json

import pandas as pd


headers_list = []
params_list = []
json_list = []
columns = ['name','url']

input_dict={
    "clientid":10000,
    'loginid':"test+6@centime.com"
}
output_dict ={}

# uri= gui.uri_entry.get()
# api_name=gui.api_name_entry.get()
# # headers = {
# #     'clientid': 5,
# #     'loginid': 'sreenivasulu@centime.com'
# # }
#
# headers= json.loads(gui.api_headers_text.get("1.0","end"))
#
# # params = {
# #     "partner":"Centime"
# # }
#
# params= json.loads(gui.api_params_text.get("1.0","end"))



# gen_dict= {
#     "headers.clientid" : 5,
#     "headers.loginid":"test+6@centime.com",
#     "params.partner":"Centime",
#     "response":{"status":"FAILURE","errors":[{"code":"CCOO1"}]}
# }

#err_response = gui.api_response_error_message_text.get("1.0","end")

# rel_dict= {
#     "headers.clientid" : 5,
#     "headers.loginid":"test+6@centime.com",
#     "params.partner":"Centime",
#     "response":{"status":"FAILURE","errors":[{"code":"CCOO1"}]}
# }

# rel_dict=gen_dict

scenarios_int = {
    "empty":"",
    "negative":-5,
    "positive":10,
    "bigvalue":1000000000000,
    "smallvlaue":1,
    "stringvalue":"test",
    "decimalvalue":10.5
}

scenarios_string = {
    "empty":"",
    "bigvalue":"Big Value given here",
    "smallvlaue":"test",
    "numericalvalue":10
}

output_df = pd.DataFrame(columns=columns)





def generate_tests(uri,api_name,headers,params,err_response):
    headers = json.loads(headers)
    params = json.loads(params)
    err_response = json.loads(err_response)
    for key in headers.keys():
        headers_list.append("header." + key)

    for key in params.keys():
        params_list.append("params." + key)

    columns.extend(headers_list)
    columns.extend((params_list))
    columns.append('response')
    global output_df
    rot_range = len(headers) + len(params)
    for i in range(0,rot_range):
        gen_dict = {}
        if i < len(headers):
            key = f"headers.{list(headers)[i]}"
            data_type = headers[list(headers)[i]]
        else:
            i = i - len(headers)
            key = f"params.{list(params)[i]}"
            data_type = params[list(params)[i]]
        if data_type == 'int':
            for scenario_key in scenarios_int.keys():
                gen_dict[key] = scenarios_int[scenario_key]
                test_case_name = f"{api_name}_with {key} as {scenario_key}"
                gen_dict['name'] = test_case_name
                gen_dict['url'] = uri
                output_df = pd.concat([output_df,pd.DataFrame(gen_dict,index=[i])],ignore_index = True)
                gen_dict['response'] = err_response
        else:
            for scenario_key in scenarios_string.keys():
                gen_dict[key] = scenarios_string[scenario_key]
                test_case_name = f"{api_name}_with {key} as {scenario_key}"
                gen_dict['name'] = test_case_name
                gen_dict['url'] = uri
                output_df = pd.concat([output_df,pd.DataFrame(gen_dict,index = [i])],ignore_index = True)
                gen_dict['response'] = err_response
    output_df.to_csv('test.csv')


