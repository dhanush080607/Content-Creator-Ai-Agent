from flask import Flask, render_template, request

app = Flask(__name__)


def build_demo_output(topic, platform, tone, count):
    count = int(count)

    variations = ""

    for i in range(1, count + 1):
        variations += f"""
🔹 Variation {i}

Hook:
Did you know how {topic} is transforming the future of content creation? 🚀

Main Content:
{topic} is no longer just a trend — it’s becoming a powerful tool for creators and businesses.
When used effectively on {platform}, it helps improve reach, engagement, and consistency.

Key Points:
• Tailored for {platform}
• Tone: {tone}
• Clear, engaging structure
• Optimized for audience interaction

Call to Action:
What’s your opinion on {topic}? Share your thoughts 👇

────────────────────────────
"""

    return f"""
✨ AI Content Generated Successfully ✨

Platform: {platform}
Topic: {topic}
Tone: {tone}
Total Variations: {count}

────────────────────────────

{variations}

Hashtags:
#AI #ContentCreation #Flask #Python #WebDevelopment

🧠 Developer Note:
This project is currently running in demo mode.
Live AI models (Gemini / OpenAI) can be integrated anytime.
"""


@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        topic = request.form.get("topic")
        platform = request.form.get("platform")
        tone = request.form.get("tone")
        count = request.form.get("count", 1)

        output = build_demo_output(topic, platform, tone, count)

    return render_template("index.html", output=output)


if __name__ == "__main__":
    app.run(debug=True)
