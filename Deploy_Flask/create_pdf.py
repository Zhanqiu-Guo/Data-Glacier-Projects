from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
def create_pdf(name, batch_code, submission_date, submitted_to, image_paths):
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    ptext = f'Name: {name}'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))

    ptext = f'Batch Code: {batch_code}'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))

    ptext = f'Submission Date: {submission_date}'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))

    ptext = f'Submitted To: {submitted_to}'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))

    ptext = f'Deploy Model: '
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))
    im1 = Image(image_paths[0])
    im1._restrictSize(400,400)
    story.append(im1)

    ptext = f'Create PDF: '
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))
    im2 = Image(image_paths[1])
    im2._restrictSize(600,600)
    story.append(im2)

    doc.build(story)

create_pdf(
   "Zhanqiu Guo",
   "LISUM19",
   "2023-3-20",
   "https://github.com/Zhanqiu-Guo/Data-Glacier-Projects.git",
   ["Deploy_Model.png", "Create_PDF.png"]
)