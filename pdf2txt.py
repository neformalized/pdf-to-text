import fitz

#

def block_handler(data: dict, links: list[dict]) -> str:
    
    if data["type"] == 0: return block_text(data, links)
    if data["type"] == 1: return block_image(data)
    
    print("echo bad one")
#

def block_text(data: dict, links: list[dict]) -> str:
    
    results = list()
    
    for line in data["lines"]:
        
        for item in line["spans"]:
            
            results.append(item["text"])
            
            if item["text"] == "Modifiers": print(item)
        #
    #
    
    return " ".join(results)
#

def block_image(data: dict) -> str:
    
    #print(data)
    return data["image"]
#

doc = fitz.open("C:\\Users\\omni\\Desktop\\topic-201.pdf")

for i, page in enumerate(doc):
    
    page_cur = page.get_text("dict")
    page_links = page.get_links()
    
    print(f"cur page {i}")
    
    for block in page_cur["blocks"]:
        
        extracted = block_handler(block, page_links)
        
        print(extracted)
    #
#