import math

# Adım 1: Noktaları tanımla
points = [(3, 4), (5, 12), (7, 24)]   # Örnek noktalar

# Adım 2: Öklid mesafesini hesaplayan bir fonksiyon yaz
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Adım 3: Tüm nokta çiftleri arasındaki mesafeleri hesapla
distances = []
for n in range(len(points)):
    for s in range(n+1, len(points)):
        distance = euclideanDistance(points[n], points[s])
        distances.append(distance)

# Adım 4: Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum distance: ", min_distance)