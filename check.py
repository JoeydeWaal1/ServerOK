from domein import Domein
from ping3 import ping
import datetime


def generate_row(domein: Domein) -> str:
    return f"""
            <tr class="bg-gray-500">
                <td class="px-5 py-1">{domein.domein_naam}</td>
                <td class="px-5 py-1">{str(domein.online)}</td>
            </tr>
            """


def generage_html(domeinen: [Domein]):
    f = open("template.html", "r")
    html = f.read()
    f.close()

    now = datetime.datetime.now().strftime("%H:%M,%D")
    html = html.replace("date", now)

    rows = ""
    for d in domeinen:
        rows = rows + generate_row(d)

    html = html.replace("rows", rows)
    f = open("output.html", "w")
    f.write(html)
    f.close()


def check_loop(domeinen: [Domein]):
    for domein in domeinen:
        domein.online = bool(ping(domein.domein_naam))
    generage_html(domeinen)
