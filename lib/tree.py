class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        if self.root is None:
            return None

        def depth_first_traversal(node):
            if node['id'] == target_id:
                return node
            for child in node['children']:
                result = depth_first_traversal(child)
                if result:
                    return result
            return None

        def breadth_first_traversal(node):
            queue = [node]
            while queue:
                current_node = queue.pop(0)
                if current_node['id'] == target_id:
                    return current_node
                queue.extend(current_node['children'])
            return None

        return depth_first_traversal(self.root)

if __name__ == "__main__":
    child1 = {
        'tag_name': 'div',
        'id': 'child1',
        'text_content': 'Child 1',
        'children': []
    }
    
    child2 = {
        'tag_name': 'div',
        'id': 'child2',
        'text_content': 'Child 2',
        'children': []
    }
    
    root = {
        'tag_name': 'div',
        'id': 'root',
        'text_content': 'Root',
        'children': [child1, child2]
    }

    tree = Tree(root)

    found_element = tree.get_element_by_id('child1')
    if found_element:
        print(f"Element found: {found_element}")
    else:
        print("Element not found.")
