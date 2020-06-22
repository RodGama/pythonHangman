def what_to_do(instructions):
    if instructions.startswith("Simon says"):
        text = instructions.replace("Simon says", "")
        text = text.lstrip()
        return "I " + text
    elif instructions.endswith("Simon says"):
        text = instructions.replace("Simon says", "")
        text = text.rstrip()
        return "I " + text
    else:
        return "I won't do it!"
