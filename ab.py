from PIL import Image, ImageDraw, ImageFont

# Text to write
text = """Hello Krish,
This is your handwritten note made with Python!

Stay consistent in learning AI :)"""

# Create a blank white image
img = Image.new('RGB', (800, 400), color=(255, 255, 255))
d = ImageDraw.Draw(img)

# Load a handwriting-style font (You need to download one)
font = ImageFont.truetype("LucidaHandwritingItalic.ttf", 24)

# Write text on the image
d.multiline_text((20, 20), text, font=font, fill=(0, 0, 255))  # Blue ink

# Save image
img.save("krish_handwritten.png")
print("✅ Handwritten-style image saved!")
