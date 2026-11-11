# Cau 3. Tao anh do sau tu dam may diem
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from stl_utils import tao_dam_may_diem

_, _, diem = tao_dam_may_diem("ball.STL")
x, y, z = diem[:, 0], diem[:, 1], diem[:, 2]
KICH_THUOC = 64

# a. Chia [x_min, x_max], [y_min, y_max] thanh 64 o; X -> cot u, Y -> hang v
x_min, x_max = x.min(), x.max()
y_min, y_max = y.min(), y.max()
z_min = z.min()
u = np.floor((x - x_min) / (x_max - x_min) * KICH_THUOC).astype(int)
v = np.floor((y - y_min) / (y_max - y_min) * KICH_THUOC).astype(int)
u = np.clip(u, 0, KICH_THUOC - 1)  # diem o bien tren (x = x_max) thuoc o 63
v = np.clip(v, 0, KICH_THUOC - 1)

# b. Tao depth 64x64 = NaN; camera nhin theo +Z -> giu gia tri z - z_min nho nhat
depth = np.full((KICH_THUOC, KICH_THUOC), np.nan)
for i in range(len(diem)):
    d = z[i] - z_min
    if np.isnan(depth[v[i], u[i]]) or d < depth[v[i], u[i]]:
        depth[v[i], u[i]] = d

# c. Hien thi anh do sau kem thang mau, in so pixel co du lieu
so_pixel = np.count_nonzero(~np.isnan(depth))
print("c. So pixel co du lieu:", so_pixel, "/", KICH_THUOC * KICH_THUOC)

plt.figure(figsize=(6, 5))
plt.imshow(depth, cmap="magma", origin="lower")
plt.colorbar(label="z - z_min")
plt.xlabel("u (cot, theo X)")
plt.ylabel("v (hang, theo Y)")
plt.title("Cau 3: Anh do sau 64x64")
Path("output").mkdir(parents=True, exist_ok=True)
plt.savefig("output/bai3_depth.png", dpi=120)
plt.show()
