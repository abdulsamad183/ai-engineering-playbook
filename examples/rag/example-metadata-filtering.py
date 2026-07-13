"""Metadata filtering before vector search.

Run: python example-metadata-filtering.py
"""


def filter_chunks(chunks: list[dict], user_tenant: str, user_groups: set[str]) -> list[dict]:
    result = []
    for c in chunks:
        if c.get("tenant_id") != user_tenant:
            continue
        acl = set(c.get("acl", []))
        if acl and acl.isdisjoint(user_groups) and "public" not in acl:
            continue
        result.append(c)
    return result


if __name__ == "__main__":
    chunks = [
        {"id": "1", "tenant_id": "acme", "acl": ["group:support"], "text": "policy"},
        {"id": "2", "tenant_id": "other", "acl": ["public"], "text": "other"},
    ]
    print(filter_chunks(chunks, "acme", {"group:support"}))
