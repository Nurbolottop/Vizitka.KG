//doughut chart
var ctx = document.getElementById("most-selling-items");
// ctx.height = 175;
new Chart(ctx, {
    type: "doughnut",
    data: {
        datasets: [
            {
                data: [33, 33, 33],
                backgroundColor: [
                    "rgba(22, 82, 240,1)",
                    "rgba(22, 82, 240,0.5)",
                    "rgba(22, 82, 240,0.15)",
                ],
                

            }],
            labels: [
                "Facebook",
                "Youtube",
                "Google",
            ]
        },
        options: {
            responsive: true,
            cutoutPercentage: 80,
            maintainAspectRatio: false, 
            animation: {
                animateRotate: true,
                animateScale: true,
            },
        labels: ["Facebook", "Youtube", "Google"],
    },
    options: {
        responsive: true,
        cutoutPercentage: 80,
        maintainAspectRatio: false,
        animation: {
            animateRotate: true,
            animateScale: true,
        },
        legend: {
            display: true,
            position: "bottom",
            labels: {
                usePointStyle: true,
                // fontFamily: "Segoe UI",
                fontSize: 12,
                fontColor: "#464a53",
                padding: 20,
            },
        },
    },
});
