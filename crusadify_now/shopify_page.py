import json
import requests
import reflex as rx

class Page(rx.Model, table=True):
    __tablename__ = "pages"

def publish_page(data: dict):
    try:
        print(data)
        shop = data["storeName"]
        access_token = data["accessToken"]
        page_name = data["pageName"]
        headers = {
            'X-Shopify-Access-Token': access_token,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "page": {
                "title": f"{page_name}",
                "body_html": "<h2>Warranty</h2>\n<p>Returns accepted if we receive items <strong>30 days after purchase</strong>.</p>",
                "metafields": [
                {
                    "key": "new",
                    "value": "new value",
                    "type": "single_line_text_field",
                    "namespace": "global"
                }
                ]
            }
        })
        res = requests.post(f"https://{shop}.myshopify.com/admin/api/2024-01/pages.json", headers=headers, data=payload)
        print(res)
        print(res.json())
        return {"response": res.json(), "url": f"https://{shop}.myshopify.com/pages/{res.json().handle}"}
    except Exception as e:
        print(e)
        return {"error": e}