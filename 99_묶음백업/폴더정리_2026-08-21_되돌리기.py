# -*- coding: utf-8 -*-
"""2026-08-21 폴더 정리 되돌리기 — 역순 복원"""
import io, os, shutil, json
os.chdir(r'C:\\Users\\yurib\\Documents\\New project\\project black titan')
done = json.load(io.open(r'C:\\Users\\yurib\\Documents\\New project\\project black titan\\99_묶음백업\\폴더정리_2026-08-21_이동목록.json', encoding='utf-8'))
for src, dst in reversed(done):
    if os.path.isdir(dst) and not os.path.exists(src):
        shutil.move(dst, src)
        print('복원', dst, '->', src)
print('완료')
