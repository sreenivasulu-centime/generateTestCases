import json
import tkinter as tk
from functools import partial

import testcase_generation as tg

generate_testcases = tk.Tk()

row1_frame = tk.Frame()
row1_frame.pack(fill=tk.X)
row2_frame = tk.Frame()
row2_frame.pack(fill=tk.X)
row3_frame = tk.Frame()
row3_frame.pack(fill=tk.X)
row4_frame = tk.Frame()
row4_frame.pack(fill=tk.X)
row5_frame = tk.Frame()
row5_frame.pack(fill=tk.X)
row6_frame = tk.Frame()
row6_frame.pack(fill=tk.X)
row7_frame = tk.Frame()
row7_frame.pack(fill=tk.X)


uri_endpoint = tk.Label(row1_frame,text="enter uri: ")
uri_entry = tk.Entry(row1_frame)

api_name = tk.Label(row1_frame,text="Enter api name:")
api_name_entry = tk.Entry(row1_frame)

api_method = tk.Label(row1_frame,text="Enter api method:")
api_method_entry = tk.Entry(row1_frame)

api_headers = tk.Label(row2_frame,text="Enter headers in the below text box")
api_params = tk.Label(row2_frame,text="Enter parameters in the below text box")
api_json = tk.Label(row2_frame,text="Enter body in the below text box")

api_headers_sample = tk.Label(row3_frame,text="Eg: headerName:value(datatype) \n loginid:test@centimecom(string)")
api_params_sample = tk.Label(row3_frame,text="Eg: parameterName:value(datatype) \n partner:Centime(string)")
api_json_sample = tk.Label(row3_frame,text="Eg: Json content")

api_headers_text = tk.Text(row4_frame,width=30,height=10)
api_params_text = tk.Text(row4_frame,width=30,height=10)
api_json_text = tk.Text(row4_frame,width=30,height=10)

api_response_error_message = tk.Label(row5_frame,text="Please enter response error message in the below text box")
api_response = tk.Label(row5_frame,text="Please enter valid response in the below text box")

api_response_error_message_text = tk.Text(row6_frame,width = 50,height = 10)
api_response_text = tk.Text(row6_frame,width = 50, height = 10)

uri_endpoint.pack(fill = tk.Y,side = tk.LEFT,padx=10)
uri_entry.pack(fill = tk.Y,side = tk.LEFT)

api_name.pack(fill = tk.Y, side=tk.LEFT)
api_name_entry.pack(fill = tk.Y, side=tk.LEFT)

api_method.pack(fill = tk.Y, side=tk.LEFT)
api_method_entry.pack(fill = tk.Y, side=tk.LEFT)

api_headers.pack(fill = tk.X,side =tk.LEFT,padx =10)
api_params.pack(fill = tk.Y, side=tk.LEFT,padx = 50)
api_json.pack(fill = tk.Y, side=tk.LEFT,padx = 70)

api_headers_sample.pack(fill = tk.X,side =tk.LEFT,padx =10)
api_params_sample.pack(fill = tk.Y, side=tk.LEFT,padx = 50)
api_json_sample.pack(fill = tk.Y, side=tk.LEFT,padx = 70)

api_headers_text.pack(fill = tk.X, side=tk.LEFT,padx=10)
api_params_text.pack(fill = tk.Y, side=tk.LEFT,padx = 50)
api_json_text.pack(fill = tk.Y, side=tk.LEFT,padx = 90)

api_response.pack(fill = tk.X, side=tk.LEFT,padx=10)
api_response_error_message.pack(fill = tk.X, side=tk.LEFT,padx=10)

api_response_text.pack(fill = tk.X, side=tk.LEFT,padx=10)
api_response_error_message_text.pack(fill = tk.X, side=tk.LEFT,padx=10)

# headers = api_headers_text.get("1.0","end")
# params = api_params_text.get("1.0","end")
# err_response = api_response_error_message_text.get("1.0","end")
generate_tests_btn = tk.Button(row7_frame,text = "generate test cases",command=lambda: tg.generate_tests(uri_entry.get(),api_name_entry.get(),api_headers_text.get("1.0","end"),api_params_text.get("1.0","end"),api_response_error_message_text.get("1.0","end")))
generate_tests_btn.pack(fill=tk.X)



#tg.GenerateTests.generate_tests()

generate_testcases.mainloop()