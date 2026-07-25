import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Node definitions: id -> (label, x, y, wing_color_key, kind)
nodes = {
    "A1": ("A1\nThe Rotunda\n(ANCHOR)", 6, 9, "A", "anchor"),
    "A2": ("A2\nThe Nave\n2x Chapel Penitent", 6, 7.3, "A", "combat"),
    "A3": ("A3\nSide Chantry\n(cleared)", 4, 7.3, "A", "empty"),
    "A4": ("A4\nDrained Plunge-Bath\nNell's rota", 6, 5.6, "A", "lore"),
    "A5": ("A5\nSunken Chapel\n2x Brine Spitter", 6, 3.9, "A", "combat"),
    "B1": ("B1\nThe Vestry\n(cleared)", 3.7, 3.9, "B", "empty"),
    "B2": ("B2\nRobing Gallery", 1.8, 3.9, "B", "normal"),
    "B3": ("B3\nRobing Annex\nBathhouse Flailer\nQ: 2nd Name", 1.8, 5.6, "B", "quest"),
    "B4": ("B4\nDrowned Sacristy\n2x Brine + Custodian\nQ: Ledger & Key", 0, 3.9, "B", "quest"),
    "C1": ("C1\nFunicular Housing\nCustodian\nFunicular Spike!", 6, 2.1, "C", "quest"),
    "C2": ("C2\nFunicular Shaft\n(fall hazard)", 6, 0.4, "C", "hazard"),
    "C3": ("C3\nLower Rail Landing\n3-window mechanism", 4, 0.4, "C", "puzzle"),
    "C4": ("C4\nBrake Room (locked)\nQ: log + Salts", 4, -1.3, "C", "quest"),
    "D1": ("D1\nChoir Loft\nMarble Attendant", 8.2, 7.3, "D", "combat"),
    "D2": ("D2\nChoir Archive\nQ: Nell's Book", 8.2, 5.6, "D", "quest"),
    "E1": ("E1\nBell Tower Base\nBellkeeper", 10.2, 5.6, "E", "combat"),
    "E2": ("E2\nStair Midpoint\nBellkeeper", 10.2, 3.9, "E", "combat"),
    "E3": ("E3\nBell Chamber\nQ: SILENCE THE BELL\n(capstone)", 10.2, 2.1, "E", "capstone"),
    "F1": ("F1\nCrypt Alcove\n(secret, brother thread)", 8.2, 3.9, "F", "secret"),
}

edges_normal = [
    ("A1","A2"), ("A2","A3"), ("A2","A4"), ("A4","A5"),
    ("A5","B1"), ("B1","B2"), ("B2","B4"),
    ("C1","C2"), ("C2","C3"), ("C3","C4"),
    ("D1","D2"), ("D2","E1"), ("E1","E2"), ("E2","E3"),
]
edges_hidden = [
    ("B2","B3"),   # loose panel
    ("A5","F1"),   # rubble
    ("C4","C3"),   # key-gated, drawn same as normal but labeled
]
edges_shortcut = [
    ("A1","C1"),   # bronze door, opens after C3 solved
    ("D1","A1"),   # one-way drop
]
edges_stair = [
    ("A2","D1"),   # stair up to loft
]

wing_colors = {
    "A": "#6f8faf", "B": "#a3785c", "C": "#7a8c5e",
    "D": "#8c6f9e", "E": "#b06a6a", "F": "#555555",
}
kind_edge = {
    "anchor": "#f2d94e", "combat": "#c0392b", "quest": "#d4a017",
    "empty": "#888888", "lore": "#4a90a4", "puzzle": "#2e8b57",
    "hazard": "#8b4513", "capstone": "#8e1a1a", "secret": "#333333",
    "normal": "#444444",
}

fig, ax = plt.subplots(figsize=(15, 13))
ax.set_facecolor("#1c1a17")
fig.patch.set_facecolor("#1c1a17")

def draw_edge(a, b, style="-", color="#cfc9b8", lw=2, curve=0.0):
    x1, y1 = nodes[a][1], nodes[a][2]
    x2, y2 = nodes[b][1], nodes[b][2]
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                             connectionstyle=f"arc3,rad={curve}",
                             arrowstyle="-", color=color, lw=lw,
                             linestyle=style, zorder=1)
    ax.add_patch(arrow)

for a, b in edges_normal:
    draw_edge(a, b, style="-", color="#cfc9b8", lw=2.2)
for a, b in edges_hidden:
    draw_edge(a, b, style=(0, (2, 2)), color="#e0c26b", lw=2)
for a, b in edges_shortcut:
    draw_edge(a, b, style=(0, (6, 3)), color="#e05a2b", lw=2.6, curve=0.15)
for a, b in edges_stair:
    draw_edge(a, b, style=(0, (1, 1)), color="#cfc9b8", lw=2)

for nid, (label, x, y, wing, kind) in nodes.items():
    w, h = 1.55, 0.85
    box = FancyBboxPatch((x - w/2, y - h/2), w, h,
                          boxstyle="round,pad=0.06,rounding_size=0.08",
                          linewidth=2.2, edgecolor=kind_edge.get(kind, "#444444"),
                          facecolor=wing_colors[wing], alpha=0.92, zorder=2)
    ax.add_patch(box)
    ax.text(x, y, label, ha="center", va="center", fontsize=8.2,
            color="white", fontweight="bold", zorder=3, linespacing=1.3)

ax.set_xlim(-1.5, 12)
ax.set_ylim(-2.5, 10.2)
ax.axis("off")
ax.set_title("CHOIR DEEP — DEEP-RUN MASTER MAP  (DM-ONLY)", color="#e8c96b",
             fontsize=18, fontweight="bold", pad=20)

legend_patches = [
    mpatches.Patch(color=wing_colors["A"], label="Wing A — Nave & Rotunda"),
    mpatches.Patch(color=wing_colors["B"], label="Wing B — Vestry & Robing"),
    mpatches.Patch(color=wing_colors["C"], label="Wing C — Funicular Works"),
    mpatches.Patch(color=wing_colors["D"], label="Wing D — Choir Loft"),
    mpatches.Patch(color=wing_colors["E"], label="Wing E — Bell Tower"),
    mpatches.Patch(color=wing_colors["F"], label="Wing F — Secret"),
]
leg1 = ax.legend(handles=legend_patches, loc="upper left", bbox_to_anchor=(0, 1.0),
                  fontsize=9, facecolor="#2a2620", edgecolor="#666", labelcolor="white")
ax.add_artist(leg1)

from matplotlib.lines import Line2D
line_patches = [
    Line2D([0],[0], color="#cfc9b8", lw=2.2, label="Normal passage"),
    Line2D([0],[0], color="#e0c26b", lw=2, linestyle=(0,(2,2)), label="Hidden / key-gated"),
    Line2D([0],[0], color="#e05a2b", lw=2.6, linestyle=(0,(6,3)), label="Shortcut (engineered)"),
]
leg2 = ax.legend(handles=line_patches, loc="lower left", bbox_to_anchor=(0, 0),
                  fontsize=9, facecolor="#2a2620", edgecolor="#666", labelcolor="white")
ax.add_artist(leg2)

plt.tight_layout()
plt.savefig("choir-deep-deeprun-map.png", dpi=150, facecolor=fig.get_facecolor())
print("saved")
