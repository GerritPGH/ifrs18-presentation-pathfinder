from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "ifrs18-pathfinder-user-guide.pdf"

PAGE_W, PAGE_H = A4
FOREST = colors.HexColor("#173F3A")
FOREST_2 = colors.HexColor("#225B52")
INK = colors.HexColor("#162522")
INK_SOFT = colors.HexColor("#4D5F5A")
PAPER = colors.HexColor("#F4F1E9")
SURFACE = colors.HexColor("#FFFDF8")
MINT = colors.HexColor("#CFE7DB")
MINT_SOFT = colors.HexColor("#EAF3ED")
AMBER = colors.HexColor("#D98C36")
AMBER_SOFT = colors.HexColor("#FFF0D9")
LINE = colors.HexColor("#D8DDD7")

LIVE_URL = "https://gerritpgh.github.io/ifrs18-presentation-pathfinder/"
LINKEDIN_URL = "https://www.linkedin.com/in/gerrithey/"


def page_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PAPER)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    canvas.setFillColor(FOREST)
    canvas.circle(22 * mm, PAGE_H - 17 * mm, 5.2 * mm, fill=1, stroke=0)
    canvas.setFillColor(colors.white)
    canvas.setFont("Times-Bold", 8)
    canvas.drawCentredString(22 * mm, PAGE_H - 19 * mm, "GH")

    canvas.setFillColor(FOREST)
    canvas.setFont("Helvetica-Bold", 8.5)
    canvas.drawString(31 * mm, PAGE_H - 19 * mm, "IFRS 18 Presentation Pathfinder")

    canvas.setStrokeColor(LINE)
    canvas.line(18 * mm, 15 * mm, PAGE_W - 18 * mm, 15 * mm)
    canvas.setFillColor(INK_SOFT)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(18 * mm, 9.5 * mm, "Five-step user guide | Indicative scoping resource")
    canvas.drawRightString(PAGE_W - 18 * mm, 9.5 * mm, f"{doc.page}")
    canvas.restoreState()


def styles():
    base = getSampleStyleSheet()
    return {
        "cover_kicker": ParagraphStyle(
            "cover_kicker",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=12,
            textColor=FOREST_2,
            spaceAfter=10,
            uppercase=True,
        ),
        "cover_title": ParagraphStyle(
            "cover_title",
            parent=base["Title"],
            fontName="Times-Bold",
            fontSize=34,
            leading=36,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=16,
        ),
        "cover_body": ParagraphStyle(
            "cover_body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=12,
            leading=18,
            textColor=INK_SOFT,
            spaceAfter=16,
        ),
        "step_title": ParagraphStyle(
            "step_title",
            parent=base["Heading1"],
            fontName="Times-Bold",
            fontSize=27,
            leading=30,
            textColor=INK,
            spaceAfter=10,
        ),
        "lead": ParagraphStyle(
            "lead",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=16,
            textColor=INK_SOFT,
            spaceAfter=16,
        ),
        "heading": ParagraphStyle(
            "heading",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            textColor=FOREST,
            spaceBefore=7,
            spaceAfter=7,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14,
            textColor=INK_SOFT,
            spaceAfter=7,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=14,
            leftIndent=12,
            firstLineIndent=-8,
            textColor=INK_SOFT,
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=12,
            textColor=INK_SOFT,
        ),
        "card_title": ParagraphStyle(
            "card_title",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            textColor=FOREST,
            spaceAfter=5,
        ),
        "url": ParagraphStyle(
            "url",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=13,
            textColor=FOREST_2,
            alignment=TA_CENTER,
        ),
    }


ST = styles()


def bullet(text):
    return Paragraph(f"- {text}", ST["bullet"])


def label(text):
    table = Table(
        [[Paragraph(text.upper(), ST["small"])]],
        colWidths=[58 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), AMBER_SOFT),
                ("TEXTCOLOR", (0, 0), (-1, -1), FOREST),
                ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#E8C79C")),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def card(title, body, width=78 * mm, background=SURFACE):
    content = [
        Paragraph(title, ST["card_title"]),
        Paragraph(body, ST["small"]),
    ]
    table = Table([[content]], colWidths=[width], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("BOX", (0, 0), (-1, -1), 0.6, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 12),
                ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 11),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
            ]
        )
    )
    return table


def two_cards(left_title, left_body, right_title, right_body):
    table = Table(
        [[card(left_title, left_body), card(right_title, right_body)]],
        colWidths=[82 * mm, 82 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def tip_box(title, text, tone="mint"):
    background = MINT_SOFT if tone == "mint" else AMBER_SOFT
    border = FOREST_2 if tone == "mint" else AMBER
    table = Table(
        [[Paragraph(title, ST["card_title"]), Paragraph(text, ST["small"])]],
        colWidths=[42 * mm, 120 * mm],
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), background),
                ("BOX", (0, 0), (-1, -1), 0.7, border),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 10),
                ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                ("TOPPADDING", (0, 0), (-1, -1), 9),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
            ]
        )
    )
    return table


def step_header(number, title, lead):
    return [
        label(f"Step {number} of 5"),
        Spacer(1, 9 * mm),
        Paragraph(title, ST["step_title"]),
        Paragraph(lead, ST["lead"]),
    ]


def build_story():
    story = []

    story.extend(
        [
            Spacer(1, 19 * mm),
            Paragraph("CHANNEL ISLANDS | IFRS 18 READINESS", ST["cover_kicker"]),
            Paragraph("See the likely impact of IFRS 18 in five easy steps.", ST["cover_title"]),
            Paragraph(
                "Use the IFRS 18 Presentation Pathfinder to create a visual first-pass view of "
                "category changes, illustrative subtotals, disclosure workstreams and transition priorities.",
                ST["cover_body"],
            ),
            Spacer(1, 7 * mm),
            two_cards(
                "What it gives you",
                "An indicative IFRS 18 structure, judgement labels, technical-basis references, disclosure previews and a prioritised action list.",
                "What it does not do",
                "It does not reach an accounting opinion, prepare complete disclosures or replace entity-specific technical analysis.",
            ),
            Spacer(1, 12 * mm),
            tip_box(
                "Your data stays local",
                "The tool runs in your browser. It has no backend, account, cookies or analytics. Save a working file if you want to continue later.",
                "mint",
            ),
            Spacer(1, 12 * mm),
            Table(
                [[Paragraph(f'<link href="{LIVE_URL}">{LIVE_URL}</link>', ST["url"])]],
                colWidths=[164 * mm],
                hAlign="LEFT",
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), colors.white),
                        ("BOX", (0, 0), (-1, -1), 0.8, FOREST),
                        ("LEFTPADDING", (0, 0), (-1, -1), 12),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                        ("TOPPADDING", (0, 0), (-1, -1), 10),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
                    ]
                ),
            ),
            Spacer(1, 7 * mm),
            Paragraph(
                "Rules reviewed 5 July 2026, including the June 2026 IAS 28 fair-value-option amendments.",
                ST["small"],
            ),
            PageBreak(),
        ]
    )

    story.extend(step_header(1, "Choose the closest profile.", "Start with a profile that resembles the reporting entity, then adjust the assumptions."))
    story.extend(
        [
            Paragraph("What to do", ST["heading"]),
            bullet("Choose one of the fourteen example profiles or select Custom profile."),
            bullet("Select whether investing in assets or financing customers is a main business activity."),
            bullet("If investing is selected, choose whether the illustration relates mainly to financial assets, other assets, or remains unassessed."),
            bullet("Review the statement-of-financial-position and financing-liability policy choices."),
            Spacer(1, 4 * mm),
            two_cards(
                "Treat profiles as a starting lens",
                "A fund administrator does not automatically inherit the activities of the funds it services. A PCC result does not automatically apply to every cell or reporting layer.",
                "Use the reporting entity",
                "IFRS 18 main-business-activity conclusions are assessed for the reporting entity as a whole and must be supported by evidence.",
            ),
            Spacer(1, 8 * mm),
            tip_box(
                "Look for the profile lens",
                "The first warning in the results explains the key assumption built into the selected example. Read it before interpreting the numbers.",
                "amber",
            ),
            Spacer(1, 6 * mm),
            Paragraph("Technical pointers: IFRS 18.49-51 and B30-B41.", ST["small"]),
            PageBreak(),
        ]
    )

    story.extend(step_header(2, "Set the presentation choices and add key lines.", "Use a consistent unit and enter enough information to reveal the likely shape of the change."))
    story.extend(
        [
            Paragraph("What to do", ST["heading"]),
            bullet("Choose nature, function or mixed operating-expense presentation."),
            bullet("Select the relevant transition, interim, MPM, EPS and digital-reporting indicators."),
            bullet("Enter income as positive and expenses as negative. The tool warns about unusual signs."),
            bullet("For function or mixed presentation, specified nature totals are treated as note inputs to reduce automatic double counting."),
            Spacer(1, 4 * mm),
            two_cards(
                "Associates and joint ventures",
                "Use the equity-method line for share of profit. Use the separate FVTPL line only where the IAS 28 fair-value option is eligible and elected.",
                "Cash and cash equivalents",
                "The illustrative category uses the selected investment activity and customer-financing policy. Confirm the detailed IFRS 18.56 facts separately.",
            ),
            Spacer(1, 8 * mm),
            tip_box(
                "Do not force precision",
                "The tool is designed for scoping. Use broad, consistent amounts to see the likely impact, then move to a detailed ledger-level assessment where the result is material.",
                "mint",
            ),
            Spacer(1, 6 * mm),
            Paragraph("Technical pointers: IFRS 18.53-68, 78-85 and IAS 28.18-19.", ST["small"]),
            PageBreak(),
        ]
    )

    story.extend(step_header(3, "Read the visual IFRS 18 structure.", "Compare the input lines with the indicative five-category presentation and subtotals."))
    story.extend(
        [
            Paragraph("What to look for", ST["heading"]),
            bullet("Operating, investing, financing, income taxes and discontinued operations are shown separately."),
            bullet("Operating profit and profit before financing and income taxes are calculated from the selected assumptions."),
            bullet("Rule-based and judgement labels show where further analysis is more likely."),
            bullet("Each populated line includes a rationale and technical-basis reference."),
            Spacer(1, 4 * mm),
            two_cards(
                "Illustrative subtotal",
                "The subtotal is useful for seeing the possible shape of the future statement. It remains dependent on the amounts, assumptions and policy selections entered.",
                "PBFIT exception",
                "The subtotal is not applied where the selected IFRS 18.65(a)(ii) policy results in the paragraph 73 exception. Confirm the full liability population.",
            ),
            Spacer(1, 8 * mm),
            tip_box(
                "Use the impact summary",
                "The three summary cards show populated lines, judgement-labelled lines and highlighted disclosure or presentation workstreams.",
                "amber",
            ),
            Spacer(1, 6 * mm),
            Paragraph("Technical pointers: IFRS 18.47-74.", ST["small"]),
            PageBreak(),
        ]
    )

    story.extend(step_header(4, "Explore the disclosure and transition previews.", "Use the result to understand the work required, not as completed disclosure wording."))
    story.extend(
        [
            Paragraph("Open the disclosure cards", ST["heading"]),
            bullet("Review the trigger, explanation, suggested wording and technical basis."),
            bullet("Use suggested wording as a drafting prompt and adapt it to the entity's facts."),
            bullet("Review amended IAS 7 cash-flow implications separately from profit-or-loss categories."),
            Paragraph("Use the four guided previews", ST["heading"]),
            bullet("Specified expenses: see the five totals entered and the allocation work still outstanding."),
            bullet("MPM helper: screen the measure and review the paragraph 123 disclosure components."),
            bullet("Transition mapping: see the populated input lines and illustrative IFRS 18 categories."),
            bullet("Evidence questions: prepare the matters management, advisers and auditors are likely to ask."),
            Spacer(1, 5 * mm),
            tip_box(
                "Important boundary",
                "The allocation table, MPM wording and transition schedule are previews. They do not represent a completed paragraph 83 note, MPM note or IFRS 18.C3 reconciliation.",
                "amber",
            ),
            Spacer(1, 6 * mm),
            Paragraph(
                "Technical pointers: IFRS 18.83-85, 117-125, B113-B142 and C2-C6; amended IAS 7.",
                ST["small"],
            ),
            PageBreak(),
        ]
    )

    story.extend(step_header(5, "Save the result and decide what happens next.", "Keep the scoping output, share the discussion points and start detailed work before the audit timetable tightens."))
    story.extend(
        [
            Paragraph("Save or share", ST["heading"]),
            bullet("Download the local JSON working file if you want to reload the scenario later."),
            bullet("Export CSV for the mapped lines, confidence labels, rationale and technical basis."),
            bullet("Use Print view to save the complete result as a PDF for an internal discussion."),
            bullet("Remember that a downloaded file contains the figures entered and should be stored appropriately."),
            Spacer(1, 4 * mm),
            two_cards(
                "A detailed assessment may be needed when",
                "Categories move materially, judgement-labelled lines are significant, MPMs are used, function expense presentation applies, or transition data is not readily available.",
                "Prepare before contacting an adviser",
                "Bring the current financial statements, trial balance mapping, public performance measures, cash-flow policy, reporting perimeter and management reporting evidence.",
            ),
            Spacer(1, 9 * mm),
            tip_box(
                "Do not wait for the year-end audit",
                "IFRS 18 applies for annual periods beginning on or after 1 January 2027 and requires retrospective comparative work. Early scoping creates time to resolve data and judgement gaps.",
                "mint",
            ),
            Spacer(1, 10 * mm),
            Table(
                [[Paragraph(f'<link href="{LINKEDIN_URL}" color="#FFFFFF">Contact Gerrit Heyneke on LinkedIn</link>', ST["url"])]],
                colWidths=[164 * mm],
                hAlign="LEFT",
                style=TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), FOREST),
                        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
                        ("BOX", (0, 0), (-1, -1), 0.8, FOREST),
                        ("LEFTPADDING", (0, 0), (-1, -1), 12),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
                        ("TOPPADDING", (0, 0), (-1, -1), 11),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
                    ]
                ),
            ),
            Spacer(1, 7 * mm),
            Paragraph(
                "This independent guide and tool are not affiliated with or endorsed by the IFRS Foundation. "
                "They provide indicative scoping information only and do not constitute accounting advice.",
                ST["small"],
            ),
        ]
    )

    return story


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = BaseDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=31 * mm,
        bottomMargin=22 * mm,
        title="IFRS 18 Presentation Pathfinder - Five-Step User Guide",
        author="Gerrit Heyneke",
        subject="How to use the IFRS 18 Presentation Pathfinder in five easy steps",
    )
    frame = Frame(
        doc.leftMargin,
        doc.bottomMargin,
        doc.width,
        doc.height,
        id="normal",
        leftPadding=0,
        rightPadding=0,
        topPadding=0,
        bottomPadding=0,
    )
    doc.addPageTemplates([PageTemplate(id="guide", frames=[frame], onPage=page_header_footer)])
    doc.build(build_story())
    print(OUTPUT)


if __name__ == "__main__":
    build()
