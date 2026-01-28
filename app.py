from flask import Flask, render_template, request
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None


def build_prompt(topic, platform):
    if platform == "LinkedIn":
        return f"""
Write a LinkedIn post about "{topic}".

FORMAT:
- Title line
- Blank line
- Short professional paragraph
- Blank line
- Section header
- Blank line
- Bullet points (each on new line)
- Blank line
- Closing paragraph
- Blank line
- CTA
- Hashtags at end

RULES:
- Keep empty lines
- Clean spacing
- Professional tone
- 

Return ONLY the formatted content.
"""

    elif platform == "Instagram":
        return f"""
Write an Instagram caption about "{topic}".

FORMAT:
- Hook line
- Blank line
- Short punchy lines
- Blank line
- Emojis allowed
- Line breaks for readability
- Hashtags at end

RULES:
- Keep spacing
- Casual and engaging

Return ONLY the formatted content.
"""

    elif platform == "Twitter":
        return f"""
Write a Twitter/X post about "{topic}".

FORMAT:
- Short lines
- Line breaks allowed
- Concise
- Emojis optional
- No long paragraphs

Return ONLY the formatted content.
"""

    else:  # Blog
        return f"""
Write a blog-style post about "{topic}".

FORMAT:
- Title
- Blank line
- Paragraphs (2–4 lines each)
- Blank line between paragraphs
- No emojis unless relevant

Return ONLY the formatted content.
"""


@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        topic = request.form.get("topic")
        platform = request.form.get("platform")

        prompt = build_prompt(topic, platform)

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            output = response.text.strip()

        except Exception:
            output = "⚠️ AI temporarily unavailable."

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
