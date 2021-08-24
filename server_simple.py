# server_simple.py
import random
from aiohttp import web
import functions as func


async def handle(request: web.Request) -> web.StreamResponse:
    name = request.match_info.get("name", "name")
    css = """<style>
    body {
      background-color: white;
    }

    h1 {
      color: red;
      text-align: center
    } 
    h2 {
      color: black;
      text-align: center
    } 
    </style>
    </head>
    <body>"""
    text = f'''<!DOCTYPE html>
<html>
<head>
{css}

<h1>Hello {name}</h1>
<h2>{func.get_current_timedate()}</h2>
<table border="1">
<tr>
  <td>{random.randint(1, 10)}</td>
</tr>
</table>

</body>
</html>'''

    return web.Response(text=text, content_type='text/html')


# async def wshandle(request: web.Request) -> web.StreamResponse:
#     ws = web.WebSocketResponse()
#     await ws.prepare(request)
#
#     async for msg in ws:
#         if msg.type == web.WSMsgType.TEXT:
#             await ws.send_str(f"Hello, {msg.data}")
#         elif msg.type == web.WSMsgType.BINARY:
#             await ws.send_bytes(msg.data)
#         elif msg.type == web.WSMsgType.CLOSE:
#             break

    # return ws


app = web.Application()
app.add_routes(
    [web.get("/", handle),
     # web.get("/echo", wshandle),
     web.get("/{name}", handle)]
)

web.run_app(app)