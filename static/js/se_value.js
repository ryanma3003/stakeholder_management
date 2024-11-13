
$(document).on("change", '#id_nilai_investasi', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_nilai_investasi').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_nilai_investasi').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_nilai_investasi').val(1);
    } else {
        $('#id_bobot_nilai_investasi').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_total_anggaran', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_total_anggaran').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_total_anggaran').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_total_anggaran').val(1);
    } else {
        $('#id_bobot_total_anggaran').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_kewajiban', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_kewajiban').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_kewajiban').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_kewajiban').val(1);
    } else {
        $('#id_bobot_kewajiban').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_kriptografi', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_kriptografi').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_kriptografi').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_kriptografi').val(1);
    } else {
        $('#id_bobot_kriptografi').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_pengguna', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_pengguna').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_pengguna').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_pengguna').val(1);
    } else {
        $('#id_bobot_pengguna').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_data_pribadi', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_data_pribadi').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_data_pribadi').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_data_pribadi').val(1);
    } else {
        $('#id_bobot_data_pribadi').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_kritis_data', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_kritis_data').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_kritis_data').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_kritis_data').val(1);
    } else {
        $('#id_bobot_kritis_data').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_kritis_proses', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_kritis_proses').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_kritis_proses').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_kritis_proses').val(1);
    } else {
        $('#id_bobot_kritis_proses').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_dampak_kegagalan', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_dampak_kegagalan').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_dampak_kegagalan').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_dampak_kegagalan').val(1);
    } else {
        $('#id_bobot_dampak_kegagalan').val(0);
    }
}).triggerHandler('change');

$(document).on("change", '#id_potensi_kerugian', function () {
    if ($(this).val() == 'a') {
        $('#id_bobot_potensi_kerugian').val(5);
    } else if ($(this).val() == 'b') {
        $('#id_bobot_potensi_kerugian').val(2);
    } else if ($(this).val() == 'c') {
        $('#id_bobot_potensi_kerugian').val(1);
    } else {
        $('#id_bobot_potensi_kerugian').val(0);
    }
}).triggerHandler('change');