from __future__ import annotations

import abc
from collections import Counter, deque
from typing import Self, Sequence

from utils import get_input, submit


class HuffmanNode(abc.ABC):
    """Generic node of a Huffman tree."""

    def __init__(self, weight: int) -> None:
        self.weight = weight
        self.value = ""


class HuffmanLeafNode(HuffmanNode):
    """Leaf node of a Huffman tree."""

    def __init__(self, weight: int, value: str) -> None:
        super().__init__(weight)
        self.value = value


class HuffmanInternalNode(HuffmanNode):
    """Non-leaf node of a Huffman tree."""

    def __init__(
        self,
        weight: int,
        left: HuffmanNode | None = None,
        right: HuffmanNode | None = None,
    ) -> None:
        super().__init__(weight)
        self.left = left
        self.right = right
        self.value = (self.left.value if self.left else "") + (
            self.right.value if self.right else ""
        )


class HuffmanTree:
    """A Huffman tree."""

    def __init__(self, root: HuffmanNode | None = None) -> None:
        self.root = root

    @property
    def value(self) -> str:
        if not self.root:
            return ""
        return self.root.value

    @property
    def weight(self) -> int:
        """Weight of the tree, stored in the root."""
        if self.root is None:
            return 0
        return self.root.weight

    @classmethod
    def from_frequency(cls, frequency: Counter[str]) -> Self:
        """Build a Huffman tree from a collection of character frequencies."""
        nodes = [
            HuffmanTree(root=HuffmanLeafNode(weight=count, value=character))
            for character, count in frequency.items()
        ]
        if not nodes:
            return HuffmanTree()
        while len(nodes) > 1:
            nodes = HuffmanTree.huffman_tree_step(nodes)
        return nodes[0]

    @staticmethod
    def huffman_tree_step(
        elements: Sequence[HuffmanTree],
    ) -> list[HuffmanTree]:
        """A single step of the Huffman tree construction.

        Take a list of nodes or partial Huffman trees, and combine
        the two with lowest weight."""
        elements = sorted(elements, key=lambda x: (x.weight, x.value))
        new_element = HuffmanTree.huffman_merge(*elements[:2])
        elements = elements[2:] + [new_element]
        return elements

    @staticmethod
    def huffman_merge(
        element_left: HuffmanTree, element_right: HuffmanTree
    ) -> HuffmanTree:
        """Combine two Huffman trees."""
        combined_weight = element_left.weight + element_right.weight
        root = HuffmanInternalNode(
            weight=combined_weight, left=element_left.root, right=element_right.root
        )
        tree = HuffmanTree(root=root)
        return tree

    def generate_table(self) -> dict[str, str]:
        """Generate the prefix-code table from the tree."""
        table: dict[str, str] = {}
        if self.root is None:
            return table
        queue: deque[tuple[HuffmanNode | None, str]] = deque([(self.root, "")])
        while queue:
            node, prefix = queue.popleft()
            if isinstance(node, HuffmanLeafNode):
                table[node.value] = prefix
            elif isinstance(node, HuffmanInternalNode):
                queue.append((node.left, f"{prefix}0"))
                queue.append((node.right, f"{prefix}1"))
        return table


def decode_text(encoded_text: str, prefix_table: dict[str, str]) -> str:
    decoded_text = ""
    char = ""
    table = {v: k for k, v in prefix_table.items()}
    for bit in encoded_text:
        char += bit
        if char in table:
            decoded_text += table[char]
            char = ""
    return decoded_text


def main() -> str:
    data = get_input(24).split("\n")
    text, answer = data
    huffman_tree = HuffmanTree.from_frequency(Counter(text))
    prefix_table = huffman_tree.generate_table()
    return decode_text(answer, prefix_table)


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(24, ANSWER)
