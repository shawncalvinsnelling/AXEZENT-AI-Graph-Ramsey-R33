import itertools, json
from pathlib import Path

def edges(n):
    return [(i, j) for i in range(n) for j in range(i + 1, n)]

def has_mono_triangle(n, bits):
    e = edges(n)
    color = {edge: (bits >> idx) & 1 for idx, edge in enumerate(e)}
    for a, b, c in itertools.combinations(range(n), 3):
        vals = [color[tuple(sorted(x))] for x in [(a, b), (a, c), (b, c)]]
        if vals[0] == vals[1] == vals[2]:
            return True
    return False

def lower_coloring_k5():
    cycle = {tuple(sorted(x)) for x in [(0,1),(1,2),(2,3),(3,4),(4,0)]}
    bits = 0
    for idx, edge in enumerate(edges(5)):
        if edge in cycle:
            bits |= (1 << idx)
    return bits

def verify():
    lower = not has_mono_triangle(5, lower_coloring_k5())
    total = 1 << len(edges(6))
    bad = 0
    for bits in range(total):
        if not has_mono_triangle(6, bits):
            bad += 1
            break
    return {"theorem": "R(3,3)=6", "lower_bound_k5": lower, "k6_colorings_checked": total, "k6_avoiders_found": bad, "truth_label": "FINITE_CERTIFICATE", "status": "PASS" if lower and bad == 0 else "FAIL"}

def main():
    r = verify()
    Path("receipts").mkdir(exist_ok=True)
    Path("receipts/r33_receipt.json").write_text(json.dumps(r, indent=2), encoding="utf-8")
    print(json.dumps(r, indent=2))
    raise SystemExit(0 if r["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
