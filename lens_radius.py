import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
import astropy.units as u

# FITS 파일 열기
fits_file = 'gravitylens.fits'  # 여기에 FITS 파일 경로를 입력하세요
hdulist = fits.open(fits_file)

# WCS 정보 추출
wcs = WCS(hdulist[1].header)

# 첫 번째 HDU 데이터 추출
data = hdulist[1].data

# 이미지 시각화 (이미지 범위 자동 조정)
plt.figure(figsize=(8, 8))
plt.imshow(data, cmap='gray', origin='lower', vmax=np.percentile(data, 99), vmin=np.percentile(data, 60)) # 이미지 범위 자동 조정
plt.colorbar()  # 색상 막대 추가
plt.title('FITS Image')

plt.xlim(800, 960)  # x축 범위 설정
plt.ylim(940, 1080)   # y축 범위 설정

# 사용자가 이미지에서 두 점을 클릭하도록 요청
print("Click on two points on the image.")
coords = plt.ginput(2)  # 두 좌표를 클릭할 수 있도록 함
plt.close()  # 클릭 후 이미지 창 닫기

# 클릭된 좌표 (픽셀 좌표)
x1, y1 = coords[0]
x2, y2 = coords[1]
print(f"Coordinates 1 (pixel): ({x1}, {y1})")
print(f"Coordinates 2 (pixel): ({x2}, {y2})")

# 픽셀 좌표를 천문 좌표(RA, Dec)로 변환
skycoord1 = wcs.pixel_to_world(x1, y1)
skycoord2 = wcs.pixel_to_world(x2, y2)

print(f"Coordinates 1 (RA, Dec): {skycoord1}")
print(f"Coordinates 2 (RA, Dec): {skycoord2}")

# SkyCoord 객체 생성
coord1 = SkyCoord(ra=skycoord1.ra, dec=skycoord1.dec, unit=(u.deg, u.deg))
coord2 = SkyCoord(ra=skycoord2.ra, dec=skycoord2.dec, unit=(u.deg, u.deg))

# 두 점 간의 각 거리 계산
separation = coord1.separation(coord2)

# 결과 출력 (각도 단위)
print(f"The angular separation is: {separation}")

# 예시: 두 점의 거리 정보가 각각 1 kpc인 경우 (옵션)
distance = 1 * u.kpc  # 두 점까지의 거리 (1 kpc)
physical_distance = separation.arcsec * u.arcsec.to(u.rad) * distance  # 물리적 거리 계산

print(f"Physical distance: {physical_distance}")

# 파일 닫기
hdulist.close()
