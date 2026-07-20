def summarize(text):
    sentences = text.split(".")

    if len(sentences) <= 2:
        return text

    return ".".join(sentences[:2]) + "."