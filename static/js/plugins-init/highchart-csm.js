// console.log(str_tatakelola);
var spider_result = JSON.parse(spider_json).map(i=>Number(i));
// console.log(spider_result);

Highcharts.chart('highchart-pie', {
    chart: {
        type: 'variablepie'
    },
    title: {
        text: 'CSM Doughnut Chart'
    },
    tooltip: {
        headerFormat: '',
        pointFormat: '<span style="color:{point.color}">\u25CF</span> <b> {point.name}</b><br/>' +
            'Maturity Score: <b>{point.y:.2f}</b><br/>'
    },
    plotOptions: {
        variablepie: {
            dataLabels: {
                distance: -50,
                format: '{point.y:.2f}',
                style: {
                    fontSize: '13px'
                }
            },
            showInLegend: true
        }
    },
    series: [{
        minPointSize: 1,
        innerSize: '40%',
        yMin: 0,
        yMax: 5,
        name: 'Aspect',
        data: [{
            name: 'Tata Kelola',
            y: parseFloat(str_tatakelola),
        }, {
            name: 'Identifikasi',
            y: parseFloat(str_identifikasi),
        }, {
            name: 'Proteksi',
            y: parseFloat(str_proteksi),
        }, {
            name: 'Deteksi',
            y: parseFloat(str_deteksi),
        }, {
            name: 'Respon',
            y: parseFloat(str_respon),
        }]
    }]
});

Highcharts.chart('highchart-radar', {

    chart: {
        polar: true
    },

    title: {
        text: 'CSM Polygon Chart'
    },

    pane: {
        startAngle: 0,
        endAngle: 360
    },

    xAxis: {
        tickInterval: 1,
        min: 0,
        max: 5,
        lineWidth: 0,
        labels: {
            formatter: function() {
            
                let label;
                switch (this.value) {
                case 0:
                    label = 'Tata Kelola';
                    break;
                case 1:
                    label = 'Identifikasi';
                    break;
                case 2:
                    label = 'Proteksi';
                    break;
                case 3:
                    label = 'Deteksi';
                    break;
                case 4:
                    label = 'Respon';
                    break;
                }
                
                return label;
            }
        }
    },

    yAxis: {
        min: 0,
        max: 6,
        tickInterval: 1,
       	gridLineInterpolation : 'polygon',
    },

    series: [{
        type: 'line',
        name: 'Maturity Score',
        data: spider_result
    }]
});

Highcharts.chart('highchart-csm', {
    chart: {
        type: 'column',
        height: 500,
        events: {
            load: function(event) {
            event.target.reflow();
          }
        }
    },
    title: {
        text: 'CSM Sub Aspect Chart'
    },
    xAxis: {
        labels: {
            groupedOptions: [{
                rotation: 0, // rotate labels for a 2nd-level
                align: 'right'
            }],
            rotation: -90, // 0-level options aren't changed, use them as always
        },
        categories: [{
            name: "Tata Kelola",
            categories: ["Kesadaran", "Audit", "Kontrol", "Pemenuhan", "Kebijakan", "Proses"]
        }, {
            name: "Identifikasi",
            categories: ["Manajemen Aset", "Inventaris", "Manajemen Risiko", "Prioritas", "Pelaporan", "Klasifikasi"]
        }, {
            name: "Proteksi",
            categories: ["Jaringan", "Aplikasi", "Pengguna", "Manajemen Identitas dan Aset", "Cloud", "Data"]
        }, {
            name: "Deteksi",
            categories: ["Perubahan", "Monitor", "Peringatan", "Pemberitahuan", "Intelijen", "Pelaporan"]
        }, {
            name: "Respon",
            categories: ["Penahanan", "Penganggulangan", "Pemulihan", "Kegiatan Paska Insiden", "Pelaporan"]
        }]
    },
    yAxis: {
        min: 0,
        max: 5,
        tickInterval: 1,
        title: {
            text: 'Score'
        }
    },
    legend: {
        enabled: false
    },
    tooltip: {
        pointFormat: '<b>{point.y:.2f}</b>'
    },
    series: [{
        name: 'Score',
        data: JSON.parse(bar_json),
        dataLabels: {
            enabled: true,
            rotation: 0,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y:.2f}', // two decimal
            y: -10, // 10 pixels down from the top
        }
    }]
});