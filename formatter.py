eq = " : "
next_line = "\n\n"


def formatter(data):
    arr = []
    out = ""
    if (data["NAMES"]):
        arr.append("Names")
        arr.append(eq)
        arr.append(",".join(set(data["NAMES"])))
        arr.append(next_line)
    if (data["EXTENSIONS"]):
        arr.append("Extenstions")
        arr.append(eq)
        arr.append(",".join(set(data["EXTENSIONS"])))
        arr.append(next_line)
    if (data["SOLUTIONS"]):
        arr.append("Solutions")
        arr.append(eq)
        arr.append(", \n".join(data["SOLUTIONS"]))
        arr.append(next_line)
    if (not data["SOLUTIONS"]):
        arr.append("Solutions")
        arr.append(eq)
        arr.append("No solutions found")
        arr.append(next_line)
    if (data["OTHER_INFO"]):
        arr.append("Other_info")
        arr.append(eq)
        arr.append(", \n".join(data["OTHER_INFO"]))
        arr.append(next_line)
    if (data["TEXTS"]):
        arr.append("Text information extracted")
        arr.append(eq)
        arr.append(", \n".join(data["TEXTS"]))
        arr.append(next_line)

    return "".join(arr)


print(formatter())
