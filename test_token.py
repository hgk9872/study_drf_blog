import requests

JWT_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc1NDM4NjcyLCJpYXQiOjE2NzU0MzgzNzIsImp0aSI6IjQ3NTQ5ZDdhM2MzZDQ2ZGFhZjNmOTEyOGU0Y2MwYWM1IiwidXNlcl9pZCI6Mn0.PYqFIcZoWL_tVXxDCZCyqOv2cbNa1S_ik2scMgn_i9s"

headers = {
    'Authorization': f'Bearer {JWT_TOKEN}'
}

res = requests.get("http://localhost:8000/post/1/", headers=headers)
print(res.json())
