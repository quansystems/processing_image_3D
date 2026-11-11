# Cau 1. Tao dam may diem tu mo hinh STL
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from stl_utils import doc_stl

# a. Doc ball.STL, in so tam giac
tam_giac = doc_stl("ball.STL")
print("a. So tam giac cua mo hinh:", len(tam_giac))

# b. Gop cac dinh thanh mang N x 3, loai cac hang trung toa do
diem_tho = tam_giac.reshape(-1, 3)
diem = np.unique(diem_tho, axis=0)
print("b. So diem truoc khi loai trung:", diem_tho.shape[0])
print("   So diem sau khi loai trung :", diem.shape[0])

# c. Ve dam may diem bang scatter 3D
fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(projection="3d")
ax.scatter(diem[:, 0], diem[:, 1], diem[:, 2], s=4, c="tab:blue")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Cau 1: Dam may diem tu ball.STL")
ax.set_box_aspect((1, 1, 1))
Path("output").mkdir(parents=True, exist_ok=True)
plt.savefig("output/bai1_point_cloud.png", dpi=120)
plt.show()
