from pymonad.tools import curry

#2.1
@curry(2)
def tag(tag_name: str, value: str) -> str:
    return f"<{tag_name}>{value}</{tag_name}>"

bold = tag("b")
italic = tag("i")

print(bold("hello")) 
print(italic("hello")) 

#2.2
@curry(3)
def tag(tag_name: str, attr: dict, value: str) -> str:
    attrs = " ".join(f'{k}="{v}"' for k, v in attr.items())
    attrs_str = f" {attrs}" if attrs else ""

    return f"<{tag_name}{attrs_str}>{value}</{tag_name}>"

print(tag("li", {"class": "list-group"}, "item 23"))
