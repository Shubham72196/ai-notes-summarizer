def generate_summary(text):

    # Split into sentences
    sentences = text.split('.')

    # Take first 2 sentences as summary
    summary = '. '.join(sentences[:2])

    return summary