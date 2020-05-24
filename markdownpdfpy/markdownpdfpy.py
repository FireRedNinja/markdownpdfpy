"""Main module."""
import mistletoe
from renderer.renderer import HTMLRenderer
from weasyprint import HTML, CSS
import mistune

def markdownToHTML(fileName):
    rendered = None
    with open(f"{fileName}", "r") as f:
        # rendered = mistletoe.markdown(f, HTMLRenderer)
        rendered = mistune.html(f.read())
    
    import pdb; pdb.set_trace()
    print(rendered)

    fileName = fileName.split(".md")[0]

    skeleton_css = CSS("./markdownpdfpy/css/skeleton.css")
    milligeram_css = CSS("./markdownpdfpy/css/milligram.min.css")

    HTML(string=rendered).write_pdf(
        target=f"{fileName}.pdf", stylesheets=[skeleton_css]
    )
    # HTML(string=rendered).write_pdf(
    #     target=f"{fileName}_milligram.pdf", stylesheets=[milligeram_css]
    # )
    # HTML(string=rendered).write_pdf(
    #     target=f"{fileName}_water.pdf",
    #     stylesheets=[
    #         "https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.min.css"
    #     ],
    # )
