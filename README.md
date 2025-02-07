# Capstone Project 1: Proof of Concept: Sistem Peminjaman Mobil Demo Car pada Dealer XYZ by Hans Darmawan (JCDS2602)
## 1. Background

Dealer XYZ merupakan salah satu dealer yang menjual berbagai macam brand mobil yang ada di Indonesia. Dealer tersebut melakukan investasi mobil demo sebagai tujuan untuk mempromosikan mobil yang dijual oleh mereka. Dalam situasi tertentu, terdapat opsi kepada pelanggan untuk meminjam mobil demo tersebut. Ketika melakukan peminjaman mobil demo, Dealer XYZ akan melakukan pencatatan peminjaman dengan form. Hal ini menjadi tantangan tersendiri, sebab :

- **Operasional Mobil Demo Menjadi Kurang Efisien dan Efektif:** Proses peminjaman yang kurang efisien dan efektif ini dapat menyebabkan keterlambatan, kesalahan, dan ketidakpuasan pelanggan, baik pelanggan internal maupun eksternal.
- **Keterbatasan dalam Pengelolaan Data:** Metode pencatatan secara manual seringkali menyebabkan sulitnya pelacakan ketersediaan mobil demo, yang dapat mengarah kepada misinformasi.

## 2. Gap Analysis

Dari latar belakang yang telah ditulis sebelumnya, terdapat kesenjangan utama antara sistem saat ini dan kebutuhan pengguna yang belum dapat terpenuhi, antara lain:

- **Pencatatan Secara Manual Menyebabkan Human Error:** Sistem manual rentan terhadap kesalahan manusia dan proses konfirmasi ketersediaan mobil demo yang lambat.
- **Ketidakmampuan untuk Melacak Data Secara Real-Time:** Sistem yang tersedia memiliki kemungkinan untuk tidak menyediakan informasi ketersediaan mobil demo secara real-time. Akibatnya, hal tersebut akan menyulitkan pemantauan dan pengelolaan mobil demo secara efektif dan efisien.

## 3. Objectives

- Capstone Project ini ditujukan untuk melakukan proof of concept sistem peminjaman mobil demo yang sederhana namun berfungsi untuk mengelola proses peminjaman mobil, termasuk fungsionalitas CRUD (Create, Read, Update, Delete). Implementasi ini akan dilakukan tanpa menggunakan operasi file atau database. 

## 4. Project Scope (Scope of Work)

- Sistem ini akan dibangun menggunakan bahasa pemrograman Python.
- Terdapat 2 list of dictionary yang akan dibuat, yaitu data mobil dan data informasi peminjaman.
- Semua data akan disimpan dalam memori.
- Sistem ini akan mencakup:
  - Fungsionalitas untuk menambahkan data peminjaman mobil baru.
  - Fungsionalitas untuk melihat daftar peminjaman mobil.
  - Fungsionalitas untuk memperbarui informasi peminjaman yang ada.
  - Fungsionalitas untuk menghapus data peminjaman.
- Sistem ini dirancang sebagai capstone project dan tidak akan mencakup evaluasi dan umpan balik formal.

## 5. Requirements Analysis

- **Functional Requirements:**
  - Pengguna dapat menambahkan peminjaman baru dengan informasi seperti ID peminjaman, nama peminjam, tanggal peminjaman, dan detail mobil.
  - Pengguna dapat melihat semua peminjaman yang ada.
  - Pengguna dapat memperbarui informasi peminjaman yang ada.
  - Pengguna dapat menghapus peminjaman dari sistem.

## 6. System Design -> Menyesuaikan.

- **Data Structure:**
  - Data peminjaman akan disimpan dalam list atau dictionary Python. Setiap entri akan berisi informasi peminjaman. Contoh struktur data: `[{'id': 1, 'name': 'John Doe', 'date': '2024-03-08', 'car_details': 'Toyota Camry'}, ...]`

- **CRUD Functions:**
  - `create_rental(id, name, date, car_details)`: Menambahkan peminjaman baru.
  - `read_rentals()`: Menampilkan semua peminjaman.
  - `update_rental(id, name=None, date=None, car_details=None)`: Memperbarui informasi peminjaman yang ada.
  - `delete_rental(id)`: Menghapus peminjaman dari sistem.

## 7. Implementation
- Terlampir pada file [...].py

## 8. Testing Methods -> Tentatif -> Opsional, fokus ke implementasi
- Terlampir pada file Test Script.xlsx
- **Unit Testing:** Setiap fungsi (create_rental, read_rentals, update_rental, delete_rental) akan diuji secara individu untuk memastikan fungsionalitasnya memenuhi spesifikasi. Pengujian akan memverifikasi apakah fungsi menghasilkan output yang diharapkan untuk berbagai input, termasuk kasus batas dan kasus kesalahan (misalnya, mencoba menghapus peminjaman yang tidak ada).

- **Integration Testing:** Pengujian ini akan memverifikasi interaksi antara fungsi-fungsi. Misalnya, apakah data yang dibuat oleh fungsi create_rental dapat dibaca dengan benar oleh fungsi read_rentals.

## 9. Conclusion -> Menyesuaikan

Proof of concept ini bertujuan untuk menunjukkan bahwa sistem peminjaman mobil demo dapat dikembangkan menggunakan pendekatan yang sederhana dan efektif. Dengan implementasi fitur CRUD dasar, sistem ini dapat memberikan solusi yang efisien untuk mengelola peminjaman mobil, serta menjadi dasar untuk pengembangan lebih lanjut di masa depan. Karena ini adalah proyek capstone, evaluasi formal dan umpan balik pengguna tidak termasuk dalam ruang lingkup proof of concept ini.
