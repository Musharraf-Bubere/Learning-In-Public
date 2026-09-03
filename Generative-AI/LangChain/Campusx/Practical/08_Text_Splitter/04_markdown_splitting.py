from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
# My Markdown Document

## Section 1: Introduction
Welcome to your new Markdown file! This is a standard paragraph of text. You can add formatting easily using plain text symbols. For example, you can make text **bold** or *italicized*. If you want to cross something out, you can use ~~strikethrough~~.

### Sub-section: Quick Links
If you need to link to an external website, you can do it like this: [Visit Google](https://google.com).

---

## Section 2: Organized Information
Here is how you can organize your thoughts using different types of lists and tables.

### Bulleted List
- First main point
- Second main point
  - Sub-point A
  - Sub-point B
- Third main point

### Numbered Steps
1. Complete the first task.
2. Move on to the second task.
3. Finish the final step.

### Data Table

| Item Name | Quantity | Status |
| :--- | :---: | :--- |
| Laptops | 5 | Shipped |
| Monitors | 10 | Pending |
| Keyboards | 15 | In Stock |

---

## Section 3: Technical and Extra Elements
You can also include quotes and code snippets directly in your document.

### Blockquote
> "The best way to predict the future is to invent it." 
> — *Alan Kay*

### Code Examples
You can share inline code like `npm install`, or write out entire blocks of code with syntax highlighting:

```javascript
function sayHello() {
    console.log("Hello, world!");
}
sayHello();
```

### Task Checklist
- [x] Create the markdown template
- [ ] Add more content
- [ ] Share with the team
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=400,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])