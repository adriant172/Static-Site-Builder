

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if not self.props:
            return ""
        attributes = []
        for key in self.props:
            attributes.append(f' {key}="{self.props[key]}"')
        attributes = "".join(attributes)
        return attributes
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None,  props)
    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes require a value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent node require a tag.")
        if not self.children:
            raise ValueError("Parent nodes require children, please create a leaf node instead.")
        children_string = ""
        for child in self.children:
            children_string += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_string}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"