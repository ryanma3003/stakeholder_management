var spider_result = JSON.parse(spider_json_csm).map(i=>Number(i));

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