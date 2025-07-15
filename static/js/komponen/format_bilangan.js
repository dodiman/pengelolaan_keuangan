function format_ribuan(n) {
    return new Intl.NumberFormat('id-ID').format(n);
  }

  
  
  const elm_input_total_harga = document.getElementById('id_total_harga_temp');
  const id_total_harga = document.getElementById('id_total_harga');
  
  // Inisialisasi nilai awal
  elm_input_total_harga.value = format_ribuan(elm_input_total_harga.value)
  
  elm_input_total_harga.addEventListener("input", () => {
    let angka = elm_input_total_harga.value.replace(/\D/g, "");
    if (angka == "") angka = "0";
    elm_input_total_harga.value = format_ribuan(angka);
    id_total_harga.value = angka;
  });