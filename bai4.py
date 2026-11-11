# Cau 4. Bo sung trong tam tam giac vao dam may diem
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from stl_utils import tao_dam_may_diem

tam_giac, _, diem = tao_dam_may_diem("ball.STL")

# a. Moi tam giac co ba dinh: lay trung binh theo truc 1.
trong_tam = tam_giac.mean(axis=1)
diem_bo_sung = np.unique(np.vstack((diem, trong_tam)), axis=0)
print("a. So trong tam:", len(trong_tam))
print("   So diem ban dau:", len(diem))
print("   So diem sau bo sung:", len(diem_bo_sung))

# b. Co dinh luoi chieu va moc do sau theo dam may diem o Cau 3.
KICH_THUOC = 64
x_min, y_min, z_min = diem.min(axis=0)
x_max, y_max, _ = diem.max(axis=0)


def tao_anh_do_sau(cac_diem):
    u = np.floor((cac_diem[:, 0] - x_min) / (x_max - x_min) * KICH_THUOC).astype(int)
    v = np.floor((cac_diem[:, 1] - y_min) / (y_max - y_min) * KICH_THUOC).astype(int)
    u = np.clip(u, 0, KICH_THUOC - 1)
    v = np.clip(v, 0, KICH_THUOC - 1)
    depth = np.full((KICH_THUOC, KICH_THUOC), np.nan)
    # Tu cap nhat tung o: camera nhin theo +Z, giu do sau nho nhat.
    for i in range(len(cac_diem)):
        d = cac_diem[i, 2] - z_min
        if np.isnan(depth[v[i], u[i]]) or d < depth[v[i], u[i]]:
            depth[v[i], u[i]] = d
    return depth


depth_truoc = tao_anh_do_sau(diem)
depth_sau = tao_anh_do_sau(diem_bo_sung)
so_truoc = np.count_nonzero(~np.isnan(depth_truoc))
so_sau = np.count_nonzero(~np.isnan(depth_sau))
print(f"c. So pixel co du lieu truoc: {so_truoc} / {KICH_THUOC ** 2}")
print(f"   So pixel co du lieu sau  : {so_sau} / {KICH_THUOC ** 2}")
print(f"   So pixel tang them      : {so_sau - so_truoc}")

# Dung chung gioi han mau cho ca hai anh.
vmin = min(np.nanmin(depth_truoc), np.nanmin(depth_sau))
vmax = max(np.nanmax(depth_truoc), np.nanmax(depth_sau))
fig, axes = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
for ax, depth, tieu_de in zip(
    axes,
    (depth_truoc, depth_sau),
    (f"Truoc: {so_truoc} pixel", f"Sau: {so_sau} pixel (+{so_sau - so_truoc})"),
):
    anh = ax.imshow(depth, cmap="magma", origin="lower", vmin=vmin, vmax=vmax)
    ax.set_title(tieu_de)
    ax.set_xlabel("u (cot, theo X)")
    ax.set_ylabel("v (hang, theo Y)")
fig.colorbar(anh, ax=axes, label="z - z_min")
fig.suptitle("Cau 4: Bo sung trong tam tam giac - luoi 64x64")
Path("output").mkdir(parents=True, exist_ok=True)
fig.savefig("output/bai4_so_sanh_depth.png", dpi=120)

print("Nhan xet: Them trong tam lam mau day hon, nhung moi tam giac chi them mot diem.")
print("Tam giac lon van phu nhieu o luoi khong chua dinh hay trong tam, nen con o trong.")
print("Neu mo hinh co than dai voi it tam giac lon, vung nay co the van rat thua.")
print("Cac diem chong nhau khi chieu XY cung khong lam tang so pixel co du lieu.")
print("Cac o nam ngoai hinh chieu cua mo hinh luon trong.")
plt.show()
