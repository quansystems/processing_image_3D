# Doc file STL (ho tro ca ASCII va binary) -> mang tam giac (M, 3, 3)
import numpy as np


def doc_stl(ten_file):
    with open(ten_file, "rb") as f:
        du_lieu = f.read()

    # Binary STL: 80 byte header + 4 byte so tam giac + 50 byte moi tam giac
    if len(du_lieu) >= 84:
        so_tg = int(np.frombuffer(du_lieu[80:84], dtype="<u4")[0])
        if 84 + 50 * so_tg == len(du_lieu):
            kieu = np.dtype([("normal", "<f4", 3), ("v", "<f4", (3, 3)), ("attr", "<u2")])
            ban_ghi = np.frombuffer(du_lieu[84:], dtype=kieu, count=so_tg)
            return ban_ghi["v"].astype(np.float64)

    # ASCII STL: lay cac dong "vertex x y z"
    dinh = []
    for dong in du_lieu.decode("utf-8", errors="ignore").splitlines():
        phan = dong.strip().split()
        if len(phan) == 4 and phan[0] == "vertex":
            dinh.append([float(x) for x in phan[1:]])
    return np.array(dinh, dtype=np.float64).reshape(-1, 3, 3)


def tao_dam_may_diem(ten_file):
    tam_giac = doc_stl(ten_file)
    diem_tho = tam_giac.reshape(-1, 3)
    diem = np.unique(diem_tho, axis=0)
    return tam_giac, diem_tho, diem
