import tkinter as tk
import json
import requests


def render_image():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMmQzNGViNWUtMTdlYi00NDY4LWFiM2MtZjliZGMxZTRhMmQyIiwidHlwZSI6ImFwaV90b2tlbiJ9.SDOQRxtWNj6PI5XpbI-agEVFfnHhkAdtWfcDboICDGA"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "256x256",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['items'][0]["image_resource_url"])


window = tk.Tk()
window.title('AI Image Generator')
window.geometry('500x350')

input_field = tk.Entry(window, width=14)
input_field.place(x=165, y=20)

generate_button = tk.Button(window, text="Create", height=1, command=render_image)
generate_button.place(x=255, y=17)


window.mainloop()