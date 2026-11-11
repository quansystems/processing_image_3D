# Cau 2. Loc dam may diem theo Z
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from stl_utils import tao_dam_may_diem

_, _, diem = tao_dam_may_diem("ball.STL")
z = diem[:, 2]

# a. Tinh z_min, z_max, z_mid
z_min, z_max = z.min(), z.max()
z_mid = (z_min + z_max) / 2
print(f"a. z_min = {z_min:.4f}, z_max = {z_max:.4f}, z_mid = {z_mid:.4f}")

# b. Giu cac diem co z >= z_mid
mask = z >= z_mid
diem_giu = diem[mask]
diem_loai = diem[~mask]
print("b. So diem giu lai:", len(diem_giu), "/", len(diem))

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection="3d")
ax.scatter(diem_giu[:, 0], diem_giu[:, 1], diem_giu[:, 2], s=5, c="#0891B2", label="Giu (z >= z_mid)")
ax.scatter(diem_loai[:, 0], diem_loai[:, 1], diem_loai[:, 2], s=5, c="#F97316", alpha=0.4, label="Loai (z < z_mid)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title(f"Cau 2: Loc theo Z (z_mid = {z_mid:.2f})")
ax.set_box_aspect((1, 1, 1))
ax.legend()
Path("output").mkdir(parents=True, exist_ok=True)
plt.savefig("output/bai2_loc_z.png", dpi=120)
plt.show()
