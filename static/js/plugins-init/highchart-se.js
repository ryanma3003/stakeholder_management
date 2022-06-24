Highcharts.chart('highchart-se', {
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
        text: 'Kategorisasi SE Chart'
    },
    xAxis: {
        categories: [
            'Strategis',
            'Tinggi',
            'Rendah'
        ]
    },
    yAxis: {
        min: 0,
        max: 50,
        tickInterval: 10,
        title: {
            text: 'Jumlah'
        }
    },
    legend: {
        enabled: false
    },
    tooltip: {
        pointFormat: '<b>{point.y}</b>'
    },
    series: [{
        name: 'Score',
        data: JSON.parse(bar_se_json),
        dataLabels: {
            enabled: true,
            rotation: 0,
            color: '#FFFFFF',
            align: 'right',
            format: '{point.y}',
            y: -10, // 10 pixels down from the top
        }
    }]
});