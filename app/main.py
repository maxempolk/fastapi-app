from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from random import shuffle

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

items = [
    {
        "name": "docker",
        "logo": r"https://w7.pngwing.com/pngs/219/411/png-transparent-docker-logo-kubernetes-microservices-cloud-computing-dockers-logo-text-logo-cloud-computing-thumbnail.png",
    },
    {
        "name": "vue.js",
        "logo": r"https://w7.pngwing.com/pngs/854/555/png-transparent-vue-js-hd-logo-thumbnail.png",
    },
    {
        "name": "fastapi",
        "logo": "/static/fastapi.svg"
    },
    {
        "name": "html",
        "logo": "/static/html.png"
    },
    {
        "name": "css",
        "logo": r"https://e7.pngegg.com/pngimages/603/759/png-clipart-css3-cascading-style-sheets-logo-html-world-wide-web-blue-angle-thumbnail.png"
    }
]

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    shuffle(items)

    return templates.TemplateResponse(
        request=request, name="index.html", context = { "items": items[:3] }
    )