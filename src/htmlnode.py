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
    def __init__(self, value, tag=None, children=None, props=None):
        super().__init__(tag, value, children, props)
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes require a value.")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
        
