import math

# Öklid Mesafesi Hesaplama Fonksiyonu
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 1), (7, 7), (2, 8)]  # Örnek noktalar

# Mesafeleri Hesaplama
distances = []  # Mesafeleri tutan liste

# Tüm nokta çiftlerini döngü ile gezip mesafeleri hesaplıyoruz
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı noktaların tekrarlanmasını önlemek için
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonuçları Yazdırma
print("Tüm Nokta Çiftleri Arasındaki Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)
