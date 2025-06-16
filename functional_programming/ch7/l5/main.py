def create_markdown_image(alt_text):
    enclosed_text = f"![{alt_text}]"

    def encode_url(url):
        new_open = url.replace("(", "%28")
        new_close = new_open.replace(")", "%29")
        enclosed_url = f"({new_close})"
        text_url = f"{enclosed_text}{enclosed_url}"

        def encode_title(title=None):
            if title == None:
                return text_url
            enclosed_title = f' "{title}")'
            complete_syntax = text_url.replace(")", enclosed_title)
            return complete_syntax
        return encode_title
    return encode_url

