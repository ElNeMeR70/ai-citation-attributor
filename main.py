"""RAG Citation & Source Grounding Attributor"""

def attribute_statement(statement, sources):
    words = set(statement.lower().split())
    best_src = None
    best_overlap = 0
    for idx, src in enumerate(sources):
        overlap = len(words & set(src.lower().split()))
        if overlap > best_overlap:
            best_overlap = overlap
            best_src = idx + 1
    return f"{statement} [Source #{best_src}]"

if __name__ == "__main__":
    print("[RUN] RAG Citation Attributor...")
    st = "Transformers use self-attention mechanisms."
    srcs = ["Attention mechanisms allow transformers to scale.", "Convolutional layers process 2D images."]
    cited = attribute_statement(st, srcs)
    print(f"[OK] Grounded Citation: {cited}")
